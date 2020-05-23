from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
