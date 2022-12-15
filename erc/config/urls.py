from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularAPIView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("esn.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r"^__debug__/", include("debug_toolbar.urls")),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
