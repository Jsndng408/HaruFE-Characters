from django.apps import apps
CharSheetModel = apps.get_model('charsheet', 'CharacterSheet')

def message_processor(request):
	return {
		'character_sheets': CharSheetModel.objects.all().order_by('name')
	}