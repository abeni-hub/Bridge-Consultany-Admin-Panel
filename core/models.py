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
    section = models.ForeignKey("ServiceSection", related_name="services", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=100)  # removed choices
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
    name = models.CharField(max_length=255)
    email = models.EmailField()
    rating = models.IntegerField()
    status = models.CharField(max_length=50, default='new')  # removed choices
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=50)  # removed choices
    image_url = models.URLField()
    expert = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

# ========================
# ✅ SIMPLE COMMENT (NO FK)
class Comment(models.Model):
    fullName = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()
    Company = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)


class Story(models.Model):
    title = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    image = models.URLField()
    description = models.TextField()
    gradient = models.CharField(max_length=100)
    challenge = models.TextField()
    solution = models.TextField()
    impact = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class StoryResult(models.Model):
    story = models.ForeignKey(Story, related_name="results", on_delete=models.CASCADE)
    metric = models.CharField(max_length=255)
    value = models.CharField(max_length=50)
    icon = models.CharField(max_length=100)
    description = models.TextField()