import csv
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from learn.models import Course, Lesson, Exercise, AnswerChoice
from django.contrib import messages

def upload_lesson(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST" and request.FILES.get("csv_file"):
        csv_file = request.FILES["csv_file"]
        
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "Please upload a valid CSV file.")
            return redirect('create:upload_lesson', course_id=course.id)

        # Process CSV file
        file_path = default_storage.save(f'temp/{csv_file.name}', ContentFile(csv_file.read()))
        
        try:
            with open(default_storage.path(file_path), newline='', encoding="utf-8") as file:
                reader = csv.reader(file)
                lesson = None
                
                for i, row in enumerate(reader):
                    if i == 0:  # First row is the lesson title
                        lesson = Lesson.objects.create(course=course, title=row[0])
                    else:  # Remaining rows are exercises
                        exercise_text, correct_answer, *other_choices = row
                        exercise = Exercise.objects.create(lesson=lesson, text=exercise_text, order=i)
                        AnswerChoice.objects.create(exercise=exercise, text=correct_answer, is_correct=True)
                        
                        for choice in other_choices:
                            AnswerChoice.objects.create(exercise=exercise, text=choice, is_correct=False)
            
            # After processing, delete the temporary file
            default_storage.delete(file_path)
            messages.success(request, "Lesson uploaded successfully!")
        
        except Exception as e:
            # In case of any error during processing, delete the file and show an error
            default_storage.delete(file_path)
            messages.error(request, f"An error occurred: {e}")
            return redirect('create:upload_lesson', course_id=course.id)

        return redirect('learn:course_detail', course_id=course.id)

    return render(request, "create/upload_lesson.html", {"course": course})
