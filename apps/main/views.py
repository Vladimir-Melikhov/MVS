import json
import urllib.request
import urllib.parse

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from .models import ProjectsModel


@method_decorator(ensure_csrf_cookie, name='dispatch')
class MainListView(ListView):
    model = ProjectsModel
    template_name = 'main/main_page.html'
    context_object_name = 'object_list'
    paginate_by = 12

    def get_queryset(self):
        return ProjectsModel.objects.filter(is_active=True)


@require_POST
def contact_send(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        data = request.POST

    name = (data.get('name') or '').strip()
    email = (data.get('email') or '').strip()
    message = (data.get('message') or '').strip()

    if not name or not email or not message:
        return JsonResponse({'ok': False, 'error': 'all fields required'}, status=400)

    token = getattr(settings, 'TELEGRAM_BOT_TOKEN', '')
    chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', '')

    if not token or not chat_id:
        return JsonResponse({'ok': False, 'error': 'telegram not configured'}, status=500)

    text = (
        'NEW CONTACT // mvs-dev\n\n'
        f'NAME: {name}\n'
        f'EMAIL: {email}\n\n'
        f'MESSAGE:\n{message}'
    )

    try:
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        payload = urllib.parse.urlencode({'chat_id': chat_id, 'text': text}).encode('utf-8')
        req = urllib.request.Request(url, data=payload)
        urllib.request.urlopen(req, timeout=10)
    except Exception:
        return JsonResponse({'ok': False, 'error': 'send failed'}, status=500)

    return JsonResponse({'ok': True})
