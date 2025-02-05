from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для админки Django
    path('api/', include('backend_dev.urls')),  # Подключение URL-адресов из приложения backend_dev
]
