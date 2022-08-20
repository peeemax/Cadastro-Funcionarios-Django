from django.contrib import admin, auth
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('funcionarios/', include('funcionario.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
