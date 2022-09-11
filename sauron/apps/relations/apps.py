from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RelationConfig(AppConfig):
    name = "sauron.apps.relations"
    verbose_name = _("Relations")

    def ready(self) -> None:
        try:
            import sauron.apps.relations.signals  # noqa F401
        except ImportError:
            pass
