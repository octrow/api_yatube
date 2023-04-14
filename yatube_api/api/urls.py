from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"groups", GroupViewSet, basename=r"groups")
router.register(r"posts/(?P<post_id>\d+)/comments", CommentViewSet,
                basename='comments')

urlpatterns = [path('v1/api-token-auth/', views.obtain_auth_token),
               path('v1/', include(router.urls))]
