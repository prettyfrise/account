"""accountbook URL Configuratio

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    #url(r'^reviews/', include(('reviews.urls', 'reviews'), namespace='reviews')),
    url(r'^expense/',include(('expense.urls', 'expense'), namespace='expense')),
    url(r'^loan/',include(('loan.urls', 'loan'), namespace='loan')),
    url(r'^bank/',include(('bank.urls', 'bank'), namespace='bank'))
]
