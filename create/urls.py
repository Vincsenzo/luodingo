from django.urls import path
from . import views

app_name = "create"

urlpatterns = [
    path('upload_lesson/<int:course_id>/', views.upload_lesson, name="upload_lesson"),
]
