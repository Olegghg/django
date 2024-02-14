from django.contrib import admin
from .models import Categories, Budget, Expenses, User

admin.site.register(Categories)
admin.site.register(Budget)
admin.site.register(Expenses)
admin.site.register(User)
# Register your models here.
