from django.http import JsonResponse, HttpResponse
from .models import Calendar


def calendar_view(request):
    try:
        calendar_entry = Calendar.objects.latest('id')
        return JsonResponse({
            'year': calendar_entry.year,
            'month': calendar_entry.month,
            'day': calendar_entry.day,
        })
    except Calendar.DoesNotExist:
        return JsonResponse({'error': 'No calendar entries found.'}, status=404)
