import os
from django.db import models

class MDdirectory(models.Model):
    """Directory with MD trajectories"""
    name = models.CharField(max_length=300,help_text="Directory with MD simulations")
    note = models.TextField(help_text="Note on this directory", null=True)
    atime = models.DateTimeField()
    mtime = models.DateTimeField()
    ctime = models.DateTimeField()
    
    class Meta:
        ordering = ['-atime']

    def __unicode__(self):
        return "%s" % self.name

    def __str__(self):
        return "%s" % self.name


class MDtrajectory(models.Model):
    """Represents MD trajectory"""
    type_choices= [('amber','Amber'),('gromacs','Gromacs')]

    type = models.CharField(max_length=10,choices=type_choices,help_text="What type of trajectory")
    file = models.CharField(max_length=300,help_text="Directory with MD simulations")
    note = models.TextField(help_text="Note on this trajectory", null=True)
    directory = models.ForeignKey(MDdirectory, related_name='trajectories',on_delete=models.CASCADE,null=True)
    atime = models.DateTimeField()
    mtime = models.DateTimeField()
    ctime = models.DateTimeField()
    filesize = models.BigIntegerField() 
    # Data from trajectory
    totaltime = models.FloatField()
    num_atoms = models.IntegerField()
    num_frames = models.IntegerField()
    
    class Meta:
        ordering = ['-atime']

    def filename(self):
        return os.path.basename(self.file)

    def __str__(self):
       return "%s" % self.filename()
