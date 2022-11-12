from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter
from .views import CustomUserView

from djoser import views

router = DefaultRouter()
router.register("users", CustomUserView)

User = get_user_model()

urlpatterns = router.urls
