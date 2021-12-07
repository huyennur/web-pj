from django.contrib import admin
from donation.models import Donation, Regis_teach, Introduce
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class DonationManagement(admin.ModelAdmin):
    fields = ['StudentCode', 'FirstName', 'LastName', 'Email', 'PhoneNumber',
              'BankAccountNumber', 'AmountOfDonation', 'DonationDate', 'Messages']


class IntroduceManagement(admin.ModelAdmin):
    fields = ['StudentCode', 'FirstName', 'LastName', 'Email', 'PhoneNumber',
              'BankAccountNumber', 'AmountOfDonation', 'DonationDate', 'Messages']


class RegisManagement(admin.ModelAdmin):
    fields = ['StudentCode', 'FirstName', 'LastName', 'Email', 'PhoneNumber',
              'BankAccountNumber', 'AmountOfDonation', 'DonationDate', 'Messages']


class DonationResources(resources.ModelResource):
    class Meta:
        model = Donation


class Regis_teachResources(resources.ModelResource):
    class Meta:
        model = Regis_teach


class IntroduceResources(resources.ModelResource):
    class Meta:
        model = Introduce


class DonationAdmin(ImportExportModelAdmin):
    list_display = ('StudentCode', 'FirstName', 'LastName', 'Email', 'PhoneNumber',
                    'BankAccountNumber', 'AmountOfDonation', 'DonationDate', 'Messages')
    resources_class = DonationResources


class IntroduceAdmin(ImportExportModelAdmin):
    list_display = ('StudentCode', 'FirstName', 'LastName',
                    'intro_title', 'intro_content')
    resources_class = IntroduceResources


class RegisAdmin(ImportExportModelAdmin):
    list_display = ('StudentCode', 'FirstName', 'LastName',
                    'teach_title', 'teach_date', 'teach_mess')
    resources_class = Regis_teachResources


admin.site.register(Donation, DonationAdmin)
admin.site.register(Introduce, IntroduceAdmin)
admin.site.register(Regis_teach, RegisAdmin)
