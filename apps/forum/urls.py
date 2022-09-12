from django.urls import path

from .views import *

urlpatterns = [
    path('', QuestionListView.as_view(), name='question_list'),
    path('create/', QuestionCreateView.as_view(), name='question_create'),
    path('<int:pk>/update/', QuestionUpdateView.as_view(), name='question_update'),
    path('<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('del/<int:pk>/', QuestionDeleteView.as_view(), name='question_delete'),
    path('<int:pk>/<int:a_pk>/', AnswerDetailView.as_view(), name='answer_detail'),
    path('<int:pk>/<int:a_pk>/update/', AnswerUpdateView.as_view(), name='answer_update'),
    path('<int:pk>/<int:a_pk>/delete/', AnswerDeleteView.as_view(), name='answer_delete'),
    path('<int:pk>create/', AnswerCreateView.as_view(), name='answer_create'),

]
