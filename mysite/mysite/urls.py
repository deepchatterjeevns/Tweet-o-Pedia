"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from Home.views import Startpage

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', Startpage, name='Startpage'),
    path('Tweet_Generator/', include('Tweet_Generator.urls')),
    path('Recent_Tweets/', include('RecentTweetSentiment.urls')),
    path('Objective/', include('Objective.urls')),
    path('QuerybasedSentiment/', include('QuerybasedSentiment.urls')),
    path('Trends/',include("TwitterTrends.urls")),
    path('hate_o_meter/',include("hate_o_meter.urls"))

]
