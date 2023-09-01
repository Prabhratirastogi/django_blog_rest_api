from .models import Blog
from .serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# Class based views
# GET, POST
class BlogListView(APIView):
    def get(self,request):
        all_blogs = Blog.objects.filter(is_public=True)
        serializer=BlogSerializer(all_blogs, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET, PUT, DELETE
class BlogDetailView(APIView):
    def get(self,request,pk):
        blog = Blog.objects.get(pk=pk)
        serializer=BlogSerializer(blog)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_200_OK)
    
# -------------function based views-----------
# @api_view(['GET','POST'])
# def blog_list(request):
    # if request.method == "GET":
        # all_blogs = Blog.objects.filter(is_public=True)
        # serializer=BlogSerializer(all_blogs, many=True)
        # return Response(serializer.data,status=status.HTTP_200_OK)
#     if request.method == "POST":
        # serializer = BlogSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     # blogs = Blog.objects.all()

#     # data = {
#     #     "Blogs":list(blogs.values())
#     # }
#     # return JsonResponse(data)

    
# @api_view(['GET','PUT','DELETE'])

# def blog_detail(request, pk):
#     if request.method=="GET":
#         blog= Blog.objects.get(is_public=True, pk=pk)
#         serializer=BlogSerializer(blog)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method=="PUT":
#         blog = Blog.objects.get(pk=pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUES)
#     if request.method == "DELETE":
#         blog = Blog.objects.get(pk=pk)
#         blog.delete()
#         return Response(status=status.HTTP_200_OK)
#     # blog = Blog.objects.get(pk=pk)
#     # blog_dict = model_to_dict(blog)

#     # # data = {
#     # #     'name':blogs.name,
#     # #     'description': blogs.description,
#     # #     'slug':blogs.slug,
#     # # }
#     # data = {
#     #     "Blog": blog_dict
#     # }
   
#     # return JsonResponse(data)