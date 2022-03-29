from rest_framework import routers
from .views import StudentViewSet, SubjectViewSet

from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('school/', include(router.urls))
]