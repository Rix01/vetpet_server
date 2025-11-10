from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# ViewSet 임포트
from user.views import UserViewSet
from hospital.views import HospitalViewSet
from category.views import CategoryViewSet
from pet.views import PetViewSet
from post.views import PostViewSet
from review.views import ReviewViewSet
from reservation.views import ReservationViewSet
from comment.views import CommentViewSet
from post_image.views import PostImageViewSet

# Router 생성
router = DefaultRouter()

# ViewSet 등록
router.register(r'users', UserViewSet)
router.register(r'hospitals', HospitalViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'pets', PetViewSet)
router.register(r'post', PostViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'post-images', PostImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
