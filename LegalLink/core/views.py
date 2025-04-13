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

@csrf_exempt
def user_profile_update_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Not logged in"}, status=401)

    user = request.user
    profile = user.userprofile

    if request.method == "GET":
        data = {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": profile.age,
            "gender": profile.gender,
            "city": profile.city,
            "state": profile.state,
            "is_helper": profile.is_helper,
            "karma": profile.karma,  # Karma is returned, but not editable
            "contact_info": profile.contact_info,
            "avatar": profile.avatar.url if profile.avatar else None,
        }
        return JsonResponse(data)

    elif request.method == "POST":
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)

        # Update User model fields
        user.first_name = payload.get("first_name", user.first_name)
        user.last_name = payload.get("last_name", user.last_name)
        user.save()

        # Update UserProfile fields (EXCEPT karma)
        profile.age = payload.get("age", profile.age)
        profile.gender = payload.get("gender", profile.gender)
        profile.city = payload.get("city", profile.city)
        profile.state = payload.get("state", profile.state)
        profile.is_helper = payload.get("is_helper", profile.is_helper)
        profile.contact_info = payload.get("contact_info", profile.contact_info)
        # Ignore any attempt to update karma by the user.
        profile.save()

        return JsonResponse({"status": "ok"})

    return JsonResponse({"error": "Invalid request method."}, status=400)

@csrf_exempt
def update_avatar_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"status": "error", "message": "Not authenticated"}, status=401)
    if request.method == "POST":
        if 'avatar' not in request.FILES:
            return JsonResponse({"status": "error", "message": "No avatar file provided."}, status=400)
        avatar_file = request.FILES['avatar']
        profile = request.user.userprofile
        profile.avatar = avatar_file
        profile.save()
        return JsonResponse({"status": "ok", "avatar": profile.avatar.url})
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)