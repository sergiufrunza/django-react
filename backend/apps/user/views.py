from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class UserProfileView(LoginRequiredMixin, TemplateView):
    pass


