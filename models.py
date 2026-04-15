from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import random
import string

# Create your models here.


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        DONOR = 'DONOR', 'Donor'
        HOSPITAL = 'HOSPITAL', 'Hospital/User'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.HOSPITAL)
    email_verified = models.BooleanField(default=False)


class EmailVerification(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.otp:
            self.otp = ''.join(random.choices(string.digits, k=6))
        if not self.expires_at:
            self.expires_at = timezone.now() + timezone.timedelta(minutes=10)
        super().save(*args, **kwargs)
    
    def is_valid(self):
        return not self.is_used and timezone.now() < self.expires_at
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.email} - {self.otp}"
