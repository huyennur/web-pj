from django.contrib import admin
from donation.models import Donation
from import_export.admin import ImportExportModelAdmin
from import_export import resources


# class ReportManagement(admin.ModelAdmin):
#     fields = ['StudentCode', 'FirstName', 'LastName', 'Email', 'PhoneNumber',
#               'BankAccountNumber', 'AmountOfDonation', 'DonationDate', 'Messages']


# class DonationResources(resources.ModelResource):
#     class Meta:
#         models = Donation


# class DonationAdmin(ImportExportModelAdmin):
#     list_display = ('StudentCode', 'FirstName', 'LastName', 'Email', 'PhoneNumber',
#                     'BankAccountNumber', 'AmountOfDonation', 'DonationDate', 'Messages')
#     resources_class = DonationResources


# admin.site.register(Donation, DonationAdmin)

# admin.site.register(Report, ReportManagement)
