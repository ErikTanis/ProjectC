from django.db import models

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.CharField(max_length=20)
    description = models.TextField()
    item_reference = models.CharField(max_length=20)
    locations = models.JSONField()
    total_on_hand = models.IntegerField()
    total_expected = models.IntegerField()
    total_ordered = models.IntegerField()
    total_allocated = models.IntegerField()
    total_available = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.item_id