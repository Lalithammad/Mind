from django.urls import path,include
from App import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Doc API",
      default_version='v1',
      description="Employee details",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hammadlalit8@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('Employee',views.EmployeeViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name="token"),
    path('refreshtoken/',TokenRefreshView.as_view(),name="refresh"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]