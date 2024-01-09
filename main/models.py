
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse



# Create your models here.

class Skills (models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
        
    name = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    url = models.URLField( blank=True, null=True)
    image = models.FileField( blank=True, null=True, upload_to= 'skills')
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
class UserProfile (models.Model):
    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField( blank=True, null=True, upload_to= 'avatar')
    skills = models.ManyToManyField(Skills, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to= 'cv')
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
class Testimonial (models.Model):
    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        
    name = models.CharField(max_length=200, blank=True, null=True)
    title = models.TextField(max_length=256, blank=True, null=True)
    role = models.CharField(max_length=20, blank=True, null=True)
    thumbnail = models.ImageField( blank=True, null=True, upload_to= 'thumbnail')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

class Media (models.Model):
    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ['name']
        
    image = models.ImageField( blank=True, null=True, upload_to= 'media')
    url = models.URLField( blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)
    
    def save (self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name


class Portfolio (models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    skill = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField( blank=True, null=True)
    image = models.FileField( blank=True, null=True, upload_to= 'portfolio')
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    


class Blog (models.Model):
    class Meta:
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
        ordering = ["timestamp"]
        
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    author_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    author_profession = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField( blank=True, null=True)
    feature_image = models.ImageField( blank=True, null=True, upload_to= 'blog')
    author_image = models.ImageField( blank=True, null=True, upload_to= 'author_image')
    slug = models.SlugField( blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_recent = models.BooleanField(default=False)
    is_feature = models.BooleanField(default=True)
    
    def save (self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # return reverse('main:blog', args=[self.id,])
        return f'/blog/{self.slug}'
    
    