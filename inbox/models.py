from django.db import models
from authentication.models import CustomUser
from django.core.exceptions import ValidationError

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='sent_messages')
    recipient = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,related_name='received_messages')
    subject= models.CharField(max_length= 200, blank=True)
    body=models.TextField()
    is_read = models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['is_read', '-created']
    
    def clean(self):
        if self.sender is not None and self.recipient is not None:
            if self.sender_id == self.recipient_id:
                raise ValidationError("You can't send a message to yourself")
    
    def __str__(self):
        return f"From {self.sender} to {self.recipient}"