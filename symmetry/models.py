from django.db import models
from pdbase.models import *

class Contact(models.Model):
    """Represents one crystal contact between chains"""
    d = models.FloatField()
    prob = models.CharField(max_length=3)
    from_atom = models.ForeignKey(Atom, related_name='contacts_from', on_delete=models.CASCADE)
    to_atom = models.ForeignKey(Atom, related_name='contacts_to', on_delete=models.CASCADE)
    symop = models.ForeignKey('SymmOp', null=True, related_name='contacts',on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s %s %s" % (self.from_atom, self.to_atom, self.prob, self.d)

class UnitCell(models.Model):
    """Represents unit cell and symmetry"""
    params  = models.JSONField(null=True)
    sg = models.CharField(max_length=10)
    num = models.IntegerField()
    pdb = models.OneToOneField(Pdb, related_name="unit_cell",on_delete=models.CASCADE)
    projections  = models.JSONField(null=True)
    
    def __str__(self):
        return "%s" % self.sg

class SymmOp(models.Model):
    """Represents a symmetry operation in the group"""
    rot = models.CharField(null=True,max_length=50)
    trans = models.CharField(null=True,max_length=50)
    geom = models.CharField(max_length=100,null=True,help_text="Geometric interpretation")
    pdb = models.ForeignKey(Pdb, null=True, related_name="symops",on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s + %s" % (self.rot,self.trans)
