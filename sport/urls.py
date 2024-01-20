from django.urls import path, include
from . import views
from sport.views import AdsView

urlpatterns = [
    path('', views.home, name = "home"),
    path('blog/', include("blogApp.urls")),
    path('home/', views.home, name = "home"),
    path('app/', views.app, name = "app"),
    path('twitter/', views.twitter, name = "twitter"),
    path('facebook/', views.facebook, name = "facebook"),
    path('history/', views.results, name = "history"),
    path('jackpot/', views.jackpot, name = "jackpot"),
    path('payment/', views.payment, name = "payment"),
    path('pricing/', views.price, name = "price"),
    path('viptips/', views.viptips, name = "viptips"),
    path('signup/', views.signup, name = "signup"),
    path('singlebet/', views.singlebet, name = "singlebet"),
    path('Popular_Websites_that_Provide_Reliable_Football_Predictions/', views.Popular_Websites_that_Provide_Reliable_Football_Predictions, name = "Popular_Websites_that_Provide_Reliable_Football_Predictions"),
    path('viptipsgames/', views.viptipsgames, name = "viptips"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ads.txt/', AdsView.as_view()),
]
