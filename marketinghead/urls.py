from django.urls import path


from . import views

app_name = 'marketing_head'

urlpatterns = [
    path('collateral/request/', views.collateral_request, name='collateral_request'),
    path('budget/request/', views.budget_request, name='budget_request'),
    
    path('budget/list/', views.BudgetListView.as_view(), name='budget_list'),
    path('budget/create/', views.BudgetCreateView.as_view(), name='budget'),
    path('budget/detail/<int:pk>/', views.BudgetDetailView.as_view(), name='budget_detail'),
    path('budget/update/<int:pk>/', views.BudgetUpdateView.as_view(), name='budget_update'),
    
    
    path('collateral/list/', views.CollateralListView.as_view(), name='collateral_list'),
    path('create/collateral/', views.CollateralCreateView.as_view(), name='create_collateral'),
    path('collateral/detail/<int:pk>/', views.CollateralDetailView.as_view(), name='collateral_detail'),
    path('collateral/edit/<int:pk>/', views.CollateralUpdateView.as_view(), name='collateral_update'),
    
    
    path('assign-quota/', views.CreateAssignQuota.as_view(), name='assign_quota'),
    path('quota/list/', views.AssignQuotaListView.as_view(), name='assign_list'),
    path('quota/<int:pk>/view/', views.AssignQuotaDetailView.as_view(), name='view_quota'),
    path('quota/<int:pk>/edit/', views.AssignQuotaUpdateView.as_view(), name='quota_update'),
    
    
    path('assign-territory/', views.TerritoryAssign.as_view(), name='add_territory'),
    path('territory/list/', views.TerritoryListView.as_view(), name='a_list'),
    path('territory/edit/<int:pk>/', views.TerritoryUpdateView.as_view(), name='a_edit'),
]
