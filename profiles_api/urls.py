from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('hello_viewset', views.HelloViewSet, basename='hello_viewset')
#Cuando se está utilizando un queryset, no es neceario registrar un basename
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLogininApiView.as_view()),
    path('', include(router.urls)),
]