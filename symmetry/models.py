from django.db import models
from pdbase.models import 

class Contact(models.Model):
    """Represents one crystal contact between chains"""
    d     = models.FloatField()
    y     = models.FloatField()
    z     = models.FloatField()
    residue = models.ForeignKey(Residue, related_name='atoms', on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s" % self.name

