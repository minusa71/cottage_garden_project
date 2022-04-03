from datetime import date
from enum import auto

from django import forms

from Cottage_garden_project.accounts.models import Profile
from Cottage_garden_project.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from Cottage_garden_project.common.validators import MaxDateValidator
from Cottage_garden_project.main.models import Garden,  Plant, PlantProtection, UseFullTips


class CreateGardenForm(BootstrapFormMixin,forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()


    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        garden = super().save(commit=False)

        garden.user = self.user
        if commit:
            garden.save()

        return garden

    class Meta:
        model = Garden
        fields = ('name', 'type', 'address', 'image')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter garden name',
                }

            ),
        }


class CreatePlantForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        plant = super().save(commit=False)

        plant.user = self.user
        if commit:
            plant.save()

        return plant

    class Meta:
        model = Plant
        fields = ('name', 'type', 'sort', 'image','year', 'plant_protections', 'harvest_quantity' , 'garden')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter plant name',
                }
            ),
        }


class EditPlantForm(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_date_of_birth(self):
        MaxDateValidator(date.today())(self.cleaned_data['date_of_birth'])
        return self.cleaned_data['date_of_birth']

    class Meta:
        model = Plant
        exclude = ('user_profile',)


class DeletePlantForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Plant
        exclude = ('user_profile',)



class CreatePlantProtectionForm(forms.ModelForm):
    class Meta:
        model = PlantProtection
        fields = ('product_name', 'description', 'price')


class CreateUseFullTipsForm(forms.ModelForm):
    class Meta:
        model = UseFullTips
        fields = ('plant_name', 'text_field')

# class UserDashboardForm(forms.ModelForm):
