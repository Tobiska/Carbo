from django.test import TestCase
from questionsanswers.models import Question, Answer
from django.db import transaction
from django.db.utils import IntegrityError


class QuestionTestCase(TestCase):

    MEAT_TEXT = "How much money do you spend on meat?"
    ENUM = "9c923741-0e0e-4c83-b545-cd06d79013aa"

    def setUp(self):
        Question.objects.create(text=self.MEAT_TEXT, enum=self.ENUM, type_answer=Question.ANSWER_TYPES[0][0])

    def test_answer_types(self):
        """When adding a new answer type, you need to update the tests."""
        self.assertEqual(len(Question.ANSWER_TYPES), 4)
        self.assertEqual(Question.ANSWER_TYPES[0][1], 'radio')
        self.assertEqual(Question.ANSWER_TYPES[1][1], 'checkbox')
        self.assertEqual(Question.ANSWER_TYPES[2][1], 'input')
        self.assertEqual(Question.ANSWER_TYPES[3][1], 'counter')

    def test_str_method(self):
        """Test __str__ function for Question"""
        meat_question = Question.objects.get(enum=self.ENUM)
        self.assertEqual(meat_question.__str__(), f"{meat_question.enum}:{meat_question.text}")

    def test_check_integrity(self):
        """In the question 'type_answer' must not be null, 'text' must not be null, 'enum' must be unique"""

        with (self.assertRaises(IntegrityError), transaction.atomic()):
            Question.objects.create(text="In this question 'type_answer' is null")

        with (self.assertRaises(IntegrityError), transaction.atomic()):
            Question.objects.create(text="Enum unique failed", enum=self.ENUM, type_answer=Question.ANSWER_TYPES[1][0])


class AnswerQuestionTestCase(TestCase):

    MEAT_TEXT = "How much money do you spend on meat?"
    SOME_TEXT = "A lot"
    ENUM = "9c923741-0e0e-4c83-b545-cd06d79013aa"

    def setUp(self):
        question = Question.objects.create(text=self.MEAT_TEXT, enum=self.ENUM, type_answer=Question.ANSWER_TYPES[0][0])
        Answer.objects.create(text=self.SOME_TEXT, enum=self.ENUM, question=question)

    def test_str_method(self):
        """Test __str__ function for Answer"""
        some_answer = Answer.objects.get(enum=self.ENUM)
        self.assertEqual(some_answer.__str__(), f"{some_answer.enum}:{some_answer.text}")

    def test_check_integrity(self):
        """In the answer 'question' must not be null, 'enum' must be unique"""

        with (self.assertRaises(IntegrityError), transaction.atomic()):
            Answer.objects.create()

        with (self.assertRaises(IntegrityError), transaction.atomic()):
            question = Question.objects.get(enum=self.ENUM)
            Answer.objects.create(text=self.SOME_TEXT, enum=self.ENUM, question=question)
