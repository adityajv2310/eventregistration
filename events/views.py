from django.shortcuts import render
from .models import participant

# Create your views here.
def home(request):
    context = {}
    return render(request, 'events/home.html', context)

def register(request):
    context = {}
    if request.method == 'POST':
       p1 = participant()
       p1.username = request.POST.get('username', '-')
       p1.email = request.POST.get('email', '-')
       p1.phone = request.POST.get('phone', '000')
       p1.institution = request.POST.get('institution', '-')

       if len(participant.objects.all()) >= 5:
           return render(request,'events/failed.html', context)
       else:
            p1.save()
            return render(request,'events/success.html', context)

    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['institution'] = ''
    return render(request, 'events/register.html', context)

def listofparticipants(request):
    context = {}

    context['participant'] = participant.objects.all()
    return render(request, 'events/listofparticipants.html', context)