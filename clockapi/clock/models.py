from django.contrib.auth.models import User
from django.db import models, transaction

# Create your models here.
class Clock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    name = models.CharField(max_length=100)
    is_selected = models.BooleanField(default = False)
    is_deleted = models.BooleanField(db_column = 'is_deleted', default = False)
   
    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.is_selected:
            Clock.objects.filter(user = self.user).filter(
                is_selected=True).update(is_selected=False)
        super(Clock, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'clock'
        ordering = ('created_on',)