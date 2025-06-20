from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('home.urls')),
    path('auditors-applicants/', include('auditors_applicants.urls')),
    path('authentication/', include('authentication.urls')),
    path('chat/', include('chat.urls')),
    path('auditors/', include('auditors.urls')),
    path('clients/', include('clients.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  