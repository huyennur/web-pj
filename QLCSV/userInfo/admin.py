from django.contrib import admin
from .models import Profile
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.


class ProfileManagement(admin.ModelAdmin):
    fields = ['user', 'image']


class ProfileResources(resources.ModelResource):
    class Meta:
        models = Profile


class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('user', 'image')
    resources_class = ProfileResources


admin.site.register(Profile, ProfileAdmin)
