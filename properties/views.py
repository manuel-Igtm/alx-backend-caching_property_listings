from django.http import JsonResponse
from .utils import get_all_properties

def property_list(request):
    properties = get_all_properties()
    data = [
        {
            "id": prop.id,
            "title": prop.title,
            "description": prop.description,
            "price": str(prop.price),   # convert Decimal to string for JSON
            "location": prop.location,
            "created_at": prop.created_at.isoformat(),
        }
        for prop in properties
    ]
    return JsonResponse({"data": data})
