from django.conf.urls import url
from django.contrib import admin
from django.urls import path
# from todo_list import views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.home,name="home"),

]
