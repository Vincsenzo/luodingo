from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Exercise(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="exercises")
    order = models.PositiveIntegerField()
    text = models.TextField()  # The exercise text with blanks

    class Meta:
        ordering = ['order']  # Ensures exercises are fetched in order

    def __str__(self):
        return f"{self.text}"

class AnswerChoice(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.exercise.text} - {self.text} - {self.is_correct}"
