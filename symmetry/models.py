from django.db import models
from pdbase.models import Atom, Pdb, Residue, Chain

class SymmOp(models.Model):
    """Represents a symmetry operation in the group"""
    rot = models.CharField(null=True,max_length=50)
    trans = models.CharField(null=True,max_length=50)
    geom = models.CharField(max_length=100,null=True,help_text="Geometric interpretation")
    pdb = models.ForeignKey(Pdb, null=True, related_name="symops",on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s + %s" % (self.rot,self.trans)

class Contact(models.Model):
    """Represents one crystal contact between chains"""
    d = models.FloatField()
    prob = models.CharField(max_length=3)
    from_atom = models.ForeignKey(Atom, related_name='contacts_from', on_delete=models.CASCADE)
    to_atom = models.ForeignKey(Atom, related_name='contacts_to', on_delete=models.CASCADE)
    symop = models.ForeignKey(SymmOp, null=True, related_name='contacts',on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s %s %s" % (self.from_atom, self.to_atom, self.prob, self.d)

class SymOp(models.Model):
    """Represents a symmetry operation between residues"""
    sym = models.CharField(null=True,max_length=100)
    sym_type = models.IntegerField(null=True)
    type = models.CharField(null=True,max_length=10)
    unit_cell = models.ForeignKey('UnitCell',on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s" % (self.sym)

class ResidueContact(models.Model):
    """Represents one crystal contact between chains"""
    d = models.FloatField()
    res1 = models.ForeignKey(Residue, related_name='rescont1', on_delete=models.CASCADE)
    res2 = models.ForeignKey(Residue, related_name='rescont2', on_delete=models.CASCADE)
    symop = models.ForeignKey(SymOp, null=True, related_name='rescontacts',on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s --- %s" % (self.res1, self.res2)

class UnitCell(models.Model):
    """Represents unit cell and symmetry"""
    params  = models.JSONField(null=True)
    sg = models.CharField(max_length=10)
    num = models.IntegerField()
    pdb = models.OneToOneField(Pdb, related_name="unit_cell",on_delete=models.CASCADE)
    projections  = models.JSONField(null=True)
    
    def __str__(self):
        return "%s" % self.sg

class Interface(models.Model):
    """Represents interfaces between two chains"""
    num = models.IntegerField()
    pdb = models.ForeignKey(Pdb, null=True, related_name="interfaces",on_delete=models.CASCADE)
    chain1 = models.ForeignKey(Chain, null=True, related_name="ifaces1",on_delete=models.CASCADE,)
    chain2 = models.ForeignKey(Chain, null=True, related_name="ifaces2",on_delete=models.CASCADE,)
    area = models.FloatField()
    type1 = models.CharField(max_length=10)
    confidence = models.FloatField()
    symop = models.ForeignKey(SymOp, null=True, related_name='interfaces',on_delete=models.CASCADE)
    
    def __str__(self):
        return "%d" % self.id

class InterfaceResidueContact(models.Model):
    """Represents contact between two residues on the interface"""
    interface = models.ForeignKey(Interface, null=True, related_name="rescontacts",on_delete=models.CASCADE)
    mind = models.FloatField()
    num_atoms = models.IntegerField()
    res1 = models.ForeignKey(Residue, related_name='ifrc1', on_delete=models.CASCADE)
    res2 = models.ForeignKey(Residue, related_name='ifrc2', on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s --- %s" % (self.res1, self.res2)
