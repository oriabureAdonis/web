from django.http import JsonResponse
from .models import drink
from .serializers import drinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request, format=None):

  if request.method == 'GET':
     drink = drink.objects.all()
     serializer = drinkSerializer(drink, many=True)
     return JsonResponse({'drink':serializer.data})
 
  if request.method == 'POST':
      serializer = drinkSerializer(data=request.data)
      if serializer.is_valid():
       serializer = drinkSerializer(drink, many=True)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    try:
        drink = drink.objects.get(pk=id)
    except drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = drinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = drinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
