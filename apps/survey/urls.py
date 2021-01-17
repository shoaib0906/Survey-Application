from django.urls import path,include
from .views import  survey_detail, edit_survey, add_survey,index_survey,delete_survey,view_report,mailsend

urlpatterns = [
    path('<int:survey_id>/', survey_detail, name='survey_detail'),
    path('add', add_survey, name='add_survey'),
    path('<int:survey_id>/edit', edit_survey, name='edit_survey'),
    path('mailsend', mailsend, name='mailsent'),
    path('<int:survey_id>/delete',delete_survey,name='delete_survey'),
    path('', index_survey, name='index_survey'),
    path('<int:survey_id>/view_report',view_report,name='view_report'),
]