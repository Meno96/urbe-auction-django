from django.shortcuts import render, redirect
from django_nextjs.render import render_nextjs_page_sync
from django.views.decorators.csrf import csrf_exempt
from accounts.decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token

from .forms import NewUserForm

# View function for sign up page
@csrf_exempt
@unauthenticated_user
def signUpView(request):
    """
    Renders and handles requests to the sign up page

    Parameters:
    - request: HTTP request object

    Returns:
    - HttpResponse object with JSON data or Next.js rendered page
    """

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            messages.success(request, 'Account successfully created.')

            # Format messages to JSON
            messagesData = []
            for message in messages.get_messages(request):
                messageData = {
                    'level': message.level,
                    'message': message.message,
                    'extra_tags': message.tags
                }
                messagesData.append(messageData)

            # Return JSON data with success status and message
            responseData = {
                'success': True,
                'messages': messagesData
            }

            return HttpResponse(json.dumps(responseData), content_type='application/json')

        else:
            for error in form.errors.values():
                messages.error(request, error)
            
            # Format messages to JSON
            messagesData = []
            for message in messages.get_messages(request):
                messageData = {
                    'level': message.level,
                    'message': message.message[0],
                    'extra_tags': message.tags
                }
                messagesData.append(messageData)

            # Return JSON data with error status and message
            responseData = {
                'success': False,
                'messages': messagesData
            }
                

            return HttpResponse(json.dumps(responseData), content_type='application/json')

    # Render Next.js page for GET requests
    return render_nextjs_page_sync(request)

# View function for sign in page
@csrf_exempt
@unauthenticated_user
def signInView(request):
    """
    Renders and handles requests to the sign in page

    Parameters:
    - request: HTTP request object

    Returns:
    - HttpResponse object with JSON data or Next.js rendered page
    """

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        # Authenticate user and log them in
        if user is not None:
            login(request, user)

            # Determine if user is staff or not
            if request.user.is_staff:
                isStaff = True
            else:
                isStaff = False

            # Return JSON data with success status and staff status
            responseData = {
                'success': True,
                'isStaff': isStaff
            }

            return HttpResponse(json.dumps(responseData), content_type='application/json')
        else:
            # Display error message for wrong username or password
            messages.error(request, 'Wrong username or password')

            # Display form errors as error messages
            for error in form.errors.values():
                messages.error(request, error)
            
            # Format messages to JSON
            messagesData = []
            for message in messages.get_messages(request):
                messageData = {
                    'level': message.level,
                    'message': message.message,
                    'extra_tags': message.tags
                }
                messagesData.append(messageData)

            # Return JSON data with error status and message
            responseData = {
                'success': False,
                'messages': messagesData
            }
                
            return HttpResponse(json.dumps(responseData), content_type='application/json')

    # Render Next.js page for GET requests
    return render_nextjs_page_sync(request)

# View function for the logout
@csrf_exempt
def logoutUser(request):
    logout(request)
    return HttpResponse()

# View function to get CSRF Token
def csrf(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})
