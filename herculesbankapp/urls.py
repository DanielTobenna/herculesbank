from django.urls import path

from . import views

urlpatterns=[
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('contact/', views.contact, name='contact'),
 path('news/', views.news, name='news'),
 path('dashboard/', views.dashboard, name='dashboard'),
 path('account_settings/', views.account_settings, name='account_settings'),
 path('fundtransfer/', views.fundtransfer, name='fundtransfer'),
 path('foreign_transaction/', views.foreign_transaction, name='foreign_transaction'),
 path('transactionhistory/', views.transactionhistory, name='transactionhistory'),
 path('admindashboard/', views.admindashboard, name='admindashboard'),
 path('admincreateaccount/', views.admincreateaccount, name='admincreateaccount'),
 path('admingotouserprofile/<str:pk>/', views.admingotouserprofile, name='admingotouserprofile'),
 path('admincreditaccount/<str:pk>/', views.admincreditaccount, name='admincreditaccount'),
 path('admindebitaccount/<str:pk>/', views.admindebitaccount, name='admindebitaccount'),
 path('clientsignin/', views.clientsignin, name='clientsignin'),
 path('logout/', views.logoutuser, name='logout'),
]