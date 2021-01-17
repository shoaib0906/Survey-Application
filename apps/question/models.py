from django.contrib.auth.models import User
from apps.survey.models import Survey
from django.db import models

class Question(models.Model):
    survey_id = models.ForeignKey(Survey,related_name='questions',on_delete=models.CASCADE)
    title = models.CharField(max_length=2555)
    created_by = models.ForeignKey(User,related_name='questions',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=2555,blank=False)

    def __str__(self):
        return self.option

class Answer(models.Model):
    #survey_id = models.ForeignKey(Survey,on_delete=models.CASCADE,blank=False)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE,blank=False)
    answer_id = models.ForeignKey(Option, on_delete=models.CASCADE,blank=False)
    audience_email = models.CharField(max_length=2555,blank=False)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.audience_email

    class Meta:
        unique_together = ('question_id', 'answer_id','created_by')