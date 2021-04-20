from django.contrib import admin
from .models import Money, Budget, Famdetails, Passenger, TodoList

# Register your models here.
admin.site.register(Money)
admin.site.register(Budget)
admin.site.register(Passenger)
admin.site.register(Famdetails)
admin.site.register(TodoList)
