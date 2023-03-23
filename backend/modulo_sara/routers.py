from rest_framework.routers import DefaultRouter
from modulo_sara.views import *

router = DefaultRouter()

# router.register(r'sara',clase,basename = 'nombre')

urlpatterns = router.urls