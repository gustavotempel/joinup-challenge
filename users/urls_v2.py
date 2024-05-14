from django.urls import path

from users.views_v2 import UserView


urlpatterns = [
    path('signup/', UserView.as_view(), name='users'),
    path('profile/<email>/', UserView.as_view(), name='users'),

]