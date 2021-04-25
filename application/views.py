from django.http import Http404
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import QuizTakers, Quiz
from .serializers import QuizTakersSerializer, QuestionSerializer


class QuizTakerData(generics.ListAPIView):
    serializer_class = QuizTakersSerializer
    queryset = QuizTakers.objects.all()


class StartQuiz(APIView):

    def get(self, request, id=None):
        try:
            quiz = Quiz.objects.get(id=id)
        except Quiz.DoesNotExist:
            raise Http404
        serializer = QuestionSerializer(quiz.question.all(), many=True)
        return Response(serializer.data)
