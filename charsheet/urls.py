from django.urls import path
from . import views
from .views import (
	CharListView,
	UserCharListView,
	CharDetailView,
	EquipmentDetailView,
	StatDetailView,
	GrowthDetailView,
	CharCreateView,
	EquipmentCreateView,
	StatCreateView,
	GrowthCreateView,
	CharUpdateView,
	EquipmentUpdateView,
	StatUpdateView,
	GrowthUpdateView,
	CharDeleteView,
	EquipmentDeleteView
)

urlpatterns = [
	path('', CharListView.as_view(), name='character-sheet'),
	path('usersheets/<str:username>', UserCharListView.as_view(), name='user-characters'),
	path('sheet/<int:pk>/', CharDetailView.as_view(), name='character-sheet-detail'),
	path('sheet/new/', CharCreateView.as_view(), name='character-sheet-create'),
	path('sheet/<int:pk>/update/', CharUpdateView.as_view(), name='character-sheet-update'),
	path('sheet/<int:pk>/delete/', CharDeleteView.as_view(), name='character-sheet-delete'),

	path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
	path('equipment/<int:pk>/new', EquipmentCreateView.as_view(), name='equipment-create'),
	path('equipment/<int:pk>/update/', EquipmentUpdateView.as_view(), name='equipment-update'),
	path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name='equipment-delete'),
	
	path('stat/<int:pk>', StatDetailView.as_view(), name='stat-detail'),
	path('stat/<int:pk>/new/', StatCreateView.as_view(), name='stat-create'),
	path('stat/<int:pk>/update/', StatUpdateView.as_view(), name='stat-update'),
	
	path('growth/<int:pk>', GrowthDetailView.as_view(), name='growth-detail'),
	path('growth/<int:pk>/new/', GrowthCreateView.as_view(), name='growth-create'),
	path('growth/<int:pk>/update/', GrowthUpdateView.as_view(), name='growth-update'),
]