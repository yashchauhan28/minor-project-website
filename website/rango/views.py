from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import UserInformation,ConnectionDetail
from rango.forms import UserInformationForm,ConnectionDetailForm
from django.views.decorators.csrf import csrf_exempt

def index(request):
    user_list = UserInformation.objects.all()
    print user_list
    context_dict = {'users' : user_list}
    return render(request, 'rango/index.html', context_dict)

@csrf_exempt
def startsession(request,sessionid):
    context_dict={'id' : sessionid , 'name':''}
    #print sessionid
    if request.method == 'POST':
        name = request.POST.get('name',)
        print "name is :" + name
        context_dict['name']=name
        print context_dict
        return render(request,'rango/session.html',context_dict)
    return render(request,'rango/session.html',context_dict)

def about(request):
    return HttpResponse("This is about page!!")

def add_user(request):
    form = UserInformationForm()

    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            form.save(commit='True')
            return index(request)
        else:
            print form.errors

    return render(request,'rango/add_user.html',{'form' : form})
