from rest_framework.routers import DefaultRouter
from modulo_usuario.views import *

router = DefaultRouter()

router.register(r'usuario',usuario_viewsets,basename = 'usuario')

urlpatterns = router.urls