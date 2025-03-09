from django.contrib import admin

from common.admin import BaseAdmin
from lawfirm.models.customer import Customer, CustomerIssue, CustomerIssueFile
from lawfirm.models.lawfirm import Lawfirm


@admin.register(Customer)
class CustomerAdmin(BaseAdmin):
    pass


@admin.register(CustomerIssue)
class CustomerIssueAdmin(BaseAdmin):
    pass

@admin.register(CustomerIssueFile)
class CustomerIssueFileAdmin(BaseAdmin):
    pass

@admin.register(Lawfirm)
class LawfirmAdmin(BaseAdmin):
    pass
