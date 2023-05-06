from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Booking, Menu
from .serializers import MenuSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here. 
def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]
    
