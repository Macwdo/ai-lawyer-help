from django.db import models

from common.models import BaseModel


def upload_to(instance, filename):
    return f"{instance.__class__.__name__.lower()}/{instance.code}/{filename}"


class Customer(BaseModel):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


class CustomerIssue(BaseModel):
    name = models.CharField(max_length=200)
    human_description = models.TextField()
    ai_description = models.TextField()

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)


class CustomerIssueFile(BaseModel):
    name = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to=upload_to)
    issue = models.ForeignKey(CustomerIssue, on_delete=models.CASCADE, null=True)
