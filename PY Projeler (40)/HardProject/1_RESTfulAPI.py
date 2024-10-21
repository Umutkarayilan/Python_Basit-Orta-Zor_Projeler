# Proje Açıklaması: Django REST Framework kullanarak bir RESTful API oluşturun.
#  Bu API, kullanıcı yönetimi ve basit bir blog sistemi içerebilir.



# settings.py'de gerekli uygulamaları ekleyin
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.auth',
    'blog',  # Kendi uygulamanız
]

# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    yazar = models.ForeignKey(User, on_delete=models.CASCADE)
    baslik = models.CharField(max_length=100)
    icerik = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik

# blog/serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    yazar = serializers.ReadOnlyField(source='yazar.username')

    class Meta:
        model = Post
        fields = ['id', 'yazar', 'baslik', 'icerik', 'olusturulma_tarihi']

# blog/views.py
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-olusturulma_tarihi')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(yazar=self.request.user)

# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'postlar', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# projenin ana urls.py dosyasında blog uygulamasını ekleyin
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
]




# Django REST Framework kullanarak API endpoint'leri oluşturulur.
# Model-View-Serializer mimarisi ile veri modeli, görünüm ve serileştirici tanımlanır.
# Authentication ve Permissions ile güvenlik sağlanır.
# Router kullanılarak URL yapılandırması otomatikleştirilir.