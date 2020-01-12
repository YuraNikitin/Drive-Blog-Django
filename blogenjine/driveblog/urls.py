from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),

    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name = 'tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),

    path('login/', Login.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', RegisterNewUser.as_view(), name='register_user_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
