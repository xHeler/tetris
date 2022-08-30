from rest_framework import generics, permissions

from ..models import Score
from .serializers import ScoreSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
