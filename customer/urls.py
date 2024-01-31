from django.urls import include, path

# from rest_framework import routers
from rest_framework_nested import routers

from customer.views import UserViewSet, ProfileViewSet, LoginView

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'^', UserViewSet, basename='user')

profile_router = routers.NestedSimpleRouter(
    router,
    r'^',
    lookup='user')
profile_router.register(
    r'profile',
    ProfileViewSet,
    basename='user-profiles'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(profile_router.urls)),
    path(r'login/', LoginView.as_view()),
]
