from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from super_types.models import SuperTypes
from .serializers import SuperSerializer
from .models import Super
# Create your views here.

@api_view(['GET', 'POST'])
def super_list(request):
  super_type_param = request.query_params.get('type')
  supers = Super.objects.all()
  if super_type_param:
    supers = supers.filter(super_type__type=super_type_param)
    serializer = SuperSerializer(supers, many=True)
    return Response(serializer.data)
  elif request.method == 'GET':
    super_types = SuperTypes.objects.all()
    custom_response_dictionary = {}
    for supertype in super_types:
      supers = Super.objects.filter(super_type_id=supertype.id)
      super_serializer = SuperSerializer(supers, many=True)
      if supertype.id == 1:
        custom_response_dictionary['Heroes'] = super_serializer.data
      if supertype.id == 2:
           custom_response_dictionary['Villains'] = super_serializer.data
      
    return Response(custom_response_dictionary)
  elif request.method == 'POST':
    serializer = SuperSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)