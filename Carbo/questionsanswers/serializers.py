from rest_framework import serializers

from questionsanswers.models import Question
from questionsanswers.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'next_question_id']


class AnswersStoreSerializer(serializers.Serializer):
    question_id = serializers.IntegerField(required=True)
    answers = serializers.ListField(
        child=serializers.CharField()
    )


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    type_answer = serializers.ChoiceField(choices=Question.ANSWER_TYPES, source='get_type_answer_display')

    class Meta:
        model = Question
        fields = ('id', 'text', 'type_answer', 'next_question_id', 'answers', 'type_answer')
