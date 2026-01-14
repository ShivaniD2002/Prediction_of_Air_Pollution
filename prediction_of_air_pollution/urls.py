from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Remote_User.urls')),
    path('service/', include('Service_Provider.urls')),
]
