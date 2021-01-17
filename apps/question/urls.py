from django.urls import path,include
from .views import  add_question,show_questions,option_view,edit_question,answer_questions,index_question,delete_question

urlpatterns = [
    path('add', add_question, name='add_question'),
    path('', index_question, name='index_question'),
    path('<int:survey_id>/showall',show_questions,name='show_questions'),
    path('<int:question_id>/optionview',option_view,name='option_view'),
    path('<int:question_id>/edit',edit_question,name='edit_question'),
    path('<int:question_id>/delete',delete_question,name='delete_question'),

    path('<int:survey_id>/answer',answer_questions,name='answer_questions'),


]