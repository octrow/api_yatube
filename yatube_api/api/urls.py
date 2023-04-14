from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

routerv1 = routers.DefaultRouter()
routerv1.register(r'posts', PostViewSet, basename=r'posts')
routerv1.register(r'groups', GroupViewSet, basename=r'groups')
routerv1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                  basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(routerv1.urls)),
]
