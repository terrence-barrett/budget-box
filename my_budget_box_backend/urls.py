from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('apps.posts.urls')),
    path('category/',include('apps.category.urls')),
    path('transactions/',include('apps.transactions.urls')),
    path('users/',include('apps.users.urls'))
]