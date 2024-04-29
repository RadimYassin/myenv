from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Transport
from .serializers import TransportSerializer

@api_view(['GET'])
def get_all_transports(request):
    transports = Transport.objects.all()
    serializer = TransportSerializer(transports, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_transport(request):
    serializer = TransportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_transport_detail(request, pk):
    try:
        transport = Transport.objects.get(pk=pk)
    except Transport.DoesNotExist:
        return Response({'error': 'Transport not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TransportSerializer(transport)
    return Response(serializer.data)

@api_view(['PUT'])
def update_transport(request, pk):
    try:
        transport = Transport.objects.get(pk=pk)
    except Transport.DoesNotExist:
        return Response({'error': 'Transport not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TransportSerializer(transport, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_transport(request, pk):
    try:
        transport = Transport.objects.get(pk=pk)
    except Transport.DoesNotExist:
        return Response({'error': 'Transport not found'}, status=status.HTTP_404_NOT_FOUND)

    transport.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)