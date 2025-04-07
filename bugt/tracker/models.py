from django.db import models

class Bug(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(
        max_length=10,
        choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]
    )
    status = models.CharField(
        max_length=15,
        choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Closed', 'Closed')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
