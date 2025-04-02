import random

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from .models import Lesson, Exercise, AnswerChoice, Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'learn/index.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'learn/course_detail.html', {'course': course})


def lesson_detail(request, lesson_id, exercise_order=1):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    exercises = lesson.exercises.all()
    exercises_count = exercises.count()

    # Check if there are any exercises
    if not exercises:
        return redirect('learn:course_detail', course_id=lesson.course.id)

    # Get current exercise based on order
    exercise = exercises.filter(order=exercise_order).first()

    # If no more exercises, go back to course detail
    if not exercise:
        return redirect('learn:course_detail', course_id=lesson.course.id)

    # Handle answer submission
    if request.method == "POST":
        selected_id = request.POST.get("choice_id")
        selected_choice = AnswerChoice.objects.get(id=selected_id)
        is_correct = selected_choice.is_correct
        return JsonResponse({"correct": is_correct})

    return render(request, "learn/lesson_detail.html", {
        "lesson": lesson,
        "exercise": exercise,
        "exercises_count": exercises_count,
        "choices": random.sample(list(exercise.choices.all()), len(exercise.choices.all())),  # Shuffle choices
        "next_order": exercise.order + 1
    })
