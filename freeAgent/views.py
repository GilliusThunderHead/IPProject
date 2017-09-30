from django.http import HttpResponse,HttpResponseForbidden
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Project, Member, Review
from django.views import generic
from django.views.generic import View
from .form import UserForm, LoginForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Not sure about the use of DetailView Vs ListView.
# Documentation says DetailView is for when we want to add specifics to the table.

class AcceptedProjects(generic.ListView):
    template_name = 'accepted_projects.html'
    model = Project

    #  @login_required()
    def a_method_for_eliminate_the_error_remind(self):  # this is an example built for login_required
        pass


class AllProjects(generic.ListView):
    template_name = 'all_projects.html'
    model = Project
    

class CreateProject(generic.ListView):
    template_name = 'create_project.html'
    model = Project
    

class EndClientProjects(generic.ListView):
    template_name = 'end_client_projects.html'
    model=Project
    
"""
class Login(generic.ListView):
    template_name = 'login.html'
    model = Member
"""


class RegisterForm(CreateView):
    form_class = UserForm
    template_name = 'register.html'

    """
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
            return HttpResponse('yes')  # redirect to next page
        else:
            return HttpResponse('error')
            # send_activate email : send_email()
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterForm, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.group.add()
        user.save()
        return HttpResponse("fine")


class Login(LoginView):
    form_class = LoginForm
    template_name = "login.html"
    redirect_authenticated_user = True


    """
    def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        # Return an error message.
        
    def logout_view(request):
    logout(request)
    # Redirect to a success page.
    """


class DashBoardForRedirect(TemplateView):
    template_name = 'dashboard.html'


class LogOut(LogoutView):
    template_name = 'logout.html'
    next_page = 'login'
