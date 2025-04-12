import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def profile_setup_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required.'}, status=403)

    if request.method == 'GET':
        # Return current user profile info
        user = request.user
        profile = user.userprofile  # changed from user.profile
        return JsonResponse({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'age': profile.age,
            'gender': profile.gender,
            'city': profile.city,
            'state': profile.state,
        })

    elif request.method == 'POST':
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)

        # Update user fields
        user = request.user
        user.first_name = payload.get('first_name', '')
        user.last_name = payload.get('last_name', '')
        user.save()

        # Update related profile
        profile = user.userprofile  # changed from user.profile
        profile.age = payload.get('age')
        profile.gender = payload.get('gender', profile.gender)
        profile.city = payload.get('city', '')
        profile.state = payload.get('state', '')
        profile.save()

        return JsonResponse({'status': 'ok'})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)