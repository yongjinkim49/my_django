# accounts/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User   # 추가

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):   # 추가    
    user = models.OneToOneField(User, on_delete=models.CASCADE) # User와 연결
    college = models.CharField(max_length=20, blank=True) #college field 추가
    major = models.CharField(max_length=20, blank=True) #major field 추가
    def __str__(self):   # 추가        
        return f'id={self.id}, user_id={self.user.id}, college={self.college}, major={self.major}'
    # 아래 코드 추가  
    @receiver(post_save, sender=User)  
    def create_user_profile(sender, instance, created, **kwargs):        
        if created:          
            Profile.objects.create(user=instance)  
    
    @receiver(post_save, sender=User)  
    def save_user_profile(sender, instance, **kwargs):        
        instance.profile.save()