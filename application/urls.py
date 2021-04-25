from django.urls import path
from . import views


urlpatterns = [
    path('list_quiz_takers', views.QuizTakerData.as_view()),
    path('start/', views.StartQuiz.as_view()),
    path('start/<int:category_id>/', views.StartQuiz.as_view()),
]
