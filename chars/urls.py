from django.urls import path
from .views import  CharListCreate,  CharRetrieveUpdateDestroy

urlpatterns = [
    path('chars/',  CharListCreate.as_view(), name='char-view-create'),
    path(
        'chars/<int:pk>/',
          CharRetrieveUpdateDestroy.as_view(), 
          name='update'
          ),
]
