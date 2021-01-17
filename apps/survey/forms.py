from django import forms
from .models import Survey,Mailtrack

class AddSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title','short_description']

class MailsentForm(forms.ModelForm):
    class Meta:
        model = Mailtrack
        fields = ['survey_id', 'mail_id']