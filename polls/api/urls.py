from django.urls import path
from polls.api.views import *


urlpatterns = [
    # admin links
    path('polls/', PollsListCreateAPIView.as_view(), name='polls-list-create'),
    path('polls/<int:pk>/', PollsDetailAPIView.as_view(), name='polls-detail'),
    path('polls/<int:pk>/questions/', QuestionListCreateAPIView.as_view(), name='questions-list-create'),
    path('polls/<int:polls_pk>/questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='questions-detail'),

    # user links
    path('active-polls/', PollsListAPIView.as_view(), name='active-polls-list'),
    path('polls/<int:polls_pk>/questions/<int:question_pk>/answer/', AnswerCreateAPIView.as_view(), name='user-answer-create'),
    path('answers/<int:user_pk>/', AnswerListAPIView.as_view(), name='user-answers-list')
]
