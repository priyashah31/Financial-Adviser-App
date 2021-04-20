from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator,MaxValueValidator
from datetime import datetime
from django.conf import settings
from django.utils import timezone


CAT_CHOICES = (
    ('mneed', 'Monthly Needs'),
    ('dneed', 'Daily Need'),
    ('want', 'Want'),
)
class Famdetails(models.Model):

    profile_pic = models.ImageField(upload_to='rail/static', blank=True)
    role = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Passenger(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    survived = models.BooleanField(default=False)
    age = models.FloatField(blank=0,default=0)
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=100)
# Create your models here.
class Money(models.Model):
    name = models.CharField(max_length=255, blank=True)
    savingPer = models.PositiveIntegerField(validators=[MinValueValidator(15)])
    wantPer = models.PositiveIntegerField(validators=[MaxValueValidator(85)])
    needPer = models.PositiveIntegerField(validators=[MaxValueValidator(85)])

    def form_valid(self):
        totalPer = int(self.savingPer + self.wantPer + self.needPer)
        if (totalPer!=100):
            return HttpResponse("Wrong input")
        else:
            return True

    def __str__(self):
        return self.name

class Budget(models.Model):
    #salary = models.ForeignKey('Famdetails', on_delete=models.CASCADE,default=0)
    itemname = models.CharField(max_length=255, blank=True)
    publish = models.DateTimeField(auto_now=True)
    amount = models.IntegerField(default =0)
    category = models.CharField(choices=CAT_CHOICES, max_length=255)

    def __str__(self):
        return self.itemname

class Category(models.Model): # The Category table name that inherits models.Model
    name = models.CharField(max_length=100) #Like a varchar
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name

class TodoList(models.Model): #Todolist able name that inherits models.Model
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    class Meta:
        ordering = ["-created"] #ordering by the created field
    def __str__(self):
        return self.title

class Famdetails(models.Model):
    profile_pic = models.ImageField(upload_to='rail/static', blank=True)
    role = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Passenger(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    survived = models.BooleanField(default=False)
    age = models.FloatField(blank=0,default=0)
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=100)
