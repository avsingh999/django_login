from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^your_name/', include('your_name.urls')),
    url(r'^auth/', include('auth_api.urls')),
]
