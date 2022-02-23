from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView
# from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicaciones.Usuario.urls')),
    path('', include('Aplicaciones.report.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view()),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='Aplicaciones/Usuario/templates/login.html')),
    path("accounts/login/", auth_views.LoginView.as_view(template_name = "login.html"), name='login'),
    path("^logout/$", auth_views.LogoutView.as_view(next_page = 'login'), name= 'logout'),
    # path('login', LoginView.as_view(),{'template_name':'login.html'}, name = 'login')
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]