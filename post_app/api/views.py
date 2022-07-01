import json
import logging
from typing import Any

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer

# Create your views here.
logger = logging.getLogger("post_app")


@api_view(['GET'])
@csrf_exempt
def welcome() -> JsonResponse:
    content = {"message": "Welcome to the Post App!"}
    return JsonResponse(content)


@api_view(['POST'])
@csrf_exempt
def add_post(request: Any) -> JsonResponse:
    """
    Add post.
    """
    data = json.loads(json.dumps(request.data))

    name = data.get("name")
    content = data.get("content")
    email = data.get("email")

    if not name or not content or not email:
        return JsonResponse(
            {"error": "Required parameters are missing"},
            safe=False,
            status=status.HTTP_406_NOT_ACCEPTABLE
        )

    if email:
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse(
                {"error": "Invalid email"},
                safe=False,
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

    try:
        post = Post.objects.create(name=name, content=content, email=email)
        serializer = PostSerializer(post)

        return JsonResponse(
            {'posts': serializer.data},
            safe=False,
            status=status.HTTP_201_CREATED
        )

    except IntegrityError:
        return JsonResponse(
            {'error': "Post already exists"},
            safe=False,
            status=status.HTTP_400_BAD_REQUEST
        )

    except Exception as exc:
        logger.error(exc)
        return JsonResponse(
            {'error': "An error has occurred"},
            safe=False,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
@csrf_exempt
def get_posts(request: Any = None, last_id: int = 0) -> JsonResponse:
    """
    Get paginated posts.
    """
    posts = Post.objects.filter(
        id__gt=last_id
    ).order_by("-likes").values()[:10]

    return JsonResponse(
        {'posts': list(posts)},
        safe=False,
        status=status.HTTP_200_OK
    )


@api_view(['PUT'])
@csrf_exempt
def like_post(request: Any = None, post_id: int = None) -> JsonResponse:
    """
    Like post.
    """
    try:
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
        serializer = PostSerializer(post)
        return JsonResponse(
            {"post": serializer.data},
            safe=False,
            status=status.HTTP_200_OK
        )

    except ObjectDoesNotExist:
        return JsonResponse(
            {"error": "Post not found"},
            safe=False,
            status=status.HTTP_404_NOT_FOUND
        )

    except Exception as exc:
        logger.error(exc)
        return JsonResponse(
            {"error": "An error has occurred"},
            safe=False,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['PUT'])
@csrf_exempt
def dislike_post(request: Any = None, post_id: int = None) -> JsonResponse:
    """
    Dislike post.
    """
    try:
        post = Post.objects.get(id=post_id)
        post.dislikes += 1
        post.save()
        serializer = PostSerializer(post)
        return JsonResponse(
            {"post": serializer.data},
            safe=False,
            status=status.HTTP_200_OK
        )

    except ObjectDoesNotExist:
        return JsonResponse(
            {"error": "Post not found"},
            safe=False,
            status=status.HTTP_404_NOT_FOUND
        )

    except Exception as exc:
        logger.error(exc)
        return JsonResponse(
            {"error": "An error has occurred"},
            safe=False,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
