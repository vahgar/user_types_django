from django.db import models

# Create your models here.
class School(models.Model):
    school_id = models.CharField(primary_key=True,max_length=20)
    school_name = models.CharField(max_length=300)
    school_branch_area = models.CharField(max_length=200)
    affiliation_number = models.CharField(max_length=100)
    board = models.CharField(max_length=10)
    address = models.CharField(max_length=1000)
    North = 'North'
    East = 'East'
    West = 'West'
    South = 'South'
    NorthEast = 'North East'
    NorthWest = 'Nort West'
    Central = "Central"
    NewDelhi = "New Delhi"
    SouthWest = "South West"
    zone_choices = (
        (North,'North'),
        (East,'East'),
        (West,'West'),
        (South,'South'),
        (NorthEast,'North East'),
        (NorthWest,'North West'),
        (Central,'Central'),
        (NewDelhi,'New Delhi'),
        (SouthWest,'South West'),
    )
    zone = models.CharField(max_length=15,choices=zone_choices)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    active_status = models.BooleanField(default=1)
    transport_incharge = models.CharField(max_length=50)
    transport_incharge_number = models.CharField(max_length=10)

    def __str__(self):
        return self.school_name +", "+ self.school_branch_area
