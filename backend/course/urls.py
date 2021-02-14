from rest_framework.routers import SimpleRouter
from .views import CourseViewset, LessonViewset, InstructorViewset

router = SimpleRouter()
router.register('courses', CourseViewset, basename='courses')
router.register('lessons', LessonViewset, basename='lessons')
router.register('instructors', InstructorViewset, basename='lessons')


urlpatterns = router.urls
