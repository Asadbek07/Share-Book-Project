from django.urls import path

from authentication.views import AuthUserDetailView, SignupPageView, UserDetailPage

urlpatterns = [
    path("<int:pk>/update", AuthUserDetailView.as_view(), name="user_detail_update"),
    path("<int:pk>/", UserDetailPage.as_view(), name="user_detail"),
    path("", SignupPageView.as_view(), name="signup"),

]