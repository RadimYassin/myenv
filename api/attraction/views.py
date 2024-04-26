from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Attraction
from .serializers import AttractionSerializer

@api_view(['GET'])
def get_all_attractions(request):
    attractions = Attraction.objects.all()
    serializer = AttractionSerializer(attractions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_attraction(request):
    serializer = AttractionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        # Additional logic if needed
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_attraction_detail(request, pk):
    try:
        attraction = Attraction.objects.get(pk=pk)
    except Attraction.DoesNotExist:
        return Response({'error': 'Attraction not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AttractionSerializer(attraction)
    return Response(serializer.data)

@api_view(['PUT'])
def update_attraction(request, pk):
    try:
        attraction = Attraction.objects.get(pk=pk)
    except Attraction.DoesNotExist:
        return Response({'error': 'Attraction not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = AttractionSerializer(attraction, data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        # Additional logic if needed
        
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_attraction(request, pk):
    try:
        attraction = Attraction.objects.get(pk=pk)
    except Attraction.DoesNotExist:
        return Response({'error': 'Attraction not found'}, status=status.HTTP_404_NOT_FOUND)
    
    attraction.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
