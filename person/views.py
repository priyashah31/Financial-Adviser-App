from django.shortcuts import render
from .models import Money, Budget, Famdetails, Passenger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import MoneyForm, BudgetForm, StudentForm
from django.db.models import Avg,Sum,F, Count, Q
from django.shortcuts import render,redirect
from .models import Money, Budget, TodoList, Category
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import MoneyForm, BudgetForm
from django.shortcuts import render, get_object_or_404, redirect
from person.models import Famdetails,Passenger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import StudentForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import json
from django.core.mail import BadHeaderError, send_mail,EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
import urllib.request
import urllib.parse
from twilio.rest import TwilioRestClient
import time,datetime
from django.shortcuts import render
from twilio.rest import Client
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf


# Create your views here.
def budget(request):
    percent = Money.objects.all()
    for s in percent:
        wan=s.wantPer
        nee=s.needPer
        sav=s.savingPer
    saving = Budget.objects.all()
    total = 0
    for s in saving:
        total+=s.amount
    #income = Famdetails.objects.only('salary')
    save = Money.objects.all()
    for s in save:
        per=s.savingPer
    save = 50000-total
    saverate = save/50000*10
    if(saverate<sav):
        bud = Budget.objects.all()
        form = BudgetForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/person/monthly')

        #adderw = Budget.objects.all().filter(category='want').aggregate(Sum('amount'))
        context = {
            "bud": bud,
            #"budwant": budwant,
            "form":form,
            "save":save,
            #"adderw":adderw,
        }
        return render(request, 'person/budget.html', context)
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/person/daily/#chat')

def extra(request):
    return render(request, '')


def saving(request):
    saving = Budget.objects.all()
    total = 0
    for s in saving:
        total+=s.amount
    #income = Famdetails.objects.only('salary')
    save = Money.objects.all()
    for s in save:
        per=s.savingPer
    save = 50000-total
    saverate = save/50000*10
    if(saverate<=per):
        money = "less"
        return render(request,"registration/graph.html", context ={
        "save":save,
        "money":money,
        })
    else:
        money = "more"
        return render(request,"registration/graph.html", context ={
        "save":save,
        "money":money,
        })


def dailyneed_list(request):
    budneed = Budget.objects.all().filter(category='dneed')
    # page = request.GET.get.
    # print(buds.category)

    form = BudgetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/person/daily')

    adderd = Budget.objects.all().filter(category='dneed').aggregate(Sum('amount'))
    context = {
        "budneed":budneed,
        "form":form,
        "adderd":adderd,
        #"adder":adder,
    }
    return render(request, 'person/daily.html', context)

def monthlyneed_list(request):
    monthneed = Budget.objects.all().filter(category='mneed')
    # page = request.GET.get.
    #budwant = Budget.objects.all().filter(category='mneed')
    # print(buds.category)
    #c =Budget.objects.all().filter(category='mneed')
    form = BudgetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/monthlyneed_list')

    adder = Budget.objects.all().filter(category='mneed').aggregate(Sum('amount'))
    context = {
        "monthneed":monthneed,
        #"budwant": budwant,
        "form":form,
        "adder":adder,
    }
    return render(request, 'person/monthly.html', context)

def want_list(request):
    budwant = Budget.objects.all().filter(category='want')
    # page = request.GET.get.
    #budwant = Budget.objects.all().filter(category='mneed')
    # print(buds.category)
    #c =Budget.objects.all().filter(category='mneed')
    form = BudgetForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/person/monthly')

    adderw = Budget.objects.all().filter(category='want').aggregate(Sum('amount'))
    context = {
        "budwant": budwant,
        #"budwant": budwant,
        "form":form,
        "adderw":adderw,
    }
    return render(request, 'person/dailywant.html', context)

def money_settings(request):
    set = Money.objects.all()
    form = MoneyForm(request.POST or None)
    if form.is_valid():
    #    if form.form_valid():
        instance = form.save(commit=False)
        #    instance.user = user
        instance.save()
        return HttpResponse("Saved!")
    context = {
            "form":form,
            "setting":set,
    }
    return render(request, "person/daily.html", context)

def index(request): #the index view
    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo
            return redirect("/") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
    return render(request, "registration/todo.html", {"todos": todos, "categories":categories})

class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        #getting the template
        pdf = render_to_pdf('person/budget.html')
        return HttpResponse(pdf, content_type='application/pdf')


def home(request):

    return render(request, 'person/index.html', {

        })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/person/sendmail')
    else:
        form = UserCreationForm()
    return render(request,"registration/signup.html", {
        'form': form
        } )

def famdetails(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/home')
    else:
        form = StudentForm()
    return render(request,"registration/fam.html", {
        'form': form
        } )

def ticket_class_view(request):
    p = Passenger(name='Apress', sex='Male', survived=True , age=12, ticket_class='2',embarked='Mumbai')
    p.save()
    r = Passenger(name='press', sex='Male', survived=True , age=12, ticket_class='1',embarked='Mumbai')
    r.save()
    q = Passenger(name='Apress', sex='Male', survived=True , age=12, ticket_class='2',embarked='Mumbai')
    q.save()
    s = Passenger(name='Apress', sex='Male', survived=False , age=12, ticket_class='2',embarked='Mumbai')
    s.save()

    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')
    return render(request, 'registration/graph.html', {'dataset': dataset})

def send_email(request):
    if 'Your Daily Expenses Update Pending' and 'Find your Pass Attatched below' and 'cshsrailway@gmail.com':
        try:
#           send_mail('Railway Pass', 'Find your Pass Attatched below', 'cshsrailway@gmail.com', ['harshil4000@gmail.com'])
            mail = EmailMessage('Your Daily Expenses Update Pending', 'Dear User,please update your daily expenses on your Emager account at the below mentioned link and never miss another update from the best expense manager in town.http://127.0.0.1:8000/admin/', 'cshsrailway@gmail.com', ['swapnilkadakia@gmail.com'])
            mail.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('http://127.0.0.1:8000/person/sms/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
def expiry(request):
        send_mail('Pass Verified', 'Dear User,Your pass has been verified. You may pay at the this link : https://www.payumoney.com/paybypayumoney/#/562BE65F1F907C7319F95A3213D694BE. Best Wishes','cshsrailway@gmail.com',['harshil4000@gmail.com'])

def sms(request):
    try:
        client = Client('AC5ed807250e50cdc8e91aa1edcfa7f364', '621e87dfa7bec7fd9e5a0874e32a4ba5')
        message = client.messages.create(to='+917506402445', from_='+12052240034', body='This is to inform you that your concession form has been rejected due to non-verfification of your details.Contact +914045967100 or your college desk for further details ')
        print(message.sid)
    except BadHeaderError:
        return HttpResponseRedirect('http://127.0.0.1:8000/person/settings/')
    return HttpResponseRedirect('http://127.0.0.1:8000/person/settings/')
