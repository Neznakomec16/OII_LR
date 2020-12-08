"""OII URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from OII_LR.views import index, RequestView_LR_1, CreateCandidateForm_LR_1, LR2View

urlpatterns = [
    path('', index),
    path('lr_1', RequestView_LR_1.as_view(), name='request'),
    path('lr_2', LR2View.as_view(), name='lr2_main'),
    path('lr_1/create', CreateCandidateForm_LR_1.as_view(), name='create_candidate'),
]
