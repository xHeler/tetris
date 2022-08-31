from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("accounts/", include('accounts.urls')),
    path('', include('scoreboard.urls')),
    path("api/v1/", include("scoreboard.api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
