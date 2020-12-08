from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'home', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'login/', views.user_login, name='login'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^logout-then-login$', auth_views.logout_then_login, name='logout_then_login'),
    url(r'dash', views.dashboard, name='dashboard'),
    url(r'^register$', views.register, name='register'),
]
