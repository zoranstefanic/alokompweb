from django.db import models
from django.contrib.auth.models import User

import datetime
from dateutil.relativedelta import relativedelta

WORKPLAN_ITEM_CHOICES = [
    ('O', 'Objective'),
    ('A', 'Activity'),
    ('M', 'Milestone'),
    ('D', 'Deliverable'),
]

TAG_CHOICES = [
    ('1', 'General'),
    ('2', 'Equipment'),
    ('3', 'Disemination'),
    ('4', 'Doctoral'),
]

PROJECT_START = datetime.date(2020,1,1)

class Period(models.Model):
    """Generally represents one cell of the worplan table """
    tag = models.IntegerField(choices=TAG_CHOICES,default=1) 
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    users = models.ManyToManyField(User,related_name="workplan_items")

    def __unicode__(self):
        return "%s %s" % (self.start, self.end)

    def __str__(self):
        return "%s %s" % (self.start, self.end)

    def set_start_end(self,m1,m2):
        "Sets the start and end date based on months since PROJECT_START"
        self.start = PROJECT_START + relativedelta(months=m1-1) 
        self.end = PROJECT_START + relativedelta(months=m2,days=-1) 
        self.save()

class Item(models.Model):
    """Generally represents one cell of the worplan table """
    type = models.CharField(max_length=10,choices=WORKPLAN_ITEM_CHOICES) 
    label = models.CharField(max_length=10)
    text = models.TextField()
    depends_on = models.ManyToManyField('self')
    period = models.ForeignKey(Period,on_delete=models.CASCADE,related_name="items",null=True)
   
    def name(self):
        return dict(WORKPLAN_ITEM_CHOICES)[self.type]

    def __unicode__(self):
        return "%s %s" % (self.name(), self.label)

    def __str__(self):
        return "%s %s" % (self.name(), self.label)
