from rest_framework import serializers

from lawfirm.models.customer import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "code",
            "name",
            "phone",
            "email",
            "created_at",
            "updated_at",
            "picture",
        ]
