from django.db import models
from pdbase.models import *

class Contact(models.Model):
    """Represents one crystal contact between chains"""
    d = models.FloatField()
    prob = models.CharField(max_length=3)
    from_atom = models.ForeignKey(Atom, related_name='contacts_from', on_delete=models.CASCADE)
    to_atom = models.ForeignKey(Atom, related_name='contacts_to', on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s" % self.name
