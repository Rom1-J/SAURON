from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from sauron.apps.relations.api.views import RelationViewSet, TagViewSet
from sauron.apps.users.api.views import UserViewSet


router: DefaultRouter | SimpleRouter = SimpleRouter()

if settings.DEBUG:
    router = DefaultRouter()

router.register("users", UserViewSet)
router.register("relations", RelationViewSet)
router.register("tags", TagViewSet)


app_name = "api"
urlpatterns = router.urls
