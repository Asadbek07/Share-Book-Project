from django.urls import path

from authentication.views import AuthUserDetailView, SignupPageView

urlpatterns = [
    path("<pk>/update", AuthUserDetailView.as_view(), name="user_detail_update"),
    path("", SignupPageView.as_view(), name="signup"),

]