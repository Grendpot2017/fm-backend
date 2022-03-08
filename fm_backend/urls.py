from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from auth import views as views_auth
from organization import views as views_orgs

router = routers.DefaultRouter()
router.register(r'users', views_auth.UserViewSet)
router.register(r'groups', views_auth.GroupViewSet)

router1 = routers.DefaultRouter()
router1.register(r'organization', views_orgs.OrganizationViewSet)
router1.register(r'organizationessential', views_orgs.OrganizationEssentialViewSet)
router1.register(r'project', views_orgs.ProjectViewSet)
router1.register(r'tag', views_orgs.TagViewSet)
router1.register(r'link', views_orgs.LinkViewSet)
router1.register(r'contacts', views_orgs.ContactViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('orgs/', include(router1.urls)),
    path('api-auth/',  include('rest_framework.urls', namespace='rest_framework')),
]
