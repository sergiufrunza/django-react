from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from .paginators import BlogPagination
from django.shortcuts import get_object_or_404


class BlogListCreateAPIView(APIView):
    def get(self, request):
        blogs = Blog.objects.select_related("author").all().order_by('id')
        paginator = BlogPagination()
        result_page = paginator.paginate_queryset(blogs, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogGetPutDeleteAPIView(APIView):
    def get(self, request, id):
        blog = get_object_or_404(Blog.objects.select_related('author').order_by('id'), id=id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        if blog.author != request.user:
            return Response({"error": "Nu ai permisiunea să editezi acest blog."}, status=status.HTTP_403_FORBIDDEN)

        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        if blog.author != request.user:
            return Response({"error": "Nu ai permisiunea să ștergi acest blog."}, status=status.HTTP_403_FORBIDDEN)
        blog.delete()
        return Response({"message": f"Blog-ul {id} a fost șters cu succes."}, status=status.HTTP_200_OK)


class BlogLikeAPIView(APIView):
    def put(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        add = blog.like(request.user)
        return Response({"likes_count": blog.likes_count + add}, status=status.HTTP_200_OK)


