from django.contrib import admin
from django.urls import path
from analyzer.views import upload_resume
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_resume, name='upload_resume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
