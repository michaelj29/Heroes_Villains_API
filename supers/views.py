from rest_framework.decorators import api_view
from rest_framework.response import Response

from supers.serializers import SuperSerializer
from .models import Super
# Create your views here.

@api_view(['GET'])
def super_list(request):
    supers = Super.objects.all()
    serializer = SuperSerializer(supers, many=True)
    return Response(serializer.data)
