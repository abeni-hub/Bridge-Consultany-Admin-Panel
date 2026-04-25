from rest_framework import serializers

from core.models import HeroSection, AboutUs ,ServiceSection, Service, HowItWorks, Step, TestimonialSection ,Testimonial,Comment,Feedback,Blog , Story , StoryResult
def to_camel_case(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.title() for word in parts[1:])


class CamelCaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {to_camel_case(k): v for k, v in data.items()}


# ========================
# CORE
# ========================




class HeroSectionSerializer(CamelCaseSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'


class AboutUsSerializer(CamelCaseSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


# ========================
# SERVICES
# ========================

class ServiceSerializer(CamelCaseSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceSectionSerializer(CamelCaseSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceSection
        fields = '__all__'


# ========================
# HOW IT WORKS
# ========================

class StepSerializer(CamelCaseSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class HowItWorksSerializer(CamelCaseSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = HowItWorks
        fields = '__all__'


# ========================
# TESTIMONIALS
# ========================

class TestimonialSerializer(CamelCaseSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class TestimonialSectionSerializer(CamelCaseSerializer):
    testimonials = TestimonialSerializer(many=True, read_only=True)

    class Meta:
        model = TestimonialSection
        fields = '__all__'


# ========================
# FEEDBACK
# ========================

class FeedbackSerializer(CamelCaseSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    # def validate(self, data):
    #     if not data.get("post") and not data.get("story"):
    #         raise serializers.ValidationError("Provide post or story")
    #     return data

# ========================
# BLOG


class BlogSerializer(CamelCaseSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'

class StoryResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryResult
        fields = "__all__"


class StorySerializer(serializers.ModelSerializer):
    results = StoryResultSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)


class StoryResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryResult
        fields = "__all__"


class StorySerializer(serializers.ModelSerializer):
    results = StoryResultSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = "__all__"