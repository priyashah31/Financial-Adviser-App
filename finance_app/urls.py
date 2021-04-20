"""finance_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from person import views
from person.views import home, signup, dailyneed_list, monthlyneed_list, want_list, money_settings, saving, budget, index, ticket_class_view, send_email, sms, GeneratePdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('login/',include('django.contrib.auth.urls')),
    path('signup/',signup, name='signup'),
    path('dailyneed_list/',dailyneed_list, name='dailyneed_list'),
    path('monthlyneed_list',monthlyneed_list, name='monthlyneed_list'),
    path('dailywant/',want_list, name='dailywant'),
    path('settings/',money_settings, name="settings"),
    path('saving/',saving, name="saving"),
    path('budget/',budget, name="budget"),
    path('todo/',index, name='index'),
    path('graph/', ticket_class_view,name="graph"),
    path('sendmail',send_email),
    path('sms/',sms),
    path('pdf/',GeneratePdf.as_view()),
    path('accounts/',include('django.contrib.auth.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
