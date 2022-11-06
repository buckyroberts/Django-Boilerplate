from django.conf import settings
from django.contrib import admin
from django.urls import path

# TODO: Remove tests
print(settings.DEBUG)
print(settings.SECRET_KEY)

urlpatterns = [
    path('admin/', admin.site.urls),
]
