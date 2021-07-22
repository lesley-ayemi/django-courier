from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('tracking', views.track, name='track_order'),
    path('search_order', views.search_order, name='search-order'),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)