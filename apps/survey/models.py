from django.contrib.auth.models import User
from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=2555)
    short_description= models.TextField(blank=True,null=True)

    created_by = models.ForeignKey(User,related_name='surveys',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Mailtrack(models.Model):
    mail_id = models.CharField(max_length=2555)
    survey_id = models.ForeignKey(Survey,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='mailtracks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mail_id