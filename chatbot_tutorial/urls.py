"""chatbot_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import chat,loginpage,signup,logoutpg,showcount

urlpatterns = [
	url(r'^chat/', chat, name='chat'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', loginpage,name = 'loginpage'),
    url(r'^signup/', signup,name = 'signup'),
    url(r'^logout/',logoutpg,name = 'logoutpg'),
    url(r'^showcount/$',showcount,name = 'showcount')

]
