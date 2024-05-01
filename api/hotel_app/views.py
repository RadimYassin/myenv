from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel, HotelImage
from .HotelSerializer import HotelSerializer,HotelImageSerializer

@api_view(['GET'])
def get_all_hotels(request):
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_hotel_api_view(request):
    if request.method == 'POST':
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            # Save hotel data
            serializer.save()

            # Save images
            images_data = request.FILES.getlist('images')  # Assuming 'images' is the field name for images
            for image_data in images_data:
                # Assuming you have a separate serializer for handling images
                image_serializer = HotelImageSerializer(data={'image': image_data})
                if image_serializer.is_valid():
                    image_serializer.save(hotel_id=serializer.data['id'])  # Assuming hotel_id is the foreign key to Hotel
                else:
                    # Handle invalid image serializer
                    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_hotel_detail(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
    except Hotel.DoesNotExist:
        return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = HotelSerializer(hotel)
    return Response(serializer.data)

@api_view(['PUT'])
def update_hotel(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
    except Hotel.DoesNotExist:
        return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = HotelSerializer(hotel, data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        # Handle images
        images_data = request.FILES.getlist('images')
        for image_data in images_data:
            HotelImage.objects.create(hotel=serializer.instance, image=image_data)
        
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_hotel(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
    except Hotel.DoesNotExist:
        return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
    
    hotel.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
