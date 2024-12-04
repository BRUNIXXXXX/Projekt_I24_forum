from django.db import models

class Comment(models.Model):
    username = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True
    )  # Allow replies to comments

    def __str__(self):
        return f"{self.topic} by {self.username}"
