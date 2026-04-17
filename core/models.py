from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    primary_cta_text = models.CharField(max_length=100)
    primary_cta_link = models.URLField()
    secondary_cta_text = models.CharField(max_length=100, blank=True)
    secondary_cta_link = models.URLField(blank=True)
    background_image_url = models.URLField()
    stats = models.JSONField(blank=True, null=True)

class AboutUs(models.Model):
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    mission_title = models.CharField(max_length=255)
    mission_content = models.TextField()
    vision_title = models.CharField(max_length=255)
    vision_content = models.TextField()
    years_of_excellence = models.IntegerField()
    companies_count_text = models.CharField(max_length=100)
    image_url = models.URLField()
    cta_title = models.CharField(max_length=255)
    cta_content = models.TextField()

class ServiceSection(models.Model):
    section_subtitle = models.CharField(max_length=255)
    section_title = models.CharField(max_length=255)
    description = models.TextField()

class Service(models.Model):
    ICON_CHOICES = [
        ('chart', 'Chart'),
        ('code', 'Code'),
    ]

    section = models.ForeignKey(ServiceSection, related_name="services", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    gradient = models.CharField(max_length=100)
    features = models.JSONField()

class HowItWorks(models.Model):
    section_subtitle = models.CharField(max_length=255)
    section_title = models.CharField(max_length=255)
    description = models.TextField()
    cta_button_text = models.CharField(max_length=100)

class Step(models.Model):
    how_it_works = models.ForeignKey(HowItWorks, related_name="steps", on_delete=models.CASCADE)
    step_number = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    deliverables = models.JSONField()

class TestimonialSection(models.Model):
    section_subtitle = models.CharField(max_length=255)
    section_title = models.CharField(max_length=255)
    description = models.TextField()
    cta_title = models.CharField(max_length=255)
    cta_content = models.TextField()

class Testimonial(models.Model):
    section = models.ForeignKey(TestimonialSection, related_name="testimonials", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    image_url = models.URLField()
    testimonial = models.TextField()
    rating = models.IntegerField()
    gradient = models.CharField(max_length=100)

    def clean(self):
        if not (1 <= self.rating <= 5):
            raise ValidationError("Rating must be between 1 and 5")

class Feedback(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    rating = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

from django.utils.text import slugify

class Blog(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    image_url = models.URLField()
    expert = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    post = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    comment = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)