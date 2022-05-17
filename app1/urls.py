from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('createblog/<str:names>', views.createblog, name='createblog'),
    path('myprofile/<str:name>', views.myprofile, name='myprofile'),
    path('about', views.about,name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('forgot', views.forgot, name='forgot'),
    path('blogpost/<int:id>', views.blogpost, name='blogpost'),
    path('search', views.search, name='search'),
    path('covid', views.covid, name='covid'),
    path('forgotpass/<str:id>',views.forgotpass,name='forgotpass'),
    path('forgotpass/changepassword/<str:id>', views.changepassword, name='changepassword'),
    path('deletepost/<int:id>', views.deletepost, name='deletepost')

]