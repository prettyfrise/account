from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.loan_main, name='loan_main')
]