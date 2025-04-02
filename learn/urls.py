from django.urls import path
from . import views

app_name = "learn"

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('lesson/<int:lesson_id>/<int:exercise_order>/', views.lesson_detail, name='lesson_detail_order'),
]
