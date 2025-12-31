from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from activities.views import ActivityViewSet
from users.views import RegisterView

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/', include(router.urls)),
]

