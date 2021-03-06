from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^theory/', include('app.lessons.urls', namespace='theory')),
    url(r'^results/', include('app.answers.urls', namespace='results')),
    url(r'^user/', include('app.user.urls', namespace='user')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls', namespace='ckeditor')),
    url(r'^upload/', include('app.upload.urls', namespace='upload_files')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
