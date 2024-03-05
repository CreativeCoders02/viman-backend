from django.urls import path
from .views import TestView, SlotView,RequestView,LoginView,ProofView

urlpatterns = [
    path('test', TestView.as_view(), name="Test"),
    path('slot', SlotView.as_view(), name="Slot View"),
    path('request', RequestView.as_view(), name="Request View"),
    path('login', LoginView.as_view(), name="Login View"),
    path('proof', ProofView.as_view(), name="Proof View"),
]
