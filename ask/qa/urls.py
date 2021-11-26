
from django.urls import path

from .views import test, detail_question, new_list, popular

urlpatterns = [
    path("", new_list, name="main"),
    path("login/", test),
    path("signup/", test),
    path("question/<pk>/", detail_question, name="detail"),
    path("ask/", test),
    path("popular/", popular, name="popular"),
    path("new/", test)
]