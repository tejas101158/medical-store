from django.contrib import admin
from django.urls import path, include

# ✅ ADD THESE 2 LINES
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

# ✅ ADD THIS (IMPORTANT for images)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)