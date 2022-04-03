from django.contrib import admin

# Register your models here.
from Cottage_garden_project.main.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
