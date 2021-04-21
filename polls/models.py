from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.db import models


class Polls(models.Model):
    name = models.TextField(verbose_name='Название опроса')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    end_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания')
    description = models.TextField(verbose_name='Описание опроса')

    def __str__(self):
        return self.name


class Question(models.Model):
    TYPE_CHOICES = (
        ('text', 'text'),
        ('one_select', 'one selected'),
        ('multiple_select', 'multiple selected'),
    )

    poll = models.ForeignKey(Polls, on_delete=models.CASCADE, verbose_name='Название опроса', related_name='questions')
    text = models.TextField(verbose_name='Текст вопроса')
    type = models.CharField(max_length=255, verbose_name='Тип вопроса', choices=TYPE_CHOICES)

    def __str__(self):
        return self.text


class Answer(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    answer = ArrayField(models.TextField(verbose_name='Ответ пользователя'))
    incognito = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
