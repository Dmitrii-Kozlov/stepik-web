from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

"""
QuestionManager - менеджер модели Question
new - метод возвращающий последние добавленные вопросы
popular - метод возвращающий вопросы отсортированные по рейтингу

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

"""


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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User)

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
