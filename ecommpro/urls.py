from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('user/',include('userauths.urls')),
    path('api/', include('Support.urls')),
    path('admin/', include('custom_admin.urls')),
    
    # -------- third party urls -------------#
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
