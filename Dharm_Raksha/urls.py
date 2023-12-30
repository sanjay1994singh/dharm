from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
          path('admin/', admin.site.urls),
          path('', include('homepage.urls')),
          path('account/', include('account.urls')),
          path('services/', include('services.urls')),
          path('karykram/', include('karykram.urls')),
          path('sangthan_suchi/', include('sangthan_suchi.urls')),
          path('matra_shakti/', include('matra_shakti.urls')),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
