from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Offre
from .OffreSerializer import OffreSerializer

@api_view(['GET'])
def get_all_offres(request):
    offres = Offre.objects.all()
    serializer = OffreSerializer(offres, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_offre(request):
    serializer = OffreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def offre_detail(request, pk):
    try:
        offre = Offre.objects.get(pk=pk)
    except Offre.DoesNotExist:
        return Response({'error': 'Offre not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OffreSerializer(offre)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OffreSerializer(offre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        offre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
