from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from apps.question.models import Survey

from .forms import AddQuestion,AddOption,AddAnswer
from .models import Question,Option,Answer
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages


@login_required
def add_question(request):
    if request.method == 'POST':
        form = AddQuestion(request.POST)

        if form.is_valid():
            quest = form.save(commit=False)
            quest.created_by = request.user
            quest.save()
            for i in request.POST.getlist('option'):
                option = Option.objects.create(option=i,question=quest)
                option.save()
            messages.success(request, 'Question created successfully.')
            return redirect('index_question')
    else:
        form = AddQuestion()
        form1 = AddOption()
    return render(request, 'question/add_question.html', {'form': form,'form1': form1})

@login_required
def index_question(request):
    surveys = Survey.objects.filter(created_by=request.user )
    return render(request, 'question/index.html', {'surveys': surveys,'some_flag': True,'message':'This is test'})

@login_required
def delete_question(request, question_id):
    surveys = Question.objects.filter(created_by=request.user,id=question_id).delete()
    surveys = Survey.objects.filter(created_by=request.user)
    messages.success(request, 'Question deleted successfully.')
    return render(request, 'question/index.html', {'surveys': surveys})

@login_required
def show_questions(request,survey_id):
     questions = Question.objects.filter(survey_id=survey_id)
     return render(request, 'question/show_question.html', {'questions': questions})

@login_required
def answer_questions(request,survey_id):
    if request.method == 'POST':
        form = AddAnswer(request.POST)
        audience_email = request.POST['audience_email']
        user = request.user
        for i in request.POST.getlist('question'):
            if i :
                # answer = Answer.objects.create(question_id=i,answer_id='answer[i]')
                answer = request.POST['answer' + '[' + i + ']']
                ques = get_object_or_404(Question, id=i)
                opt = get_object_or_404(Option, id=answer)
                answer = Answer.objects.create(
                    question_id=ques,
                    answer_id=opt,
                    audience_email = audience_email,
                    created_by=user,
                )
                answer.save()
        messages.success(request, 'Question created successfully.')
        return redirect('answer_questions',survey_id=survey_id)
    else:
         form = AddAnswer()
         #Answer.objects.filter(created_by=request.user).delete()
         questions = Question.objects.filter(survey_id=survey_id)
         alreadyanswer = Answer.objects.filter(created_by=request.user,question_id=questions[0].id)
         answers = Answer.objects.filter(created_by=request.user)
         #return HttpResponse(answers)
         return render(request, 'question/answer_question.html',
                       {'questions': questions,'form':form,'answers':answers,'alreadyanswer':alreadyanswer})


@login_required
def edit_question(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    #return HttpResponse(question)
    if request.method == 'POST':
        form = AddQuestion(request.POST, instance=question)

        if form.is_valid():
            quest = form.save(commit=False)
            quest.created_by = request.user
            quest.save()
            Option.objects.filter(question=question_id).delete()
            for i in request.POST.getlist('option'):
                if i != "":
                    option = Option.objects.create(option=i,question=quest)
                    option.save()
            messages.success(request, 'Question Edited successfully.')
            return redirect('index_question')
    else:
        questions = Question.objects.get(id=question_id)
        #return HttpResponse(questions.survey_id);
        option = Option.objects.filter(question=question_id)[:1000]
        return render(request, 'question/edit.html', {'questions': question,'option':option})

# def edit_survey(request, survey_id):
#     survey = get_object_or_404(Survey, pk=survey_id, created_by=request.user)
#
#     if request.method == 'POST':
#         form = AddSurveyForm(request.POST, instance=survey)
#
#         if form.is_valid():
#             survey = form.save(commit=False)
#             survey.status = request.POST.get('status')
#             survey.save()
#
#             return redirect('dashboard')
#     else:
#         form = AddSurveyForm(instance=survey)
#
#     return render(request, 'survey/edit_survey.html', {'form': form, 'survey': survey})

@login_required
def option_view(request,question_id):
    option = Option.objects.filter(question=question_id)[:1000]
    return render(request,'question/optiondetail.html', {'option': option})
