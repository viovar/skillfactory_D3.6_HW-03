from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('new/', include('django.contrib.flatpages.urls')),  # < вот тут
   path('news/', include('news.urls')),
]