from .models import CharacterSheet, Role, Stat

def cap_stats_comparison (role, stats):
	caps = Role.objects.filter(name = role).values(
		'hp', 'strength', 'magic', 'skill', 'speed', 'luck', 'defense', 'resistance', 'constitution'
	)
	caps = caps[0]
	stats.hp = caps["hp"] if caps["hp"] < stats.hp else stats.hp
	stats.strength = caps["strength"] if caps["strength"] < stats.strength else stats.strength
	stats.magic = caps["magic"] if caps["magic"] < stats.magic else stats.magic
	stats.skill = caps["skill"] if caps["skill"] < stats.skill else stats.skill
	stats.speed = caps["speed"] if caps["speed"] < stats.speed else stats.speed
	stats.luck = caps["luck"] if caps["luck"] < stats.luck else stats.luck
	stats.defense = caps["defense"] if caps["defense"] < stats.defense else stats.defense
	stats.resistance = caps["resistance"] if caps["resistance"] < stats.resistance else stats.resistance
	stats.constitution = caps["constitution"] if caps["constitution"] < stats.constitution else stats.constitution