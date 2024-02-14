from django.shortcuts import render
from rest_framework.views import APIView



class HelloAPI(APIView):
    def get(self,request):
        d={
            "xabar":"API View"
        }

