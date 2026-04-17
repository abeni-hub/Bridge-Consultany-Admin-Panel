from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from core.models import HeroSection, AboutUs ,ServiceSection, Service, HowItWorks, Step, TestimonialSection ,Testimonial,Comment,Feedback,Blog
from .serializers import *


# ========================
# BASE VIEWSET (Reusable)
# ========================

class BaseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]


# ========================
# CORE
# ========================

class HeroSectionViewSet(BaseViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
    search_fields = ['title']
    ordering_fields = ['id']


class AboutUsViewSet(BaseViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    search_fields = ['subtitle']
    ordering_fields = ['id']


# ========================
# SERVICES
# ========================

class ServiceSectionViewSet(BaseViewSet):
    queryset = ServiceSection.objects.prefetch_related('services').all()
    serializer_class = ServiceSectionSerializer
    search_fields = ['section_title']
    ordering_fields = ['id']


class ServiceViewSet(BaseViewSet):
    queryset = Service.objects.select_related('section').all()
    serializer_class = ServiceSerializer
    filterset_fields = ['section']
    search_fields = ['title']
    ordering_fields = ['id']


# ========================
# HOW IT WORKS
# ========================

class HowItWorksViewSet(BaseViewSet):
    queryset = HowItWorks.objects.prefetch_related('steps').all()
    serializer_class = HowItWorksSerializer
    search_fields = ['section_title']
    ordering_fields = ['id']


class StepViewSet(BaseViewSet):
    queryset = Step.objects.select_related('how_it_works').all()
    serializer_class = StepSerializer
    filterset_fields = ['how_it_works']
    ordering_fields = ['step_number']


# ========================
# TESTIMONIALS
# ========================

class TestimonialSectionViewSet(BaseViewSet):
    queryset = TestimonialSection.objects.prefetch_related('testimonials').all()
    serializer_class = TestimonialSectionSerializer
    search_fields = ['section_title']
    ordering_fields = ['id']


class TestimonialViewSet(BaseViewSet):
    queryset = Testimonial.objects.select_related('section').all()
    serializer_class = TestimonialSerializer
    filterset_fields = ['section', 'rating']
    ordering_fields = ['rating']


# ========================
# FEEDBACK
# ========================

class FeedbackViewSet(BaseViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filterset_fields = ['status', 'rating']
    search_fields = ['name', 'email']
    ordering_fields = ['created_at']


# ========================
# BLOG
# ========================

class BlogViewSet(BaseViewSet):
    queryset = Blog.objects.prefetch_related('comments').all()
    serializer_class = BlogSerializer
    filterset_fields = ['status', 'category']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']


class CommentViewSet(BaseViewSet):
    queryset = Comment.objects.select_related('post').all()
    serializer_class = CommentSerializer
    filterset_fields = ['status', 'post']
    ordering_fields = ['created_at']