from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from core.models import (
    HeroSection, AboutUs,
    ServiceSection, Service,
    HowItWorks, Step,
    TestimonialSection, Testimonial,
    Comment, Feedback, Blog , Story , StoryResult
)

from .serializers import *


# ========================
# BASE VIEWSET
# ========================

class BaseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


# ========================
# ADMIN-ONLY WRITE MIXIN
# ========================

class AdminWritePermissionMixin:
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]


# ========================
# CORE
# ========================

class HeroSectionViewSet(AdminWritePermissionMixin, BaseViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
    search_fields = ['title']
    ordering_fields = ['id']


class AboutUsViewSet(AdminWritePermissionMixin, BaseViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    search_fields = ['subtitle']
    ordering_fields = ['id']


# ========================
# SERVICES
# ========================

class ServiceSectionViewSet(AdminWritePermissionMixin, BaseViewSet):
    queryset = ServiceSection.objects.prefetch_related('services')
    serializer_class = ServiceSectionSerializer
    search_fields = ['section_title']
    ordering_fields = ['id']


class ServiceViewSet(AdminWritePermissionMixin, BaseViewSet):
    queryset = Service.objects.select_related('section')
    serializer_class = ServiceSerializer
    filterset_fields = ['section']
    search_fields = ['title']
    ordering_fields = ['id']


# ========================
# HOW IT WORKS
# ========================

class HowItWorksViewSet(AdminWritePermissionMixin, BaseViewSet):
    queryset = HowItWorks.objects.prefetch_related('steps')
    serializer_class = HowItWorksSerializer
    search_fields = ['section_title']
    ordering_fields = ['id']


class StepViewSet(AdminWritePermissionMixin, BaseViewSet):
    queryset = Step.objects.select_related('how_it_works')
    serializer_class = StepSerializer
    filterset_fields = ['how_it_works']
    ordering_fields = ['step_number']


# ========================
# TESTIMONIALS
# ========================

class TestimonialSectionViewSet(AdminWritePermissionMixin, BaseViewSet):
    queryset = TestimonialSection.objects.prefetch_related('testimonials')
    serializer_class = TestimonialSectionSerializer
    search_fields = ['section_title']
    ordering_fields = ['id']


class TestimonialViewSet(AdminWritePermissionMixin, BaseViewSet):
    queryset = Testimonial.objects.select_related('section')
    serializer_class = TestimonialSerializer
    filterset_fields = ['section', 'rating']
    ordering_fields = ['rating']


# ========================
# FEEDBACK
# ========================

class FeedbackViewSet(AdminWritePermissionMixin, BaseViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filterset_fields = ['status', 'rating']
    search_fields = ['name', 'email']
    ordering_fields = ['created_at']


# ========================
# BLOG
# ========================

class BlogViewSet(AdminWritePermissionMixin, BaseViewSet):
    queryset = Blog.objects.prefetch_related('comments')
    serializer_class = BlogSerializer
    filterset_fields = ['status', 'category']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']
    lookup_field = 'slug'   # ✅ SEO-friendly URLs


class CommentViewSet(AdminWritePermissionMixin, BaseViewSet):
    queryset = Comment.objects.select_related('post')
    serializer_class = CommentSerializer
    filterset_fields = ['status', 'post']
    ordering_fields = ['created_at']

class StoryViewSet(AdminWritePermissionMixin, ModelViewSet):
    queryset = Story.objects.prefetch_related('results').all()
    serializer_class = StorySerializer
    search_fields = ['title', 'client', 'industry']
    ordering_fields = ['created_at']


class StoryResultViewSet(AdminWritePermissionMixin, ModelViewSet):
    queryset = StoryResult.objects.select_related('story').all()
    serializer_class = StoryResultSerializer
    filterset_fields = ['story']
    ordering_fields = ['id']

