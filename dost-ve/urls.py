from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path("serveradminpanel/", admin.site.urls),
    # External Routes
    path("", include("apps.main.urls")),
]

handler404 = "apps.main.views.handler404"
