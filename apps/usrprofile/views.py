from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from apps.survey.models import Survey

@login_required
def dashboard(request):
    # return HttpResponse(request.user.userprofile.is_employer)
    # if request.user.userprofile.is_employer == 'False':
    #     surveys=Survey.objects.all()
    #     return render(request, 'usrprofile/dashboard.html', {'userprofile': request.user.userprofile.is_employer})
    # else:
        surveys = Survey.objects.all().order_by('id')[:1000]
        return render(request, 'usrprofile/dashboard.html', {'userprofile': request.user.userprofile.is_employer,'surveys': surveys})