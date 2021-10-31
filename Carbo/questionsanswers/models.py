from django.db import models


# Create your models here.

class Question(models.Model):
    ANSWER_TYPES = [
        (1, 'radio'),
        (2, 'checkbox'),
        (3, 'input'),
        (4, 'counter'),
    ]

    text = models.TextField(
        verbose_name='Text',
    )
    type_answer = models.IntegerField(
        verbose_name='Type Answer',
        max_length=20,
        choices=ANSWER_TYPES
    )
    next_question = models.ForeignKey(
        'self',
        verbose_name='Next question id',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 related_name='answers'
                                 )
    next_question = models.ForeignKey(
        Question,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+'
    )
