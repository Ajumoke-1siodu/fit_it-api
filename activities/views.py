from rest_framework import viewsets, permissions, generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .models import Activity
from .serializers import ActivitySerializer, UserSerializer
from .filters import ActivityFilter
from .serializers import RegisterSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """ 
    Provides CRUD operations for Activity model: 
    - Create activity 
    - List activities 
    - Retrieve activity 
    - Update activity 
    - Delete activity 
    """
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ActivityFilter
    ordering_fields = ["date", "duration", "calories", "distance"]
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows logged-in user to:
    - View profile (GET)
    - Update profile (PUT/PATCH) 
    - Delete account (DELETE)
    """ 
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):  
        return self.request.user
<<<<<<< HEAD


class RegisterView(generics.CreateAPIView):
    """
    Allows new users to register (POST).
    """ 
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

=======
    
    # User Registration 
    class RegisterView(generics.CreateAPIView):  
        """
        Allows new users to register (POST).
        """
        queryset = User.objects.all()
        serializer_class = UserSerializer
        permission_classes = [permissions.AllowAny]
>>>>>>> 64935986a66f2144e2b20a91cb850e6657c043a9
# Create your views here.
