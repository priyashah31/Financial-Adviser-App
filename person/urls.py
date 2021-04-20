from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, signup, dailyneed_list, monthlyneed_list, want_list, money_settings, saving, budget, index, ticket_class_view, send_email, sms, GeneratePdf

app_name = 'person'

urlpatterns = [
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
    path('pdf/',GeneratePdf.as_view())



]
