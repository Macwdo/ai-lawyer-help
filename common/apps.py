from django.apps import AppConfig, apps
from django.db.models.signals import post_delete


class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "common"

    def ready(self):
        """Register signals after all migrations are completed."""
        self._register_all_base_models()

    def _register_all_base_models(self, **kwargs):
        from common.services.loggers.app_logger import ApplicationLogger
        from common.signals import base_model_post_delete

        logger = ApplicationLogger()
        for model in apps.get_models():
            logger.info(f"Registering post_delete signal for {model.__name__}")
            post_delete.connect(base_model_post_delete, sender=model, weak=False)
