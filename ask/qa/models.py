from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class QuestionManager(models.Manager):
    def new(self, number_of_questions=5):
        return self.model.objects.all().order_by("-added_at")[:number_of_questions]

    def popular(self, number_of_questions=5):
        return self.model.objects.all().order_by("rating")[:number_of_questions]


class Question(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    likes = models.ManyToManyField(User, related_name="questions_liked")

    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
