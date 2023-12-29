from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import *
from .serializers import *

class SuvlarAPI(APIView):
    def get(self, request):
        suvlar=Suv.objects.all()
        serializer=SuvModelSerializer(suvlar,many=True)

        return Response(serializer.data)

class SuvAPI(APIView):

    def get(self, request, son):
        suv=Suv.objects.get(id=son)

        serializer=SuvModelSerializer(suv,many=False)

        return Response(serializer.data)

    def update(self, request, son):
        suv = Suv.objects.get(id=son)
        serializer = SuvModelSerializer(suv, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            Suv.objects.filter(id=son).update(
                brend=data.get("brend"),
                narx=data.get("narx"),
                litr=data.get("litr"),
                batafsil=data.get("batafsil"),
            )
            return Response(serializer.data)
        return Response(serializer.errors)



class MijozlarAPI(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozModelSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['ism','tel']

    def get_queryset(self):
        mijozlar=self.queryset

        return mijozlar




class MijozAPI(APIView):
    def get(self,request,son):
        mijoz=Mijoz.objects.get(id=son)

        serializer=MijozModelSerializer(mijoz, many=False)
        return Response(serializer.data)

    def update(self, request, son):
        mijoz = Mijoz.objects.get(id=son)
        serializer = MijozModelSerializer(mijoz, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            Mijoz.objects.filter(id=son).update(
                ism=data.get("ism"),
                tel=data.get("tel"),
                manzil=data.get("manzil"),
                qarz=data.get("qarz"),
                user=request.user
            )
            return Response(serializer.data)
        return Response(serializer.errors)

class HaydovchilarModelViewSet(ModelViewSet):
    queryset =Haydovchi.objects.all()
    serializer_class =HaydovchiModelSerializer

    def get_queryset(self):
        haydovchilar=self.queryset

        return haydovchilar


class BuyurtmalarModelViewSet(viewsets.ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaModelSerializer

    def get_queryset(self):
        buyurtma=self.queryset

        return buyurtma


class AdminlarModelViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminModelSerializer

    def get_queryset(self):
        adminlar=self.queryset

        return adminlar

class AdminAPI(APIView):
    def get(self,request,son):
        admin=Admin.objects.get(id=son)

        serializer=MijozModelSerializer(admin, many=False)
        return Response(serializer.data)
