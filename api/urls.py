from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

# DRF のデフォルトルーター
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)  # /api/projects/ でアクセス可能

urlpatterns = [
    path('', include(router.urls)),  # ルーターが管理するエンドポイント (projects)
    path('blackjack/', include('blackjack.urls')),  # /api/blackjack/ に blackjack.urls を適用
]
