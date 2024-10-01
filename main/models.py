import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TokoSepatuMuslim(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5


