from django.contrib import admin
from django.urls import path
from .api import api
from linkedin_url.api import app
from linkedin_api import Linkedin
from linkedin_url.models import Url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", app.urls),
]

