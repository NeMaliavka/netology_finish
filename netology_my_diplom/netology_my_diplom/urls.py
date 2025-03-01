from django.contrib import admin
from django.urls import path, include
from baton import urls as baton_urls

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для админки Django
    path('api/', include('backend_dev.urls')),  # Подключение URL-адресов из приложения backend_dev
    path('baton/', include(baton_urls)),
]
