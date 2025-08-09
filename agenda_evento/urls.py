from django.contrib import admin
from django.urls import path
from agenda_evento.base.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', home)
]
