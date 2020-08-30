from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('learning/', include('learning.urls')),
    path('', RedirectView.as_view(url='learning/')),
] 
