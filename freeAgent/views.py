from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Project, Member, Review
from django.views import generic
from django.views.generic import View
from .form import UserForm


##Not sure about the use of DetailView Vs ListView. 
##Documentation says DetailView is for when we want to add specifics to the table.
class accepted_projects(generic.ListView):
    template_name='templates/accepted_projects.html'
    model=Project
    
class all_projects(generic.ListView):
    template_name='templates/all_projects.html'
    model=Project
    
class create_project(generic.ListView):
    template_name='templates/create_project.html'   
    model=Project
    
class end_client_projects(generic.ListView):
    template_name='templates/end_client_projects.html'
    model=Project
    
class login(generic.ListView):
    template_name='templates/login.html'
    model=Member
    

class RegisterForm(View):
    form_class = UserForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            # user = Member.objects.create() same method below
            user = form.save(commit=False)
            # set the password as hash
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            #return HttpResponseRedirect('/')  # redirect to next page

            # send_activate email : send_email()
