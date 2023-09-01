from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserDataView, UserRegistrationView, CustomTokenObtainPairView

app_name = 'api'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'), 
    path('user-data/', UserDataView.as_view(), name='user-data'),
     # Add this line
    # Add other URL patterns if needed
]
