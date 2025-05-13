

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer

# Company ViewSet
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# Manual Filtering
    @action(detail=False, methods=['get'], url_path='search')
    def search_companies(self, request):
        query = request.query_params.get('q')
        if query:
            results = Company.objects.filter(location__icontains=query)
            serializer = CompanySerializer(results, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Please provide a query using ?q="}, status=status.HTTP_400_BAD_REQUEST)
    
    
# Generic Filtering 
# filter_backends = [DjangoFilterBackend]
# filterset_fields = ['name', 'location']    


# Ordering Filtering
# from rest_framework.filters import OrderingFilter


# Custom Filter Set
#?min_employees=50
# ?max_employees=200


    

# Employee ViewSet (moved outside)
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
