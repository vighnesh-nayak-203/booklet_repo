from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import BookletForm,Register
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required
from .models import Booklet
# Create your views here.

@login_required
def index(request):
    print(request.user.is_superuser)
    booklets={'booklets':Booklet.objects.all()}
    return render(request,'list.html',context=booklets)

def register(request):
    if request.method=='POST':
        form=Register(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return HttpResponseRedirect('/login')
    else:
        form=Register()
    return render(request,'register.html',{'forms':form})


@staff_member_required
def addBooklet(request):
    b=Booklet.objects.all() 
    if request.method == 'POST':
        form = BookletForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BookletForm()

    return render(request, "add.html", {
        "form": form
    })