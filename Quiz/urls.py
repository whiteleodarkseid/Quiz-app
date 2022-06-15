"""Quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from core.views import fail2, index, question, role,fail_auth, question2, question3, question4, question5, question10,  question6, question7, question8, question9, result,  legend,result 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index' ),
    path('question/<user_id>/', question, name='question' ),
    path('question2/<user_id>/', question2, name='question2' ),
    path('question3/<user_id>/', question3, name='question3' ),
    path('question4/<user_id>/', question4, name='question4' ),
    path('question5/<user_id>/', question5, name='question5' ),
    path('question6/<user_id>/', question6, name='question6' ),
    path('question7/<user_id>/', question7, name='question7' ),
    path('question8/<user_id>/', question8, name='question8' ),
    path('question9/<user_id>/', question9, name='question9' ),
    path('question10/<user_id>/', question10, name='question10' ),
    path('role/<user_id>/', role, name='role' ),
    path('fail/', fail_auth, name='fail_auth'),
    path('fail2/', fail2, name='fail2'),
    path('legend/', legend, name='legend'),
    path('resut/<user_id>/', result, name='result'),
]
