from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('account', include('account.urls')),
    path('dashboard', include('dashboard.urls')),
    path('agent', include('agent.urls')),
    path('services/', include('services.urls')),
    path('freelance/', include('freelance.urls')),
    path('payment/', include('payment.urls')),
    path('partner/', include('partner.urls')),
    path('', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)