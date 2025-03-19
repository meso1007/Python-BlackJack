from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GameSession
from .serializers import GameSessionSerializer

class StartGameView(APIView):
    """Start a new game session."""
    def post(self, request):
        game = GameSession.objects.create()
        game.start_game()
        game.save()
        return Response(GameSessionSerializer(game).data, status=status.HTTP_201_CREATED)

class HitView(APIView):
    """Player takes a hit (draws a card)."""
    def post(self, request, game_id):
        try:
            game = GameSession.objects.get(id=game_id)
        except GameSession.DoesNotExist:
            return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)

        if game.game_over:
            return Response({"error": "Game is over"}, status=status.HTTP_400_BAD_REQUEST)

        game.hit()
        game.save()
        return Response(GameSessionSerializer(game).data, status=status.HTTP_200_OK)

class StandView(APIView):
    """Player stands, triggering the dealer's turn."""
    def post(self, request, game_id):
        try:
            game = GameSession.objects.get(id=game_id)
        except GameSession.DoesNotExist:
            return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)

        if game.game_over:
            return Response({"error": "Game is over"}, status=status.HTTP_400_BAD_REQUEST)

        game.stand()
        game.save()
        return Response(GameSessionSerializer(game).data, status=status.HTTP_200_OK)
