from rest_framework import viewsets

from .models import Question, Answer
from .serializers import AnswersStoreSerializer
from .serializers import QuestionSerializer


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswersViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswersStoreSerializer
