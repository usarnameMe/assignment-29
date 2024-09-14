from django.http import JsonResponse
from .models import User


def user_view(request):
    user_entry = User.objects.latest('id')
    return JsonResponse({
        'first_name': user_entry.first_name,
        'last_name': user_entry.last_name,
        'age': user_entry.age(),
    })
