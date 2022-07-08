from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet


router_v1 = DefaultRouter()
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'users', UserViewSet, basename='user_list')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='post_comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
