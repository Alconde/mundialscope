from django.views.generic import TemplateView
from matches.dashboard_services import get_dashboard_context


class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_dashboard_context())
        return context