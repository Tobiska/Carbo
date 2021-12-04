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

    enum = models.CharField(
        verbose_name='Unique str identifier',
        max_length=255,
        unique=True,
    )

    type_answer = models.IntegerField(
        verbose_name='Type Answer',
        choices=ANSWER_TYPES
    )
    next_question = models.ForeignKey(
        'self',
        verbose_name='Next question id',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.enum.__str__() + ':' + self.text.__str__()


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

    enum = models.TextField(
        verbose_name='Unique str identifier',
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.enum.__str__() + ':' + self.text.__str__()
