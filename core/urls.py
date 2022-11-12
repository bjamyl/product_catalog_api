
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("products.api.urls"), name='products'),
    path('auth/', include('djoser.urls')),
    path('auth/', include("djoser.urls.jwt")),
]
