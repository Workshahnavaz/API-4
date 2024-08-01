from django.contrib import admin
from django.urls import path,include
from.views import *


urlpatterns = [
    path('',Get),
    path('Post/',post),
    path('Put/<id>/',put),
    path('Patch/<id>/',patch),
]
