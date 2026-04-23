from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    HeroSectionViewSet,
    AboutUsViewSet,
    ServiceSectionViewSet,
    ServiceViewSet,
    HowItWorksViewSet,
    StepViewSet,
    TestimonialSectionViewSet,
    TestimonialViewSet,
    FeedbackViewSet,
    BlogViewSet,
    CommentViewSet,
    StoryViewSet,
    StoryResultViewSet
)
router = DefaultRouter()

# CORE
router.register(r'hero', HeroSectionViewSet)
router.register(r'about', AboutUsViewSet)

# SERVICES
router.register(r'service-sections', ServiceSectionViewSet)
router.register(r'services', ServiceViewSet)

# HOW IT WORKS
router.register(r'how-it-works', HowItWorksViewSet)
router.register(r'steps', StepViewSet)

# TESTIMONIALS
router.register(r'testimonial-sections', TestimonialSectionViewSet)
router.register(r'testimonials', TestimonialViewSet)

# FEEDBACK
router.register(r'feedback', FeedbackViewSet)

# BLOG
router.register(r'blogs', BlogViewSet)
router.register(r'comments', CommentViewSet)

#STORY
router.register(r'stories', StoryViewSet)
router.register(r'story-results', StoryResultViewSet)


urlpatterns = [
    path('', include(router.urls)),
]