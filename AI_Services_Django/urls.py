from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/public/", include(("recruitment.urls_public", "public"), namespace="public")),
    path("api/internal/", include(("recruitment.urls_internal", "internal"), namespace="internal")),
]