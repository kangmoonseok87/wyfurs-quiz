from django.urls import path, include
from .views import hellowAPI, randomQuiz

urlpatterns = [
    path("hellow/", hellowAPI),
    path("<int:id>", randomQuiz),
]

