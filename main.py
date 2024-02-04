
django - admin startproject myproject
cd myproject
python manage.py startapp myapp
INSTALLED_APPS:
python
INSTALLED_APPS = [
    ...
    'myapp',
    ...
]
myapp /templates /myapp /home.html admin.html custom.html
html
{ % load
static %}
< !DOCTYPE
html >
< html >
< head >
< title > Home < / title >
< link
rel = "stylesheet"
href = "{% static 'bootstrap.css' %}" >
< style >
/ *Ваш
пользовательский
стиль * /
< / style >
< / head >
< body >
< h1 > Добро
пожаловать! < / h1 >
< p > {{flatpage.content}} < / p >
< / body >
< / html >
python
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
def home(request):
    return render(request, 'myapp/home.html')
@staff_member_required
def admin_page(request):
    return render(request, 'myapp/admin.html')
def custom_page(request):
    return render(request, 'myapp/custom.html')
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.admin_page, name='admin'),
    path('custom/', views.custom_page, name='custom'),
]
python
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
python manage.py runserver
