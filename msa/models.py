from django.db import models

class MSAlignment(models.Model):
    """Multiple sequence alignment made with ClustalO"""
    description = models.TextField()
    
    def __str__(self):
        return "MSA: %s" % self.description[:20]

class Position(models.Model):
    """One column in ClustalO alignment"""
    num = models.IntegerField()
    msa = models.ForeignKey(MSAlignment, related_name='positions', on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s position %d" % (self.msa, self.num)

