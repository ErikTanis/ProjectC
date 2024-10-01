from django.db import models

class Transfer(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=20)
    transfer_from = models.IntegerField(null=True, blank=True)
    transfer_to = models.IntegerField()
    transfer_status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.reference

class TransferItem(models.Model):
    transfer = models.ForeignKey(Transfer, related_name='items', on_delete=models.CASCADE)
    item_id = models.CharField(max_length=20)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.item_id} - {self.amount}"