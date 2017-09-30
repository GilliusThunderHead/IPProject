from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^accepted_projects$', views.AcceptedProjects.as_view(), name='accepted_projects'),
    url(r'^all_projects$', views.AllProjects.as_view(), name='all_projects'),
    url(r'^create_projects$', views.CreateProject.as_view(), name='create_project'),
    url(r'^end_client_projects$', views.EndClientProjects.as_view(), name='end_client_projects'),
    url(r'^$', views.Login.as_view(), name='login'),
    url(r'^register$', views.RegisterForm.as_view(), name='register'),
    url(r'^dashboard$', views.DashBoardForRedirect.as_view(), name='Redirect'),
    url(r'^logout$', views.LogOut.as_view(), name='log_out'),
    
]
