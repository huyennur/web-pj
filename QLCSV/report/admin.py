from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from report.models import Report


class ReportManagement(admin.ModelAdmin):
    fields = ['Name', 'Title', 'Messages', 'ReportDate']


class ReportResource(resources.ModelResource):
    class Meta:
        model = Report


class ReportAdmin(ImportExportModelAdmin):
    list_display = ('Name', 'Title', 'Messages', 'ReportDate')
    resources_class = ReportResource


admin.site.register(Report, ReportAdmin)
