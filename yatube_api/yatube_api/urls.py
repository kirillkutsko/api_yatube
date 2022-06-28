from api.views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(
    r'posts/([0-9]+)/comments',
    CommentViewSet,
    basename='post_comments'
)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
