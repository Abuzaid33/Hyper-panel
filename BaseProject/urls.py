from django.contrib import admin
from django.urls import path
from Baseapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signuppage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('home/', views.home_view, name='home'),  # Update the view function name
    path('logout/', views.logoutpage, name='logout'),
    path('landing/', views.landing, name='landing'),
    path('pages/404-alt/', views.pages_404_alt, name='page_404_alt'),
    path('pages/404/', views.pages_404, name='page_404'),
    path('pages/500/', views.pages_500, name='page_500'),
    path('pages/confirm-mail-2/', views.pages_confirm_mail_2, name='page_confirm_mail_2'),
    path('pages/confirm-mail/', views.pages_confirm_mail, name='page_confirm_mail'),
    path('pages/lock-screen-2/', views.pages_lock_screen_2, name='page_lock_screen_2'),
    path('pages/lock-screen/', views.pages_lock_screen, name='page_lock_screen'),
    path('pages/login/', views.pages_login, name='page_login'),
    path('pages/logout/', views.pages_logout, name='page_logout'),
    path('pages/maintenance/', views.pages_maintenance, name='page_maintenance'),
    path('pages/preloader/', views.pages_preloader, name='page_preloader'),
    path('pages/recoverpw-2/', views.pages_recoverpw_2, name='page_recoverpw_2'),
    path('pages/recoverpw/', views.page_recoverpw, name='page_recoverpw'),
    path('pages/register/', views.pages_register, name='page_register'),
    path('pages/starter/', views.pages_starter, name='page_starter'),
    path('layouts/compact/', views.compact_layout, name='compact_layout'),
    path('layouts/detached/', views.detached_layout, name='detached_layout'),
    path('layouts/full/', views.full_layout, name='full_layout'),
    path('layouts/fullscreen/', views.fullscreen_layout, name='fullscreen_layout'),
    path('layouts/horizontal/', views.horizontal_layout, name='horizontal_layout'),
    path('layouts/hover/', views.hover_layout, name='hover_layout'),
    path('layouts/icon/', views.icon_layout, name='icon_layout'),

]
