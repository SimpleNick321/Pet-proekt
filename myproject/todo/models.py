from django.db import models

# Create your models here.


class Todo(models.Model):
    IID = models.PositiveBigIntegerField(blank=True , null=False)
    DEP_ID = models.IntegerField()
    MED_ID = models.IntegerField()
    ANALOG_ID = models.IntegerField(null=True)
    KOD_SITE = models.IntegerField(null=True)
    QTTY = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    RPRICE_SITE = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    RPRICE = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    SPRICE = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    SALLPRICE = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    RPRICE_SITE_EXP = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    VPRICE = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    REG_PRICE = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    date_stock = models.DateTimeField(null=True)
    valid_date = models.DateField(null=True)
    VALID_PERIOD = models.IntegerField(null=True)
    class Meta:
        db_table = 'todo_todo'
        unique_together = ('IID', 'DEP_ID', 'MED_ID')
        indexes = [
            models.Index(fields=['MED_ID']),
            models.Index(fields=['KOD_SITE']),
        ]
        
    def __str__(self):
        return self.title


class Category(models.Model):
    db_table = 'todo_todo'
    unique_together = ('IID', 'DEP_ID', 'MED_ID')
    indexes = [
            models.Index(fields=['MED_ID']),
            models.Index(fields=['KOD_SITE']),
        ]

    def __str__(self):
        return self.title
