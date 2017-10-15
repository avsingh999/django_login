from rest_framework.routers import DefaultRouter

from .api import CardViewSet

router = DefaultRouter()
router.register(r'cards', CardViewSet)

urlpatterns = router.urls
