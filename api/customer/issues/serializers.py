from rest_framework import serializers

from lawfirm.models import CustomerIssue, CustomerIssueFile


class CustomerIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerIssue
        fields = [
            "code",
            "name",
            "human_description",
            "ai_description",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        customer = self.context["customer"]

        customer_issue = super().create(validated_data)
        customer_issue.customer = customer
        customer_issue.save()

        return customer_issue


class CustomerIssueFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerIssueFile
        fields = [
            "code",
            "name",
            "file",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        issue = self.context["issue"]

        customer_issue_file = super().create(validated_data)
        customer_issue_file.issue = issue
        customer_issue_file.save()

        return customer_issue_file
