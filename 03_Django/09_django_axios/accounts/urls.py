from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('<username>/', views.profile, name='profile'),  # 맨위로 올리면 안 됨. 왜냐면 signup 찾을 때 여기로 들어옴. signup이라는 문자 자체가 <> 이 안으로 들어가서 username이 됨.
]