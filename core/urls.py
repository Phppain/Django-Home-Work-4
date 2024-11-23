from django.contrib import admin
from django.urls import path
from app.views import home, about, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('contacts/', contacts)
]
