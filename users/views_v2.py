from django.conf import settings
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserRegisterSerializer, UserSerializer
from users.tasks import send_verification_code_by_email, send_verification_code_by_sms


class UserView(APIView):
    
    def get(self, request, email):
        queryset = User.objects.all()
        obj = get_object_or_404(queryset, email=email)
        serializer = UserSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(data)
            if user:
                if settings.ENVIRONMENT=="PROD":
                    send_verification_code_by_email.delay(user.email)
                    send_verification_code_by_sms.delay(user.phone)
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
