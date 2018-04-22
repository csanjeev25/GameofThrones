from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Character(models.Model):
	character_id = models.AutoField(primary_key=True)
	c_name = models.CharField(max_length=22,blank = False)
	c_image = models.ImageField(max_length=1024,blank = False)

	class Meta:
		db_table = u'CHARACTER'
		def __str__(self):
			return(self.name)

class House(models.Model):
	house_id = models.AutoField(primary_key=True)
	h_name = models.CharField(max_length=22)
	h_image = models.ImageField(max_length=1024)
	house_slogan = models.CharField(max_length=100)
	house_leader = models.ForeignKey(Character,related_name = 'characterID')
	leader_successor = models.ForeignKey(Character,related_name = 'characterID2')

	class Meta:
		db_table = u'HOUSE'
		def __str__(self):
			return(self.h_name)

class Battle(models.Model):
	battle_id = models.AutoField(primary_key=True)
	b_name = models.CharField(max_length=22)
	attacker_id	= models.ForeignKey(House,related_name = 'houseID')
	defender_id = models.ForeignKey(House,related_name = 'houseID2')
	attacker_size = models.IntegerField(null=True)
	defender_size = models.IntegerField(null=True)

	def getattacker(self):
		return self.attacker_id.h_name

	def getdefender(self):
		return self.defender_id.h_name

	class Meta:
		db_table = u'BATTLE'
		def __str__(self):
			return(self.b_name)

