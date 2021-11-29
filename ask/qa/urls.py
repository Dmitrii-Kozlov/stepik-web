
from django.urls import path

from .views import test, detail_question, new_list, popular, question_add

urlpatterns = [
    path("", new_list, name="main"),
    path("login/", test),
    path("signup/", test),
    path("question/<pk>/", detail_question, name="detail"),
    path("ask/", question_add, name="add_question"),
    path("popular/", popular, name="popular"),
    path("new/", test)
]