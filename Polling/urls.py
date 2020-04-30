
from django.contrib import admin
from django.urls import path, include
from pollsapp.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('polls/', include("pollsapp.urls")),
]
