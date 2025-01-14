from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings  
from django.conf.urls.static import static  

schema_view = get_schema_view(
 openapi.Info(
     title="Devil-Data Documentation",
     default_version='v1',
     description="Api com CRUD básico sobre o universo de ChainsawMan"
 ),
 public=True,
 permission_classes=(permissions.AllowAny,
                     ),

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chars.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)