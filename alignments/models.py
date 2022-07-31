from django.db import models
from pdbase.models import Chain, Residue

class Alignment(models.Model):
    """Structural alignment made with GESAMT"""
    Qscore  = models.FloatField()
    rmsd  = models.FloatField()
    aligned_num = models.IntegerField()
    seq_identity = models.FloatField()
    chain_fixed = models.ForeignKey(Chain,related_name="alignments_fixed", on_delete=models.CASCADE)
    chain_moving = models.ForeignKey(Chain,related_name="alignments_moving", on_delete=models.CASCADE)
    
    def __unicode__(self):
        return "%s|%s" % (self.chain_fixed,self.chain_moving)

    def __str__(self):
        return "%s|%s" % (self.chain_fixed,self.chain_moving)

class ResidueMatch(models.Model):
    """One row in the GESAMT alignment"""
    hydrophobicity = [('-','hydrophobic'),('+','hydrophylic'),('.','neutral')]
    secondary_structure = [('H','helix'),('S','sheet')]

    position = models.IntegerField()
    text = models.CharField(max_length=50)
    alignment = models.ForeignKey(Alignment, related_name='positions', on_delete=models.CASCADE)
    fixed = models.ForeignKey(Residue, related_name='matches_fixed',on_delete=models.CASCADE,null=True)
    moving = models.ForeignKey(Residue, related_name='matches_moving',on_delete=models.CASCADE,null=True)
    distance = models.FloatField(null=True)
    similarity = models.IntegerField(null=True)
    ss_fixed = models.CharField(max_length=1,choices=secondary_structure,null=True) # helix or sheet fixed residue
    ss_moving = models.CharField(max_length=1,choices=secondary_structure,null=True) # helix or sheet moving residue 
    h_fixed = models.CharField(max_length=1,choices=hydrophobicity,null=True) # hydrophobicity fixed residue
    h_moving = models.CharField(max_length=1,choices=hydrophobicity,null=True) # hydrophobicity moving residue
    
    def __str__(self):
        return "%s ---- %s %.2f" % (self.fixed,self.moving,self.distance)

