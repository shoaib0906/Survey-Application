from django import forms
from .models import Question,Option,Answer


class AddQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title','survey_id']

class AddOption(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option']

class AddAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_id','audience_email']