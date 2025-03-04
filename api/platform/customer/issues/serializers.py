from rest_framework import serializers
from lawfirm.models.customer import CustomerIssue


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
