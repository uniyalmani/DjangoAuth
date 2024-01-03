from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from .models import User
from auth_app.serializers.user_serializer import UserSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
import jwt, datetime



# Function to generate tokens for a user
def get_tokens_for_user(user):
    """
    Generate JWT tokens for a user.

    Parameters:
        user: User object

    Returns:
        dict: Dictionary containing 'refresh' and 'access' tokens.
    """
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# View for user signup
class SignUp(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        """
        Handle GET request for signup page.

        Parameters:
            request: HTTP request object

        Returns:
            HttpResponse: Rendered signup page.
        """
        return render(request, template_name="auth_app/signup.html")

    def post(self, request):
        """
        Handle POST request for user signup.

        Parameters:
            request: HTTP request object

        Returns:
            HttpResponseRedirect: Redirect to the home page on successful signup.
            Redirect to signup page with error message on failure.
        """
        try:
            serializer = UserSerializer(data=request.data)
            response = {}

            if serializer.is_valid():
                user = serializer.save()
                token = get_tokens_for_user(user)

                response = HttpResponseRedirect('/auth/home')
                response['Authorization'] = 'Bearer ' + str(token["refresh"])
                response.set_cookie('jwt', str(token["access"]))

                return response

            messages.error(request, 'Please try again. Email already exists or create an account with a new email.')
            return HttpResponseRedirect('/auth/login')

        except Exception as e:
            messages.error(request, e)
            return  HttpResponseRedirect('/auth/login')

# View for user login
class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handle POST request for user login.

        Parameters:
            request: HTTP request object

        Returns:
            HttpResponseRedirect: Redirect to the home page on successful login.
            Redirect to login page with error message on failure.
        """
        try:
            response = {}
            serializer = UserLoginSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                email = serializer.data.get("email")
                password = serializer.data.get("password")
                user = authenticate(email=email, password=password)

                if user is not None:
                    token = get_tokens_for_user(user)
                    response = HttpResponseRedirect('/auth/home')
                    response.set_cookie('jwt', str(token["access"]))
                    return response

            messages.error(request, 'Wrong email or password. Please try again.')
            return HttpResponseRedirect('/auth/login')

        except Exception as e:
            messages.error(request, e)
            return HttpResponseRedirect('/auth/login')

    def get(self, request):
        """
        Handle GET request for login page.

        Parameters:
            request: HTTP request object

        Returns:
            HttpResponse: Rendered login page.
        """
        if request.info["valid"]:
            messages.error(request, 'Already logged in.')
            return redirect('/auth/home')

        return render(request, template_name="auth_app/login.html")
    

# View for user logout
def logout(request):
    """
    Handle user logout.

    Parameters:
        request: HTTP request object

    Returns:
        HttpResponseRedirect: Redirect to login page on successful logout.
    """
    response = HttpResponseRedirect('/auth/login')
    response.delete_cookie('jwt')
    return response

# View for the home page
def home(request):
    """
    Handle GET request for the home page.

    Parameters:
        request: HTTP request object

    Returns:
        HttpResponse: Rendered home page.
    """
    return render(request, template_name="auth_app/home.html")

# View for user profile
def profile(request):
    """
    Handle GET request for the user profile page.

    Parameters:
        request: HTTP request object

    Returns:
        HttpResponse: Rendered user profile page.
    """
    if not request.info["valid"]:
        messages.error(request, 'Please login.')
        return redirect('/auth/login')

    return render(request, template_name="auth_app/profile.html")