from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse

# Create your views here.
def topic_creation(request):
    if request.method == 'POST':
        t_name = request.POST['tn']
        tobj = Topic.objects.get_or_create(topic_name = t_name)[0]
        tobj.save()
        return HttpResponse('Data has been inserted')
    return render(request, 'topic_creation.html')

def webpage_creation(request):
    wl = Topic.objects.all()
    d = {'wl':wl}
    if request.method == 'POST':
        t_name = request.POST['wdata']
        nam    = request.POST['na']
        urll   = request.POST['ur']
        tobj = Topic.objects.get(topic_name = t_name)
        wobj = Webpage.objects.get_or_create(topic_name = tobj, name = nam, url = urll)[0]
        wobj.save()
        return HttpResponse('Data has been inserted')
    return render(request, 'webpage_creation.html', d)

def data_retrive(request):
    rl = Topic.objects.all()
    d = {'rl' : rl}
    if request.method == 'POST':
        t_name = request.POST.getlist('rdata')
        temp = Topic.objects.none()
        for i in t_name:
            temp = temp | Webpage.objects.filter(topic_name = i)
        print(t_name)
        print(temp)
        d1 = {'temp' : temp}
        return render(request, 'display.html', d1)
    else:
        return render(request, 'data_retrive.html', d)

def checkbox(request):
    cl = Topic.objects.all()
    d = {'cl' : cl}
    return render(request, 'checkbox.html', d)

