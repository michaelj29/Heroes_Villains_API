from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import SuperTypes
from .serializers import SuperTypesSerializer


@api_view(['GET', 'POST'])
def super_types_list(request):
  super_types = SuperTypes.objects.all()
  if request.method == 'GET':
    serializer = SuperTypesSerializer(super_types, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = SuperTypesSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def super_types_detail(request, fk):
    super_types = get_object_or_404(SuperTypes, fk=fk)
    if request.method == 'GET':
        serializer = SuperTypesSerializer(super_types)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperTypesSerializer(super_types, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super_types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)