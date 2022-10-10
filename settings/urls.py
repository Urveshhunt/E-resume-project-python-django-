from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Urvesh Admin"
admin.site.site_title = "Urvesh Admin Portal"
admin.site.index_title = "Welcome to Urvesh Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("UserProfile.urls")),
    path('Company/',include('Company.urls')),
    path('Feedback/',include('Feedback.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)