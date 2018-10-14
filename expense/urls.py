from django.conf.urls import url
#from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.expense_home, name='expense_home'),
    url(r'^input/$', views.expense_input, name='expense_input'),
    #url(r'^access_deny/$', TemplateView.as_view(template_name='contents_access_deny.html'), name='access_deny'),
]