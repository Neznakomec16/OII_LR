from django.urls import path

from OII_LR.views import index, RequestView_LR_1, CreateCandidateForm_LR_1, LR2View

urlpatterns = [
    path('', index),
    path('lr_1', RequestView_LR_1.as_view(), name='request'),
    path('lr_2', LR2View.as_view(), name='lr_2'),
    path('lr_1/create', CreateCandidateForm_LR_1.as_view(), name='create_candidate'),
]
