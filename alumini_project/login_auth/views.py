from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


User = get_user_model()

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        # Get or create a token for the user
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "message": "Login successful",
            "token": token.key
        }, status=status.HTTP_200_OK)
        

# class ProtectedView(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({"message": "You have access to this protected resource!"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])  
def logout_view(request):
    try:
        request.user.auth_token.delete() 
        return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
    except AttributeError:
        return Response({"error": "User is not authenticated"}, status=status.HTTP_400_BAD_REQUEST)    


# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from .serializers import RegisterSerializer

# @api_view(['POST'])
# def register_user(request):
#     serializer = RegisterSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
