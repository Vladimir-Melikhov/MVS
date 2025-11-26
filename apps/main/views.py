from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import ProjectsModel


@method_decorator(cache_page(60 * 15), name='dispatch')
class MainListView(ListView):
    model = ProjectsModel
    template_name = 'main/main_page.html'
    context_object_name = 'object_list'
    paginate_by = 12
    
    def get_queryset(self):
        return ProjectsModel.objects.filter(
            is_active=True
        ).select_related().prefetch_related()