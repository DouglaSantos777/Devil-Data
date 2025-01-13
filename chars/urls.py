from django.urls import path
from .views import CharList, CharDetail

urlpatterns = [
    path('chars/', CharList.as_view(), name='char-list'),
    path('chars/<int:pk>/', CharDetail.as_view(), name='char-detail'),
]
