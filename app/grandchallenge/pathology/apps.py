from django.apps import AppConfig


class Config(AppConfig):
    name = "grandchallenge.pathology"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass