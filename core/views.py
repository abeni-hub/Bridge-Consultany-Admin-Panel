from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import CommentPermission


from core.models import (
    HeroSection, AboutUs,
    ServiceSection, Service,
    HowItWorks, Step,
    TestimonialSection, Testimonial,
    Comment, Feedback, Blog, Story, StoryResult
)

from .serializers import *


# ========================
# PERMISSION
# ========================

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


# ========================
# BASE
# ========================

class BaseViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]


# ========================
# CORE
# ========================

class HeroSectionViewSet(BaseViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer


class AboutUsViewSet(BaseViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


# ========================
# SERVICES
# ========================

class ServiceSectionViewSet(BaseViewSet):
    queryset = ServiceSection.objects.prefetch_related('services')
    serializer_class = ServiceSectionSerializer


class ServiceViewSet(BaseViewSet):
    queryset = Service.objects.select_related('section')
    serializer_class = ServiceSerializer


# ========================
# HOW IT WORKS
# ========================

class HowItWorksViewSet(BaseViewSet):
    queryset = HowItWorks.objects.prefetch_related('steps')
    serializer_class = HowItWorksSerializer


class StepViewSet(BaseViewSet):
    queryset = Step.objects.select_related('how_it_works')
    serializer_class = StepSerializer


# ========================
# TESTIMONIALS
# ========================

class TestimonialSectionViewSet(BaseViewSet):
    queryset = TestimonialSection.objects.prefetch_related('testimonials')
    serializer_class = TestimonialSectionSerializer


class TestimonialViewSet(BaseViewSet):
    queryset = Testimonial.objects.select_related('section')
    serializer_class = TestimonialSerializer


# ========================
# FEEDBACK
# ========================

class FeedbackViewSet(BaseViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


# ========================
# BLOG
# ========================

class BlogViewSet(BaseViewSet):
    queryset = Blog.objects.prefetch_related('comments')
    serializer_class = BlogSerializer
    lookup_field = 'slug'


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # ✅ FIXED
    filterset_fields = ['status']   # only real fields

    search_fields = ['full_name', 'email', 'comment']
    ordering_fields = ['created_at']


# ========================
# STORY
# ========================

class StoryViewSet(BaseViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryResultViewSet(BaseViewSet):
    queryset = StoryResult.objects.all()
    serializer_class = StoryResultSerializer