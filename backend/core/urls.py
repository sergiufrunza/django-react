
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from decouple import config

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.auth.urls')),
    path('api/v1/', include('apps.user.urls')),
    path('api/v1/', include('apps.blog.urls')),
]



if config('DEBUG', cast=bool):
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls'))
    ] + urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
