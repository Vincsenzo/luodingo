from django.contrib import admin
from .models import Course, Lesson, Exercise, AnswerChoice

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Exercise)
admin.site.register(AnswerChoice)
