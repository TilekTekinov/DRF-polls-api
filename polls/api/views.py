import datetime
from dateutil import parser

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from polls.models import Polls, Question, Answer
from polls.api.serializers import PollsSerializer, QuestionSerializer, AnswerSerializer
from polls.api.permissions import IsAdminUserOrReadOnly


class PollsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Polls.objects.all().order_by('id')
    serializer_class = PollsSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class PollsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Polls.objects.all()
    serializer_class = PollsSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_update(self, serializer):
        polls_pk = self.kwargs.get('pk')
        polls = get_object_or_404(Polls, pk=polls_pk)
        polls_queryset = Polls.objects.get(pk=polls.pk)
        if self.request.data.get('create_date'):
            if str(parser.parse(self.request.data.get('create_date'))) not in str(polls_queryset.create_date):
                raise ValidationError("You can't change created date!")
            else:
                serializer.save()


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class PollsListAPIView(generics.ListAPIView):
    queryset = Polls.objects.filter(end_date__gt=datetime.datetime.now()).order_by('id')
    serializer_class = PollsSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        print(self.request.data)
        if self.request.data.get('incognito'):
            serializer.save(user_id=None,
                            answer=self.request.data.get('answer'),
                            incognito=self.request.data.get('incognito'),
                            question_id=self.request.data.get('question'))
        else:
            serializer.save()


class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        answers = Answer.objects.filter(user_id=self.kwargs.get('pk'))
        return answers

