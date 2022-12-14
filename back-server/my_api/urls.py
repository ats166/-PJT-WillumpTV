from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('api/v2/', include('movies.urls')),
]

# 127.0.0.1:8000/media/articles/images/

urlpatterns += \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)