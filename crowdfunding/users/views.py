from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .models import CustomUser, Badge
from .serializers import BadgeSerializer, BadgeDetailSerializer, CustomUserSerializer, CustomUserDetailSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


# View a list of ALL user profiles on the website
class CustomUserList(ObtainAuthToken):
    permission_classes = [permissions.AllowAny,]
    queryset = CustomUser.objects.all()

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            user = serializer.data['id']
            token, created = Token.objects.get_or_create(user_id=user)
            return Response({
                'token': token.key,
                'data': serializer.data
            })
        return Response(serializer.errors)


# User Profile View
class CustomUserDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
        ]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserDetailSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(
            instance=user,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# /* --------------------------------------------------------- */
# /* --------------------------------------------------------- */

# "Creating user account view" == Register Account
# class RegisterView(APIView):
#     # serializer_class = RegisterSerializer
#     permission_classes = [permissions.AllowAny,]
#     # queryset = CustomUser.objects.all()

#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

# /* --------------------------------------------------------- */
# /* --------------------------------------------------------- */

class BadgeView(generics.ListCreateAPIView):
    serializer_class = BadgeSerializer
    queryset = Badge.objects.all()
    permission_classes = [permissions.IsAdminUser]

class BadgeDetailView(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
        ]

    def get_object(self, pk):
        try:
            return Badge.objects.get(pk=pk)
        except Badge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        badge = self.get_object(pk)
        serializer = BadgeDetailSerializer(badge)
        return Response(serializer.data)

    def put(self, request, pk):
        badge = self.get_object(pk)
        data = request.data
        serializer = BadgeDetailSerializer(
            instance=badge,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        badge = self.get_object(pk)
        badge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)