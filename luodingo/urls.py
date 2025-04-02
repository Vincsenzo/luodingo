from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learn/', include('learn.urls')),
    path('create/', include('create.urls')),

     path('', RedirectView.as_view(url='/learn/', permanent=True)),
]
