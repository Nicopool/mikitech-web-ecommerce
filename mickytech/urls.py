"""URLs principales de MIKITECH-APP"""

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('productos/', include('products.urls')),
    path('cuenta/', include('users.urls')),
    path('interacciones/', include('interactions.urls')),
    path('admin-panel/', include('core.admin_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
