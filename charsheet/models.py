from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Role(models.Model):
	name = models.CharField(max_length = 64)
	promoted = models.BooleanField(default = False)
	hp = models.IntegerField(default = 0)
	strength = models.IntegerField(default = 0)
	magic = models.IntegerField(default = 0)
	skill = models.IntegerField(default = 0)
	speed = models.IntegerField(default = 0)
	luck = models.IntegerField(default = 0)
	defense = models.IntegerField(default = 0)
	resistance = models.IntegerField(default = 0)
	constitution = models.IntegerField(default = 0)

	def __str__(self):
		return self.name

class CharacterSheet(models.Model):
	STATS = [
		('HP', 'HP'),
        ('STR', 'STRENGTH'),
        ('MAG', 'MAGIC'),
        ('SKL', 'SKILL'),
        ('SPD', 'SPEED'),
        ('LCK', 'LUCK'),
        ('DEF', 'DEFENSE'),
        ('RES', 'RESISTANCE'),
        ('CON', 'CONSTITUTION'),
	]
	AFFINITIES = [
		('FI', 'FIRE'),
    	('WA', 'WATER'),
    	('EA', 'EARTH'),
    	('WI', 'WIND'),
    	('TH', 'THUNDER'),
    	('IC', 'ICE'),
    	('LI', 'LIGHT'),
    	('DA', 'DARK'),
    	('VO', 'VOID'),
    ]
	name = models.CharField(max_length = 32)
	level = models.IntegerField()
	origin = models.CharField(max_length = 32)
	affinity = models.CharField(max_length=2, choices=AFFINITIES)
	boon = models.CharField(max_length=3, choices=STATS)
	bane = models.CharField(max_length=3, choices=STATS)
	date_created = models.DateField(default=timezone.now)
	role = models.ForeignKey(Role, on_delete=models.CASCADE)
	user = models.ForeignKey(User, related_name="User", null=True, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name + ", Level " + str(self.level) + " " + self.role.name

	def get_absolute_url(self):
		return reverse('character-sheet-detail', kwargs={'pk': self.pk})

class Equipment(models.Model):
	TYPES = [
		('SW', 'Sword'),
		('LA', 'Lance'),
		('AX', 'Axe'),
		('BO', 'Bow'),
		('FI', 'Fire'),
		('TH', 'Thunder'),
		('WI', 'Wind'),
		('LI', 'Light'),
		('DA', 'Dark'),
		('ST', 'Staff'),
		('DS', 'Dragonstone'),
		('DG', 'Dagger'),
		('TO', 'Tool'),
		('OH', 'Offhand'),
		('SH', 'Shield'),
		('CH', 'Charm'),
		('RI', 'Ring'),
		('EQ', 'Equipment'),
		('NO', 'None'),
	]
	RANKS = [
		('S', 'S'),
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
		('D', 'D'),
		('E', 'E'),
	]
	rp_name = models.CharField(max_length = 64)
	bot_name = models.CharField(max_length = 128)
	prf = models.BooleanField(default=False)
	weapon_type = models.CharField(max_length=2, choices=TYPES)
	subtype = models.CharField(max_length=2, choices=TYPES)
	rank = models.CharField(max_length=1, choices=RANKS)
	might = models.IntegerField(default = -256)
	weight = models.IntegerField(default = -256)
	hit = models.IntegerField(default = -256)
	crit = models.IntegerField(default = -256)
	rng_min = models.IntegerField(default = 0)
	rng_max = models.IntegerField(default = 0)
	uses = models.PositiveIntegerField(default = 0)
	block = models.IntegerField(default = -256)
	block_dr = models.IntegerField(default = -256)
	other = models.TextField(blank=True, default='')
	epithet = models.TextField(blank=True, default='')
	owner = models.ForeignKey(CharacterSheet, on_delete=models.CASCADE)

	def __str__(self):
		return self.rp_name

	def get_absolute_url(self):
		return reverse('equipment-detail', kwargs={'pk': self.pk})

class Stat(models.Model):
	hp = models.IntegerField(default = 0)
	strength = models.IntegerField(default = 0)
	magic = models.IntegerField(default = 0)
	skill = models.IntegerField(default = 0)
	speed = models.IntegerField(default = 0)
	luck = models.IntegerField(default = 0)
	defense = models.IntegerField(default = 0)
	resistance = models.IntegerField(default = 0)
	constitution = models.IntegerField(default = 0)
	owner = models.OneToOneField(CharacterSheet, related_name='stat_set', on_delete=models.CASCADE)

	def __str__(self):
		return self.owner.name + " - Stats"

	def get_absolute_url(self):
		return reverse('stat-detail', kwargs={'pk': self.pk})

class Growth(models.Model):
	hp = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
	strength = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
	magic = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
	skill = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
	speed = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
	luck = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
	defense = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
	resistance = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
	constitution = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
	owner = models.OneToOneField(CharacterSheet, related_name='growth_set', on_delete=models.CASCADE)

	def __str__(self):
		return self.owner.name + " - Growths"

	def get_absolute_url(self):
		return reverse('growth-detail', kwargs={'pk': self.pk})