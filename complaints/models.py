from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Complaint(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    village = models.CharField(max_length=100)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    user_photo = models.ImageField(upload_to='complaints/', null=True, blank=True)
    admin_proof = models.ImageField(upload_to='proofs/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title