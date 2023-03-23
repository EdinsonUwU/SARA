from modulo_usuario.views import user_extended
from rest_framework.routers import DefaultRouter
from modulo_sara.views import *

router = DefaultRouter()

router.register(r'user_extended',user_extended,basename = 'user_extended')

urlpatterns = router.urls