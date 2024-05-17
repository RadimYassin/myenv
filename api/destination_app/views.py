from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Destination
from .DestinationSerializer import DestinationSerializer

@api_view(['GET'])
def destination_list_with_events(request):
    destinations = Destination.objects.all()
    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def create_destination(request):
    serializer = DestinationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

@api_view(['GET'])
def get_destination_detail(request, pk):
    try:
        destination = Destination.objects.get(pk=pk)
    except Destination.DoesNotExist:
        return Response({'error': 'Destination not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = DestinationSerializer(destination)
    return Response(serializer.data)

@api_view(['PUT'])
def update_destination(request, pk):
    try:
        destination = Destination.objects.get(pk=pk)
    except Destination.DoesNotExist:
        return Response({'error': 'Destination not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = DestinationSerializer(destination, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_destination(request, pk):
    try:
        destination = Destination.objects.get(pk=pk)
    except Destination.DoesNotExist:
        return Response({'error': 'Destination not found'}, status=status.HTTP_404_NOT_FOUND)

    destination.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)