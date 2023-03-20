from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Blog
from django.http import JsonResponse
from PIL import Image
import io
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .serializers import BlogSerializer


class BlogCreateView(APIView):
    def post(self, request):
        title = request.data.get("title")
        slug = request.data.get("slug")
        cover_img = request.data.get("cover_img")
        content = request.data.get("content")
        author_name = request.data.get("author_name")
        author_description = request.data.get("author_description")

        # Check if all fields are provided
        if not all([title, slug, cover_img, content, author_name, author_description]):
            return JsonResponse({"success": False, 'message':"some detailsl are missing"})

        # Validate image file type
        if not cover_img.content_type in ['image/png', 'image/jpeg']:
            return JsonResponse({"success": False, "message": "Only PNG and JPEG formats are allowed for cover image"})

        # Save Blog object in database
        try:
            image = Image.open(io.BytesIO(cover_img.read()))  # Open image file using PIL library
            blog = Blog(
                title=title,
                slug=slug,
                cover_img=cover_img,
                content=content,
                author_name=author_name,
                author_description=author_description
            )
            blog.save()
            return JsonResponse({"success": True, "message": "Blog saved successfully"})
        except Exception as e:
            return JsonResponse({"success": False, "message": "Error"})


class GetBlogDataAPI(APIView):
    def get(self, request):
        data = Blog.objects.filter().order_by("-created_at")
        context = dict()
        context['data'] = BlogSerializer(data, many=True).data
        return JsonResponse(context)



class ObtainAuthToken(APIView):
    """
    API View that receives a POST with a user's username and password.
    Returns a token that can be used for authenticated requests.
    """
    # authentication_classes = []
    # permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        # Get the username and password from the request data
        # username = request.data.get('username')
        username = 'gourav'
        # password = request.data.get('password')
        password = 'gourav'

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user:
            print("user", user)
            # If the user is authenticated, generate a token and return it
            token, created = Token.objects.get_or_create(user=user)
            print("token", token)
            print("token.key", token.key)
            return Response({'token': token.key})
        else:
            # If the user is not authenticated, return an error message
            return Response({'error': 'Invalid credentials'}, status=400)


from django.http import JsonResponse
from django.middleware.csrf import get_token

def csrf_token_view(request):
    token = get_token(request)
    print("token", token)
    response = JsonResponse({'csrftoken': token})
    response['Access-Control-Allow-Origin'] = '*'
    return response
