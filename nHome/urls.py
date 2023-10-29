from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import homepage, post,catagory

urlpatterns = [
    path('', homepage),
    path('nHome/<slug:url>', post),
    path('catagory/<slug:url>', catagory)


]
