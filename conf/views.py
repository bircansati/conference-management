from django.shortcuts import *
from .models import conference_form
from .forms import *
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from .models import conference_form
from django.contrib.auth.models import User


# Create your views here.
def conf_index(request):
    confs = conference_form.objects.all()
    usercount = User.objects.all().count()
    confcount = conference_form.objects.all().count()

    return render(request, 'home.html', {'usercount': usercount, 'confcount': confcount,'confs':confs, })


@login_required
def conf_create(request):
    form = confForm(request.POST or None)
    if form.is_valid():
        conf = form.save()
        conf.conference_author = request.user
        conf.save()
        return HttpResponseRedirect(conf.get_absolute_url())

    return render(request, 'conf/form.html', {'form': form})


def conf_detail(request, id):
    conf = get_object_or_404(conference_form, id=id)
    context = {
        'conf': conf,
    }
    return render(request, 'conf/detail.html', context)


def smartcfp_view(request):
    confs = conference_form.objects.all()
    return render(request, 'conf/index.html', {'confs': confs})


def myconference_view(request):
    confs = conference_form.objects.all().filter(conference_author=request.user)
    return render(request, 'conf/myconferences.html', {'confs': confs})
