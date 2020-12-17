from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from .models import (
	CharacterSheet,
	Role,
	Equipment,
	Stat,
	Growth
)
from .utils import cap_stats_comparison

# Create your views here.
def charSheet(request):
	context = {
		'characters': CharacterSheet.objects.all().order_by('name')
	}
	return render(request, 'charsheet/charsheet.html', context)
	# return HttpResponse('<h1>Blog Home</h1>')

# Get views - Character Information, User-filtered Equipment and Character Details, Equipment Information
class CharListView(ListView):
	model = CharacterSheet
	template_name = 'charsheet/charsheet.html'
	context_object_name = 'characters'
	ordering = ['name']

class UserCharListView(ListView):
	model = CharacterSheet
	template_name = 'charsheet/charsheet.html'
	context_object_name = 'characters'
	ordering = ['name']

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return CharacterSheet.objects.filter(user = user)

class CharDetailView(DetailView):
	model = CharacterSheet

class EquipmentDetailView(DetailView):
	model = Equipment

class StatDetailView(DetailView):
	model = Stat

class GrowthDetailView(DetailView):
	model = Growth

# Create views - New Character Sheet, New Equipment, New Stats, New Growths
class CharCreateView(LoginRequiredMixin, CreateView):
	model = CharacterSheet
	fields = ['name', 'level', 'origin', 'affinity', 'boon', 'bane', 'role']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EquipmentCreateView(LoginRequiredMixin, CreateView):
	model = Equipment
	fields = ['rp_name', 'bot_name', 'prf', 'weapon_type', 'subtype', 'rank', 
					'might', 'weight', 'hit', 'crit', 'rng_min', 'rng_max', 'uses', 
					'block', 'block_dr', 'other', 'epithet']

	def form_valid(self, form):
		form.instance.owner = CharacterSheet.objects.get(pk = self.kwargs['pk'])
		return super().form_valid(form)

class StatCreateView(LoginRequiredMixin, CreateView):
	model = Stat
	fields = ['hp', 'strength', 'magic', 'skill', 'speed', 'luck', 'defense', 'resistance', 'constitution']

	def form_valid(self, form):
		owner = CharacterSheet.objects.get(pk=self.kwargs['pk'])
		form.instance.owner = owner

		cap_stats_comparison(owner.role.name, form.instance)
		return super().form_valid(form)

class GrowthCreateView(LoginRequiredMixin, CreateView):
	model = Growth
	fields = ['hp', 'strength', 'magic', 'skill', 'speed', 'luck', 'defense', 'resistance', 'constitution']

	def form_valid(self, form):
		form.instance.owner = CharacterSheet.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)

# Update views - Update Character Sheet, Update Equipment, Update Stats, Update Growths
class CharUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = CharacterSheet
	fields = ['name', 'level', 'origin', 'affinity', 'boon', 'bane', 'role']

	def form_valid(self, form):
		# Do some stat updating
		return super().form_valid(form)

	# Validates that the logged in user is the one who created the post
	def test_func(self):
		sheet = self.get_object()
		return self.request.user == sheet.user

class EquipmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Equipment
	fields = ['rp_name', 'bot_name', 'prf', 'weapon_type', 'subtype', 'rank', 
					'might', 'weight', 'hit', 'crit', 'rng_min', 'rng_max', 'uses', 
					'block', 'block_dr', 'other', 'epithet']

	def form_valid(self, form):
		return super().form_valid(form)

	def test_func(self):
		equipment = self.get_object()
		return self.request.user == equipment.owner.user

class StatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Stat
	fields = ['hp', 'strength', 'magic', 'skill', 'speed', 'luck', 'defense', 'resistance', 'constitution']

	def form_valid(self, form):
		cap_stats_comparison(form.instance.owner.role.name, form.instance)
		return super().form_valid(form)

	def test_func(self):
		stat = self.get_object()
		return self.request.user == stat.owner.user

class GrowthUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Growth
	fields = ['hp', 'strength', 'magic', 'skill', 'speed', 'luck', 'defense', 'resistance', 'constitution']

	def form_valid(self, form):
		return super().form_valid(form)

	def test_func(self):
		growth = self.get_object()
		return self.request.user == growth.owner.user

# Delete views - Delete Character Sheet, Delete Equipment
class CharDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = CharacterSheet
	success_url = '/'

	def test_func(self):
		sheet = self.get_object()
		return self.request.user == sheet.user

class EquipmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Equipment
	
	def get_success_url(self):
		sheet = self.object.owner
		return reverse_lazy('character-sheet-detail', kwargs={'pk': sheet.id})

	def test_func(self):
		equipment = self.get_object()
		return self.request.user == equipment.owner.user