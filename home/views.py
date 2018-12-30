from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from conf.models import conference_form


# Create your views here.
def home_view(request):
    usercount = User.objects.all().count()
    confcount = conference_form.objects.all().count()

    return render(request, 'home.html', {'usercount': usercount, 'confcount': confcount, })
