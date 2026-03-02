from django.db import models
from accounts.models import CustomUser

class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='feedbacks')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], help_text="Rating out of 5")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user.username} on {self.subject}"

    class Meta:
        ordering = ['-submitted_at']
