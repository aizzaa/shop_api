from rest_framework.urls import path
from .views import RegisterView, ActivationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
# "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5OTI5NTA4MywiaWF0IjoxNjk4NjkwMjgzLCJqdGkiOiIyMWNlYmNlMzhjZjk0OTEyYjM1MmZlNmVkNzRlYWI4MyIsInVzZXJfaWQiOjEzfQ.lRA4NZE3HtPYAdRCUhMw-g5GbkcJ17-MSzbwAg3Havc"````````````````````````