from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('api/block_account/', views.get_block_account, name='block_account'),
    path('api/latest_hash/', views.get_latest_hash, name='latest_hash'),
    path('api/bc_per_block/', views.get_bc_per_block, name='bc_per_block'),
    path('api/difficulty/', views.get_difficulty, name='get_difficulty'),
    path('api/total_bc/', views.get_total_bc, name='get_total_bc'),
    path('api/probablity/', views.get_probablity, name='get_probablity'),
    path('api/hash_to_win/', views.get_hash_to_win, name='get_hash_to_win'),
    path('api/next_re_target/', views.get_next_re_target, name='get_next_re_target'),
    path('api/unconfirmed_count/', views.get_unconfirmed_count, name='get_unconfirmed_count'),
    path('api/market_cap/', views.get_market_cap, name='get_market_cap'),
    path('api/stats/', views.get_stats, name='get_stats'),
    path('api/24_hour_btcsent/', views.get_24_hour_btcsent, name='get_24_hour_btcsent'),
]
