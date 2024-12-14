from django.urls import path
from .views import (PartnershipCreateView, ManagerPartnershipListView, DefaultPartnershipListView, PartnershipQuestionCreateView, ManagerQuestionListView,
DefaultQuestionListView, PartnershipAnswerCreateView
                    )

app_name = 'partner'
urlpatterns = [
    path('partnership/create/', PartnershipCreateView.as_view(), name='create-partnership'),
    path('partnership/manager/', ManagerPartnershipListView.as_view(), name='manager_partnership_list'),
    path('partnership/default/', DefaultPartnershipListView.as_view(), name='default_partnership_list'),
    path('partnership/question/', PartnershipQuestionCreateView.as_view(), name='partnership-question'),
    path('question/manager/', ManagerQuestionListView.as_view(), name='manager_question_list'),
    path('question/default/', DefaultQuestionListView.as_view(), name='default_question_list'),
    path('answer/create/', PartnershipAnswerCreateView.as_view(), name='answer-create')




]