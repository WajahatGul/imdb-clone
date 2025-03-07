from django.shortcuts import render
import requests

# API Key for TMDB
tmdb_api_key = "668968f426dbce05b4788b59f1f25cd7"

# 🟢 Fetch and Display Popular Movies OR Search Results
def movie_list(request):
    query = request.GET.get("query", "")
    
    if query:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={tmdb_api_key}&query={query}&language=en-US"
    else:
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={tmdb_api_key}&language=en-US&page=1"
    
    response = requests.get(url)
    movies = response.json().get("results", []) if response.status_code == 200 else []
    
    return render(request, "movie_app/movie.html", {"movies": movies, "query": query})

# 🟢 Fetch and Display Movie Details
def movie_detail(request, movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}&language=en-US"
    response = requests.get(url)
    
    movie = response.json() if response.status_code == 200 else None
    
    return render(request, "movie_app/movie_detail.html", {"movie": movie})
