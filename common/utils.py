from common.models import File


def get_file_related_fields(instance):
    """
    Returns a list of field names on `instance` that are relations to File.
    This checks for ForeignKey and OneToOneField relationships.
    """
    file_fields = []
    for field in instance._meta.get_fields():
        # Check if the field has a remote field and that its related model is File
        if hasattr(field, "remote_field") and field.remote_field:
            if field.remote_field.model == File:
                file_fields.append(field.name)

    return file_fields
