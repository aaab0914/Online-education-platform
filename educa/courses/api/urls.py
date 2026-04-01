from django.urls import (
    path,
    include
)
from rest_framework import routers

from . import views

app_name = 'course'

router = routers.DefaultRouter()
router.register(
    'courses',
    views.CourseViewSet,
    basename='courses'
)
router.register(
    'subjects',
    views.SubjectViewSet,
    basename='subjects'
)

urlpatterns = [
   path(
       '',
       include(router.urls)
   ),
   # path(
   #     'courses/<pk>/enroll/',
   #     views.CourseEnrollView.as_view(),
   #     name='course_enroll'
   # ),
   # path(
   #     'subjects/',
   #     views.SubjectListView.as_view(),
   #     name='subject_list'
   # ),
   #  path(
   #      'subjects/<pk>/',
   #      views.SubjectDetailView.as_view(),
   #      name='subject_detail'
   #  ),
]