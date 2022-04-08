from django.contrib import admin

# Register your models here.
from Cottage_garden_project.main.models import Profile, Plant


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    class Meta:
        model = Plant
        fields = ('name', 'type', 'sort', 'image','year', 'harvest_quantity' , 'garden')