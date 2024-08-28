from django.urls import path,include
from rest_framework import routers
from organization.views import *

app_name = "organization"

user_router = routers.SimpleRouter()
user_router.register('usersignup',UserSignUpViewSet, basename = 'user')

usersigin_router = routers.SimpleRouter()
usersigin_router.register('usersignin', UserSignInViewSet, basename = 'usersignin')

urlpatterns = [
    path('',include(user_router.urls)),
    path('',include(usersigin_router.urls))
]
