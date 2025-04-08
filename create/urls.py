from django.urls import path
from . import views

app_name = "create"

urlpatterns = [
    path('course-edit/<int:course_id>/', views.course_edit, name="course_edit"),
    path('upload-lesson/<int:course_id>/', views.upload_lesson, name="upload_lesson"),
]
