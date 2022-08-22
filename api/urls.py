from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views


from .views import FuncionarioViewSet

router = routers.DefaultRouter()
router.register('funcionarios', FuncionarioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', views.obtain_auth_token)
]

