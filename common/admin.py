from django.contrib import admin

from common.models import File

class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("code", "created_at", "updated_at",)


@admin.register(File)
class FileAdmin(BaseAdmin):
    pass
