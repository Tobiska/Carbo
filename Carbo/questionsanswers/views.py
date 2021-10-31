from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .serializers import AnswersStoreSerializer
from .serializers import QuestionListSerializer


# Create your views here.

class QuestionCreateView(APIView):
    def post(self, request):
        questions = Question.objects.all()
        serializer = AnswersStoreSerializer(data=request.data, many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response({
            'msg': "data is invalid"
        }, 422)


class QuestionListView(APIView):

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionListSerializer(questions, many=True)
        return Response(serializer.data)