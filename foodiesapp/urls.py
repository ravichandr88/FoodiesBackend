from django.urls import path,include
from rest_framework import routers
from . import views
router = routers.SimpleRouter()

router.register(r'meal', views.MealViewSet)
router.register(r'food', views.FoodViewSet)
router.register(r'bevrage', views.BEVERAGESViewSet)
router.register(r'combo', views.COMBOSViewSet)
router.register(r'slider', views.SliderViewSet)
router.register(r'gallery', views.GalleryViewSet)
router.register(r'contact', views.ConsultViewSet)
urlpatterns = router.urls