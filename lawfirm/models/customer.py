from django.db import models

from common.models import BaseModel, File


class Customer(BaseModel):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    picture = models.ForeignKey(File, on_delete=models.CASCADE, null=True)


class CustomerIssue(BaseModel):
    name = models.CharField(max_length=200)
    human_description = models.TextField()
    ai_description = models.TextField()

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)


class CustomerIssueFile(BaseModel):
    class Meta:
        unique_together = ("customer_issue", "file")

    customer_issue = models.ForeignKey(CustomerIssue, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
