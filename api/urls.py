from django.urls import path
from .views import UserListView, UserDetailView, ProfileView, MenuListView, MenuDetailView, DiscountedMenuListView, OrderCreateView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('menus/', MenuListView.as_view(), name='menu-list'),
    path('menus/<int:pk>/', MenuDetailView.as_view(), name='menu-detail'),
    path('menus/discounted/', DiscountedMenuListView.as_view(), name='discounted-menu-list'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),
]
