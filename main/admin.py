from django.contrib import admin
from .models import (
    UserProfile,
    Testimonial,
    Media,
    Portfolio,
    Blog,
    Skills
)

# Register your models here.

@admin.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'is_active')
    
@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' )


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'is_active')

@admin.register(Blog)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'is_active')
    readonly_fields = ('slug',)
    
@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'is_active')