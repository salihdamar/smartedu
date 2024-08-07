from django.urls import path
from .views import TeacherListView,TeacherDetailView

urlpatterns = [
    path('', TeacherListView.as_view(), name="teachers"),
    path('teacher/<pk>',TeacherDetailView.as_view(),name="teacher_detail")
]
