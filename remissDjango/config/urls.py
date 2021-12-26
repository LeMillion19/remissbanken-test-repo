from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cards/', include('cards.urls')),
    path('decks/', include('decks.urls')),
    path('', include('rest_framework.urls')),
]
