from django.contrib import admin
from django.urls import path,include
from mskololagi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mskololagi.urls')),
]
