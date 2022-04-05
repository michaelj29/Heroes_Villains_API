from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Super
# Create your views here.

@api_view(['GET', 'POST'])
def super_list(request):
  supers = Super.objects.all()
  if request.method == 'GET':
    serializer = SuperSerializer(supers, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = SuperSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)