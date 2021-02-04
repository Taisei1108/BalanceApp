from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters

from .models import BorrowEvent
# Create your views here.

class ListBalance(APIView):
    def get(self, request):
        try:
            Borrow = BorrowEvent.objects.all()
            res_list = [
                {
                    'id': b.id,
                    'event_name': b.event_name.name,
                    'event_date': b.event_date,
                    'price': b.price,
                    'is_paid': b.is_paid,
                }
                for b in Borrow
            ]
            return Response(res_list)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)