from django.db import models
from msa.models import Position

class Pdb(models.Model):
    """PDB structure """
    code  = models.CharField(primary_key=True,max_length=4)
    title = models.TextField()
    data  = models.JSONField(null=True)
    
    def __unicode__(self):
        return "%s" % self.code

    def __str__(self):
        return "%s" % self.code

class Chain(models.Model):
    """One chain in the PDB structure """
    chain_id  = models.CharField(max_length=4)
    is_protein = models.BooleanField(default=True)
    pdb = models.ForeignKey(Pdb, related_name='chains', on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s-%s" % (self.pdb,self.chain_id)

class Residue(models.Model):
    """One residue in the PDB structure """
    name  = models.CharField(max_length=4)
    num  = models.IntegerField(null=True)
    chain = models.ForeignKey(Chain, related_name='residues', on_delete=models.CASCADE)
    msa_position = models.ForeignKey(Position, related_name='aligned_residues', null=True, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['num']
    
    def __str__(self):
        return "%s %s" % (self.name,self.num)

class Atom(models.Model):
    """One atom in residue"""
    name  = models.CharField(max_length=4)
    num  = models.IntegerField(null=True)
    x     = models.FloatField()
    y     = models.FloatField()
    z     = models.FloatField()
    bfactor = models.FloatField()
    residue = models.ForeignKey(Residue, related_name='atoms', on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s" % self.name
