from django.urls import path
from .views import SlotView, RequestView, LoginView, ProofView, RoomView

urlpatterns = [
    path('slot', SlotView.as_view(), name="Slot View"),
    path('request', RequestView.as_view(), name="Request View"),
    path('login', LoginView.as_view(), name="Login View"),
    path('proof', ProofView.as_view(), name="Proof View"),
    path('room', RoomView.as_view(), name="Room View"),
]
