
from django.contrib import admin
from django. urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('plp_ecommerce/', include('plp_ecommerce.urls')),
]

