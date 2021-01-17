from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from apps.question.models import Question,Answer,Option
from .forms import AddSurveyForm,MailsentForm
from .models import Survey,Mailtrack
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import SurveySerializer
from rest_framework import viewsets


def survey_detail(request, survey_id):
    survey = Survey.objects.get(pk=survey_id)
    return render(request, 'survey/survey_details.html', {'survey': survey})

def view_report(request, survey_id):
    surveys = Survey.objects.filter(id=survey_id)
    return render(request, 'question/report.html', {'surveys': surveys})

class SurveyApiView(APIView):
    def get(self,request):
        allSurvey=Survey.objects.all().values()
        return Response({"Message":"List of Survey", "Survey List":allSurvey})


@login_required
def delete_survey(request, survey_id):
    surveys = Survey.objects.filter(created_by=request.user,id=survey_id).delete()
    messages.success(request, 'Survey Deleted Successfully')
    return render(request, 'survey/index.html', {'surveys': surveys})

@login_required
def mailsend(request):
    if request.method == 'POST':
        form = MailsentForm(request.POST)

        if form.is_valid():
            survey = get_object_or_404(Survey, id=request.POST['survey_id'])
            # user = get_object_or_404(User, id=request.user)
            #for i in request.POST.getlist('mail_id'):
            mailse = Mailtrack.objects.create(mail_id=request.POST['mail_id'],survey_id=survey,created_by=request.user)
            mailse.save()

            # Answer.objects.filter(created_by=request.user).delete()
            questions = Question.objects.filter(survey_id=request.POST['survey_id'])
            alreadyanswer = ''
            answers = ''
            # return HttpResponse(answers)
            # return render(request, 'question/answer_question.html',
            #               {'questions': questions, 'answers': answers, 'alreadyanswer': alreadyanswer})
            subject = 'Invitation for be a participants for a Survey'
            html_message = render_to_string( 'survey/mail.html',
                          {'questions': questions, 'answers': answers, 'alreadyanswer': alreadyanswer})
            plain_message = strip_tags(html_message)
            from_email = '<Support@surveytest.com>'
            to = request.POST['mail_id']

            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
            #messages = 'Mail Sent with Survey Successfully'
            messages.success(request, 'Mail Sent with Survey Successfully')
            return redirect('mailsent')
    else:
        mailsent = Mailtrack.objects.filter(created_by = request.user)
        surveys = Survey.objects.filter(created_by=request.user)
    return render(request, 'survey/mailindex.html', {'surveys': surveys,'mailsent':mailsent})

@login_required
def index_survey(request):
    surveys = Survey.objects.filter(created_by=request.user )
    return render(request, 'survey/index.html', {'surveys': surveys})

@login_required
def add_survey(request):
    if request.method == 'POST':
        form = AddSurveyForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            messages.success(request, 'Survey added Successfully')
            return redirect('index_survey')
    else:
        form = AddSurveyForm()

    return render(request, 'survey/add_survey.html', {'form': form})


@login_required
def edit_survey(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id, created_by=request.user)

    if request.method == 'POST':
        form = AddSurveyForm(request.POST, instance=survey)

        if form.is_valid():
            survey = form.save(commit=False)
            survey.status = request.POST.get('status')
            survey.save()
            messages.success(request, 'Survey Edited Successfully')
            return redirect('index_survey')
    else:
        form = AddSurveyForm(instance=survey)

    return render(request, 'survey/edit_survey.html', {'form': form, 'survey': survey})