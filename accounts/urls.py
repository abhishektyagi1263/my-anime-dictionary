from django.urls import path,include
from .views import *
urlpatterns = [
    path('', home , name='home'),
    path('landing', landing , name='landing'),
    path('accounts/login/', login_attempt , name='login_attempt'),
    path('accounts/logout/', logout_attempt , name='logout_attempt'),

    path('register', register_attempt , name='register_attempt'),
    path('log_out_page', log_out_page, name='log_out_page'),
    path('token', token_send, name='token_send'),
    path('success', success , name='success'),
    path('error' , error_page , name="error"),
    path('search_anime/<searched>',search_anime, name="search_anime"),
    path('detailv/<members>',detailv, name="detailv"),
    path('gen/<genre>',gen, name="gen"),
    path('top1movie/',top1movie, name="top1movie"),
    path('top1anime/',top1anime, name="top1anime"),
    path('sup/',sup,name='sup'),
    path('sin/',sin,name='sin'),
    path('similar_by_content/<query>',similar_by_content, name="similar_by_content"),
    
    # path('accounts/logout',logout,name="logout")

]