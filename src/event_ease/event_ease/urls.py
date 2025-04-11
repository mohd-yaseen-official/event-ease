from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('web.urls', namespace='web')),

    path('events/', include('events.urls', namespace='events')),

    path('auth/', include('authentication.urls', namespace='auth')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
