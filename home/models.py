from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Cricket(models.Model):
    men = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return str(self.college)


class TableTennis(models.Model):
    men = models.IntegerField(blank=True, null=True)
    women = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return str(self.college)


class Volleyball(models.Model):
    men = models.IntegerField(blank=True, null=True)
    women = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return str(self.college)


class BasketBall(models.Model):
    men = models.IntegerField(blank=True, null=True)
    women = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return str(self.college)


class Badminton(models.Model):
    men = models.IntegerField(blank=True, null=True)
    women = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return str(self.college)


class Football(models.Model):
    men = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return str(self.college)


class Tennis(models.Model):
    men = models.IntegerField(blank=True, null=True)
    women = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return str(self.college)


class Kabaddi(models.Model):
    women = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return str(self.college)


class Gym(models.Model):
    weightLifting = models.IntegerField(blank=True, null=True)
    powerLifting = models.IntegerField(blank=True, null=True)
    bestPhysique = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return str(self.college)


class Chess(models.Model):
    men = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return str(self.college)


class Member(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    mobile = models.CharField('Mobile No.',default='',max_length=11)
    email_id = models.CharField('Email-id',max_length=200)
    bad = models.ForeignKey(Badminton, blank=True, null=True)
    cri = models.ForeignKey(Cricket, blank=True, null=True)
    bas = models.ForeignKey(BasketBall, blank=True, null=True)
    che = models.ForeignKey(Chess, blank=True, null=True)
    foo = models.ForeignKey(Football, blank=True, null=True)
    vol = models.ForeignKey(Volleyball, blank=True, null=True)
    gym = models.ForeignKey(Gym, blank=True, null=True)
    tab = models.ForeignKey(TableTennis, blank=True, null=True)
    ten = models.ForeignKey(Tennis, blank=True, null=True)
    kab = models.ForeignKey(Kabaddi, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)






