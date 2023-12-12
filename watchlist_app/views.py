# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse

# # Create your views here.
# def movies_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies': list(movies.values())
#     }
#     return JsonResponse(data)

# def movies_details(request, pk):
#     movies = Movie.objects.get(pk=pk)
#     data = {
#         'name': movies.name,
#         'director': movies.director,
#         'description': movies.description
#     }
#     return JsonResponse(data)