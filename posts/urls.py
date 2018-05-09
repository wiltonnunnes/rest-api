from django.conf.urls import url, include
from .views import PostList, UserList, TokenList
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
	url(r'^users/$', UserList.as_view(), name='user-list'),
	url(r'^posts/$', PostList.as_view(), name='post-list'),
	url(r'^api-token-auth/', rest_framework_views.obtain_auth_token),
	url(r'^tokens/$', TokenList.as_view(), name='token-list'),
]