import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Case, UserUpvote
from django.contrib.auth.models import User

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

@csrf_exempt
def user_cases_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Not authenticated"}, status=401)
    
    if request.method == "GET":
        active_objs = Case.objects.filter(user=request.user, status="active")
        closed_objs = Case.objects.filter(user=request.user, status="closed")
        # Serialize only the necessary fields: id, title, and charges (assumed to be a list of strings)
        active_list = list(active_objs.values("id", "title", "charges"))
        closed_list = list(closed_objs.values("id", "title", "charges"))
        return JsonResponse({"active": active_list, "closed": closed_list})
    
    return JsonResponse({"error": "Invalid request method."}, status=405)


@csrf_exempt
def add_case_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"status": "error", "message": "Not authenticated"}, status=401)
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON."}, status=400)
        
        title = data.get("title")
        short_description = data.get("short_description")
        full_description = data.get("full_description")
        charges = data.get("charges", [])
        
        if not (title and short_description and full_description):
            return JsonResponse({"status": "error", "message": "Missing required fields."}, status=400)
        
        new_case = Case.objects.create(
            user=request.user,
            title=title,
            short_description=short_description,
            full_description=full_description,
            charges=charges,
            status="active"
        )
        
        new_case.save()
        return JsonResponse({"status": "ok", "case_id": new_case.id})
    
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

@csrf_exempt
def upvote_user_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"status": "error", "message": "Not authenticated"}, status=401)
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON."}, status=400)
        
        target_id = data.get("target_id")
        if not target_id:
            return JsonResponse({"status": "error", "message": "No target specified."}, status=400)
        
        try:
            target_user = User.objects.get(id=target_id)
        except User.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Target user not found."}, status=404)
        
        # Prevent self-upvote if needed (optional)
        if request.user.id == target_user.id:
            # Allow self upvote if you wish; otherwise, uncomment below:
            # return JsonResponse({"status": "error", "message": "Cannot upvote yourself."}, status=400)
            pass
        
        # Check if this voter already upvoted the target
        if UserUpvote.objects.filter(voter=request.user, voted=target_user).exists():
            return JsonResponse({"status": "error", "message": "Already upvoted."}, status=400)
        
        # Create the upvote record
        UserUpvote.objects.create(voter=request.user, voted=target_user)
        
        # Update the karma field on target user's profile.
        target_profile = target_user.userprofile
        target_profile.karma = (target_profile.karma or 0) + 1
        target_profile.save()
        
        return JsonResponse({"status": "ok", "new_karma": target_profile.karma})
    
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)