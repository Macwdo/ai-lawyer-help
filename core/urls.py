from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

auth = [
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.urls")),
    path("api/auth/", include(auth), name="auth"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += [
        path("silk/", include("silk.urls", namespace="silk")),
    ]
