"""URLs principales de MIKITECH-APP"""

from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', include('core.urls')),
    path('productos/', include('products.urls')),
    path('cuenta/', include('users.urls')),
    path('interacciones/', include('interactions.urls')),
    path('admin-panel/', include('core.admin_urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

