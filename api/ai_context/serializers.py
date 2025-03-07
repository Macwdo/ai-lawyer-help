from rest_framework import serializers


class AiContextUploadSerializer(serializers.Serializer):
    SOURCES = (
        ["customer_issue", "customer_issue"],
        ["lawsuit", "lawsuit"],
    )

    file_code = serializers.CharField(max_length=255)

    source_code = serializers.CharField(max_length=255)
    source = serializers.ChoiceField(choices=SOURCES)
