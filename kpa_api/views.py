from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FormData
from .serializers import FormDataSerializer

class LoginAPIView(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        password = request.data.get("password")
        if phone == "7760873976" and password == "to_share@123":
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class FormAPIView(APIView):
    def get(self, request):
        forms = FormData.objects.all()
        serializer = FormDataSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FormDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
