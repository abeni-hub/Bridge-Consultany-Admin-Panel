from django.core.management.base import BaseCommand
from core.models import (
    HeroSection, AboutUs,
    ServiceSection, Service,
    HowItWorks, Step,
    TestimonialSection, Testimonial,
    Feedback, Blog, Comment
)


class Command(BaseCommand):
    help = "Seed database with mock data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # ========================
        # HERO
        # ========================
        hero = HeroSection.objects.create(
            title="Bridge Consulting",
            subtitle="We build scalable business solutions",
            primary_cta_text="Get Started",
            primary_cta_link="https://example.com/start",
            secondary_cta_text="Learn More",
            secondary_cta_link="https://example.com/about",
            background_image_url="https://picsum.photos/1200/600",
            stats={
                "clients": "200+",
                "projects": "500+"
            }
        )

        # ========================
        # ABOUT
        # ========================
        about = AboutUs.objects.create(
            subtitle="Who We Are",
            description="We help businesses grow.",
            mission_title="Our Mission",
            mission_content="Deliver value",
            vision_title="Our Vision",
            vision_content="Global impact",
            years_of_excellence=10,
            companies_count_text="100+ companies",
            image_url="https://picsum.photos/500/400",
            cta_title="Join Us",
            cta_content="Let’s work together"
        )

        # ========================
        # SERVICES
        # ========================
        service_section = ServiceSection.objects.create(
            section_subtitle="Services",
            section_title="What We Offer",
            description="Our core services"
        )

        Service.objects.create(
            section=service_section,
            title="IT Consulting",
            description="Expert IT solutions",
            icon="code",
            gradient="blue",
            features=["scalable", "secure"]
        )

        Service.objects.create(
            section=service_section,
            title="Business Strategy",
            description="Growth strategies",
            icon="chart",
            gradient="green",
            features=["growth", "planning"]
        )

        # ========================
        # HOW IT WORKS
        # ========================
        how = HowItWorks.objects.create(
            section_subtitle="Process",
            section_title="How It Works",
            description="Our workflow",
            cta_button_text="Start Now"
        )

        Step.objects.create(
            how_it_works=how,
            step_number=1,
            title="Consultation",
            description="We understand your needs",
            icon="chat",
            deliverables=["analysis", "report"]
        )

        Step.objects.create(
            how_it_works=how,
            step_number=2,
            title="Execution",
            description="We implement solutions",
            icon="build",
            deliverables=["deployment", "support"]
        )

        # ========================
        # TESTIMONIALS
        # ========================
        test_section = TestimonialSection.objects.create(
            section_subtitle="Testimonials",
            section_title="What Clients Say",
            description="Client feedback",
            cta_title="Join them",
            cta_content="Work with us"
        )

        Testimonial.objects.create(
            section=test_section,
            name="John Doe",
            role="CEO",
            company="Tech Corp",
            image_url="https://picsum.photos/100",
            testimonial="Amazing service!",
            rating=5,
            gradient="purple"
        )

        # ========================
        # BLOG
        # ========================
        blog = Blog.objects.create(
            title="How to Grow Business",
            category="Business",
            status="published",
            image_url="https://picsum.photos/600/400",
            expert="Admin",
            content="Content goes here..."
        )

        Comment.objects.create(
            post=blog,
            user="Alice",
            comment="Great article!",
            status="approved"
        )

        # ========================
        # FEEDBACK
        # ========================
        Feedback.objects.create(
            name="Client One",
            email="client@test.com",
            rating=5,
            status="new",
            message="Excellent service!"
        )

        self.stdout.write(self.style.SUCCESS("✅ Data seeded successfully!"))