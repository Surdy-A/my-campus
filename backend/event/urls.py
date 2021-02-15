from rest_framework.routers import SimpleRouter
from .views import EventViewset

router= SimpleRouter()
router.register('events', EventViewset, basename='events')

urlpatterns = router.urls
