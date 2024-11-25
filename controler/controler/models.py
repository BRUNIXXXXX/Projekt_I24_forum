from django.db import models

class Comment(models.Model):
    username = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} by {self.username}"
