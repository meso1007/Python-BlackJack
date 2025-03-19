from django.urls import path
from .views import StartGameView, HitView, StandView

urlpatterns = [
    path('start-game/', StartGameView.as_view(), name='start-game'),
    path('hit/<int:game_id>/', HitView.as_view(), name='hit'),
    path('stand/<int:game_id>/', StandView.as_view(), name='stand'),
]
