
from django.contrib import admin
from django.urls import path
from tb.views import register, user_login, home, user_logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('', home, name='home'),
    path('logout/', user_logout, name='logout'),
]
