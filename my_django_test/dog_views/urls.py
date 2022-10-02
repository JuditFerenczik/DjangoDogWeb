

from django.urls import path
from . import views


app_name = 'dog_views'
urlpatterns = [
    path('list/', views.DoggoListView.as_view(), name='list_dog'),
    path('add/', views.DoggoCreateView.as_view(), name='add_dog'),
    path('add_owner/', views.OwnerCreateView.as_view(), name='add_owner'),
    path('list/delete_dog/<int:pk>', views.DoggoDeleteView.as_view(), name='delete_dog'),
    path('delete_owner/<int:pk>', views.OwnerDeleteView.as_view(), name='delete_owner'),
    path('detail_dog/<int:pk>', views.DoggoDetailView.as_view(), name='detail_dog'),
    path('edit_dog/<int:pk>', views.DoggoUpdateView.as_view(), name='edit_dog'),
    path('edit_owner/<int:pk>', views.OwnerUpdateView.as_view(), name='edit_owner'),
    path('list_owners/', views.OwnerListView.as_view(), name='list_owner'),
    path('owner_dog/<int:pk>', views.OwnerDetailView.as_view(), name='detail_owner')
]