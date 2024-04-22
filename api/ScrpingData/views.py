from rest_framework.decorators import api_view
from rest_framework.response import Response
from hotel_app.models import Hotel, HotelImage
import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from django.core.files import File
import os

@api_view(['GET'])
def get_hotels(request):
    url = "https://www.booking.com/city/ma/marrakech.html?aid=1610684;label=ma-marrakech-er6V1qm_TuU7x0s2QgA8jgS553287990362:pl:ta:p1:p2:ac:ap:neg:fi:tikwd-31153056048:lp1009979:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0;ws=&gad_source=1&gclid=CjwKCAjwz42xBhB9EiwA48pT75GkqiJmEXapaRDJOi_y53ay3-QoAmY_mH3GHGOUrItBXexCPuoCbxoC7c8QAvD_BwE"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for div in soup.find_all("div", {"class": "c82435a4b8"}):
        name_element = div.find("a", {"class": "decf596023"})
        description = div.find("p", {"class": "a53cbfa6de a2b6889344"})
        location_element = div.find("span", {"class": "b6c5ff40a7"})
        rating_element = div.find("div", {"class": "a3b8729ab1 d86cee9b25"})
        pricing_element = div.find("span", {"class": "d746e3a28e"})
        thumbnail_element = div.find("img", {"class": "e3fa9175ee"})

        # Check if elements are found before accessing attributes
        name = name_element.text.strip() if name_element else None
        description_text = description.text.strip() if description else None
        location = location_element.text.strip() if location_element else "m"  # Set default value to "m" if None
        rating = rating_element.text.strip() if rating_element else None
        pricing = pricing_element.text.strip() if pricing_element else None
        image_url = thumbnail_element["src"] if thumbnail_element else None

        if None not in [name, description_text, rating, pricing, image_url]:
            # Extracting the numeric part from the rating string
            rating_numeric = float(rating[10:])
            # Removing the dollar sign and formatting the pricing
            pricing_numeric = float(pricing.replace('$', ''))

            # Check if the hotel already exists
            hotel, created = Hotel.objects.get_or_create(
                name=name,
                location=location,
                description=description_text,
                rating=rating_numeric,
                pricing=pricing_numeric,
                destination_id=1  # Replace 1 with the actual destination ID
            )

            # Check if the hotel image already exists
            if not HotelImage.objects.filter(hotel=hotel, image_url=image_url).exists():
                # Download the image
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    # Create a unique image file name
                    image_name = os.path.basename(image_url)
                    # Save the image to a temporary file
                    temp_image = ContentFile(image_response.content)
                    # Create and save HotelImage instance
                    hotel_image = HotelImage.objects.create(
                        hotel=hotel,
                        image=File(temp_image),
                        image_url=image_url
                    )

    return Response("Hotels data inserted successfully.")
