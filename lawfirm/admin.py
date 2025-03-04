from django.contrib import admin

from lawfirm.models.customer import Customer, CustomerIssue
from lawfirm.models.lawfirm import Lawfirm


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomerIssue)
class CustomerIssueAdmin(admin.ModelAdmin):
    pass


@admin.register(Lawfirm)
class LawfirmAdmin(admin.ModelAdmin):
    pass
