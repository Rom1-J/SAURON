from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "sauron.apps.users"
    verbose_name = _("Users")

    def ready(self) -> None:
        try:
            import sauron.apps.users.signals  # noqa F401
        except ImportError:
            pass
