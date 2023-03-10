from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song

@api_view(['GET'])
def songs_list(request):
    songs = Song.objects.all()
    
    serializer = SongSerializer(songs, many=True)

    return Response(serializer.data)