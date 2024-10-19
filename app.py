from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Define the functions for each SWAIG endpoint
import requests

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"

def call_tmdb_api(endpoint, params):
    url = f"{TMDB_BASE_URL}{endpoint}"
    params['api_key'] = TMDB_API_KEY
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

def search_movie(query, language="en-US"):
    endpoint = "/search/movie"
    params = {"query": query, "language": language}
    response = call_tmdb_api(endpoint, params)
    
    # Format the results if the response is successful
    if 'results' in response:
        return format_movie_search_results(response['results'])
    
    return response

def format_movie_search_results(results):
    formatted_results = []
    for movie in results:
        formatted_results.append(
            f"id: {movie['id']}\n"
            f"title: {movie['title']}\n"
            f"release_date: {movie['release_date']}\n"
            f"overview: {movie['overview']}\n"
            f"vote_average: {movie['vote_average']}\n"
            f"vote_count: {movie['vote_count']}\n"
            f"popularity: {movie['popularity']}\n"
            f"genre_ids: {', '.join(map(str, movie['genre_ids']))}\n"
            f"original_language: {movie['original_language']}\n"
            f"poster_path: {movie['poster_path']}\n"
            f"backdrop_path: {movie['backdrop_path']}\n"
            f"adult: {'Yes' if movie['adult'] else 'No'}\n"
            "----------------------------------------\n"
        )
    return "\n".join(formatted_results)

def get_movie_details(movie_id, language="en-US"):
    endpoint = f"/movie/{movie_id}"
    params = {"language": language}
    response = call_tmdb_api(endpoint, params)
    
    # Format the response if successful
    if response and 'id' in response:
        return format_movie_details(response)
    
    return response

def format_movie_details(movie):
    genres = ', '.join(genre['name'] for genre in movie.get('genres', []))
    production_companies = ', '.join(company['name'] for company in movie.get('production_companies', []))
    spoken_languages = ', '.join(language['name'] for language in movie.get('spoken_languages', []))
    
    formatted_details = (
        f"id: {movie['id']}\n"
        f"title: {movie['title']}\n"
        f"original_title: {movie['original_title']}\n"
        f"release_date: {movie['release_date']}\n"
        f"runtime: {movie['runtime']} minutes\n"
        f"overview: {movie['overview']}\n"
        f"vote_average: {movie['vote_average']}\n"
        f"vote_count: {movie['vote_count']}\n"
        f"popularity: {movie['popularity']}\n"
        f"genres: {genres}\n"
        f"original_language: {movie['original_language']}\n"
        f"spoken_languages: {spoken_languages}\n"
        f"production_companies: {production_companies}\n"
        f"budget: ${movie['budget']}\n"
        f"revenue: ${movie['revenue']}\n"
        f"homepage: {movie['homepage']}\n"
        f"status: {movie['status']}\n"
        f"tagline: {movie['tagline']}\n"
        f"poster_path: {movie['poster_path']}\n"
        f"backdrop_path: {movie['backdrop_path']}\n"
        f"adult: {'Yes' if movie['adult'] else 'No'}\n"
        "----------------------------------------\n"
    )
    return formatted_details

def discover_movies(with_genres=None, primary_release_year=None, sort_by="popularity.desc", language="en-US"):
    endpoint = "/discover/movie"
    params = {
        "with_genres": with_genres,
        "primary_release_year": primary_release_year,
        "sort_by": sort_by,
        "language": language
    }
    response = call_tmdb_api(endpoint, params)
    
    # Format the results if the response is successful
    if 'results' in response:
        return format_discover_movies_results(response['results'])
    
    return response

def format_discover_movies_results(results):
    formatted_results = []
    for movie in results:
        formatted_results.append(
            f"id: {movie['id']}\n"
            f"title: {movie['title']}\n"
            f"release_date: {movie['release_date']}\n"
            f"overview: {movie['overview']}\n"
            f"vote_average: {movie['vote_average']}\n"
            f"vote_count: {movie['vote_count']}\n"
            f"popularity: {movie['popularity']}\n"
            f"genre_ids: {', '.join(map(str, movie['genre_ids']))}\n"
            f"original_language: {movie['original_language']}\n"
            f"poster_path: {movie['poster_path']}\n"
            f"backdrop_path: {movie['backdrop_path']}\n"
            f"adult: {'Yes' if movie['adult'] else 'No'}\n"
            "----------------------------------------\n"
        )
    return "\n".join(formatted_results)

def get_trending_movies(time_window="week", language="en-US"):
    endpoint = f"/trending/movie/{time_window}"
    params = {"language": language}
    response = call_tmdb_api(endpoint, params)
    
    # Format the results if the response is successful
    if 'results' in response:
        return format_trending_movies_results(response['results'])
    
    return response

def format_trending_movies_results(results):
    formatted_results = []
    for movie in results:
        formatted_results.append(
            f"id: {movie['id']}\n"
            f"title: {movie['title']}\n"
            f"original_title: {movie['original_title']}\n"
            f"release_date: {movie['release_date']}\n"
            f"overview: {movie['overview']}\n"
            f"vote_average: {movie['vote_average']}\n"
            f"vote_count: {movie['vote_count']}\n"
            f"popularity: {movie['popularity']}\n"
            f"genre_ids: {', '.join(map(str, movie['genre_ids']))}\n"
            f"original_language: {movie['original_language']}\n"
            f"poster_path: {movie['poster_path']}\n"
            f"backdrop_path: {movie['backdrop_path']}\n"
            f"adult: {'Yes' if movie['adult'] else 'No'}\n"
            "----------------------------------------\n"
        )
    return "\n".join(formatted_results)

def get_movie_recommendations(movie_id, language="en-US"):
    endpoint = f"/movie/{movie_id}/recommendations"
    params = {"language": language}
    response = call_tmdb_api(endpoint, params)
    
    # Format the results if the response is successful
    if 'results' in response:
        return format_movie_recommendations_results(response['results'])
    
    return response

def format_movie_recommendations_results(results):
    formatted_results = []
    for movie in results:
        formatted_results.append(
            f"id: {movie['id']}\n"
            f"title: {movie['title']}\n"
            f"original_title: {movie['original_title']}\n"
            f"release_date: {movie['release_date']}\n"
            f"overview: {movie['overview']}\n"
            f"vote_average: {movie['vote_average']}\n"
            f"vote_count: {movie['vote_count']}\n"
            f"popularity: {movie['popularity']}\n"
            f"genre_ids: {', '.join(map(str, movie['genre_ids']))}\n"
            f"original_language: {movie['original_language']}\n"
            f"poster_path: {movie['poster_path']}\n"
            f"backdrop_path: {movie['backdrop_path']}\n"
            f"adult: {'Yes' if movie['adult'] else 'No'}\n"
            "----------------------------------------\n"
        )
    return "\n".join(formatted_results)

def get_genre_list(language="en-US"):
    endpoint = "/genre/movie/list"
    params = {"language": language}
    response = call_tmdb_api(endpoint, params)
    
    # Format the genres if the response is successful
    if 'genres' in response:
        return format_genre_list(response['genres'])
    
    return response

def format_genre_list(genres):
    formatted_genres = []
    for genre in genres:
        formatted_genres.append(
            f"id: {genre['id']}\n"
            f"name: {genre['name']}\n"
            "----------------------------------------\n"
        )
    return "\n".join(formatted_genres)

def get_upcoming_movies(language="en-US", region=None):
    endpoint = "/movie/upcoming"
    params = {"language": language, "region": region}
    response = call_tmdb_api(endpoint, params)
    
    # Format the results if the response is successful
    if 'results' in response:
        return format_upcoming_movies_results(response['results'])
    
    return response

def format_upcoming_movies_results(results):
    formatted_results = []
    for movie in results:
        formatted_results.append(
            f"id: {movie['id']}\n"
            f"title: {movie['title']}\n"
            f"original_title: {movie['original_title']}\n"
            f"release_date: {movie['release_date']}\n"
            f"overview: {movie['overview']}\n"
            f"vote_average: {movie['vote_average']}\n"
            f"vote_count: {movie['vote_count']}\n"
            f"popularity: {movie['popularity']}\n"
            f"genre_ids: {', '.join(map(str, movie['genre_ids']))}\n"
            f"original_language: {movie['original_language']}\n"
            f"poster_path: {movie['poster_path']}\n"
            f"backdrop_path: {movie['backdrop_path']}\n"
            f"adult: {'Yes' if movie['adult'] else 'No'}\n"
            "----------------------------------------\n"
        )
    return "\n".join(formatted_results)

def get_now_playing_movies(language="en-US", region=None):
    endpoint = "/movie/now_playing"
    params = {"language": language, "region": region}
    response = call_tmdb_api(endpoint, params)
    
    # Format the results if the response is successful
    if 'results' in response:
        return format_now_playing_movies_results(response['results'])
    
    return response

def format_now_playing_movies_results(results):
    formatted_results = []
    for movie in results:
        formatted_results.append(
            f"id: {movie['id']}\n"
            f"title: {movie['title']}\n"
            f"original_title: {movie['original_title']}\n"
            f"release_date: {movie['release_date']}\n"
            f"overview: {movie['overview']}\n"
            f"vote_average: {movie['vote_average']}\n"
            f"vote_count: {movie['vote_count']}\n"
            f"popularity: {movie['popularity']}\n"
            f"genre_ids: {', '.join(map(str, movie['genre_ids']))}\n"
            f"original_language: {movie['original_language']}\n"
            f"poster_path: {movie['poster_path']}\n"
            f"backdrop_path: {movie['backdrop_path']}\n"
            f"adult: {'Yes' if movie['adult'] else 'No'}\n"
            "----------------------------------------\n"
        )
    return "\n".join(formatted_results)

def get_similar_movies(movie_id, language="en-US"):
    endpoint = f"/movie/{movie_id}/similar"
    params = {"language": language}
    response = call_tmdb_api(endpoint, params)
    
    # Format the results if the response is successful
    if 'results' in response:
        return format_similar_movies_results(response['results'])
    
    return response

def format_similar_movies_results(results):
    formatted_results = []
    for movie in results:
        formatted_results.append(
            f"id: {movie['id']}\n"
            f"title: {movie['title']}\n"
            f"original_title: {movie['original_title']}\n"
            f"release_date: {movie['release_date']}\n"
            f"overview: {movie['overview']}\n"
            f"vote_average: {movie['vote_average']}\n"
            f"vote_count: {movie['vote_count']}\n"
            f"popularity: {movie['popularity']}\n"
            f"genre_ids: {', '.join(map(str, movie['genre_ids']))}\n"
            f"original_language: {movie['original_language']}\n"
            f"poster_path: {movie['poster_path']}\n"
            f"backdrop_path: {movie['backdrop_path']}\n"
            f"adult: {'Yes' if movie['adult'] else 'No'}\n"
            "----------------------------------------\n"
        )
    return "\n".join(formatted_results)

def multi_search(query, language="en-US", page=1, include_adult=False, region=None):
    endpoint = "/search/multi"
    params = {
        "query": query,
        "language": language,
        "page": page,
        "include_adult": include_adult,
        "region": region
    }
    response = call_tmdb_api(endpoint, params)
    
    # Format the results if the response is successful
    if 'results' in response:
        return format_multi_search_results(response['results'])
    
    return response

def format_multi_search_results(results):
    formatted_results = []
    for item in results:
        if item['media_type'] == 'movie':
            formatted_results.append(
                f"Movie: {item['title']}\n"
                f"Original Title: {item['original_title']}\n"
                f"Release Date: {item['release_date']}\n"
                f"Overview: {item['overview']}\n"
                f"Vote Average: {item['vote_average']}\n"
                f"Vote Count: {item['vote_count']}\n"
                f"Popularity: {item['popularity']}\n"
                f"Genre IDs: {', '.join(map(str, item['genre_ids']))}\n"
                f"Original Language: {item['original_language']}\n"
                f"Poster Path: {item['poster_path']}\n"
                f"Backdrop Path: {item['backdrop_path']}\n"
                f"Adult: {'Yes' if item['adult'] else 'No'}\n"
                "----------------------------------------\n"
            )
        elif item['media_type'] == 'tv':
            formatted_results.append(
                f"TV Show: {item['name']}\n"
                f"Original Name: {item['original_name']}\n"
                f"First Air Date: {item.get('first_air_date', 'N/A')}\n"
                f"Overview: {item['overview']}\n"
                f"Vote Average: {item['vote_average']}\n"
                f"Vote Count: {item['vote_count']}\n"
                f"Popularity: {item['popularity']}\n"
                f"Genre IDs: {', '.join(map(str, item['genre_ids']))}\n"
                f"Original Language: {item['original_language']}\n"
                f"Poster Path: {item['poster_path']}\n"
                f"Backdrop Path: {item['backdrop_path']}\n"
                "----------------------------------------\n"
            )
        elif item['media_type'] == 'person':
            formatted_results.append(
                f"Person: {item['name']}\n"
                f"Known For: {', '.join([known['title'] if 'title' in known else known['name'] for known in item['known_for']])}\n"
                f"Popularity: {item['popularity']}\n"
                f"Known For Department: {item['known_for_department']}\n"
                "----------------------------------------\n"
            )
    return "\n".join(formatted_results)

SWAIG_FUNCTION_SIGNATURES = {
    "search_movie": {
        "web_hook_url": "https://swaig-server.signalwire.me/swaig",
        "purpose": "Search for movies by title",
        "function": "search_movie",
        "argument": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "The movie title to search for."},
                "language": {"type": "string", "description": "Language of the results.", "default": "en-US"},
                "page": {"type": "integer", "description": "Page number for pagination.", "default": 1},
                "include_adult": {"type": "boolean", "description": "Whether to include adult content.", "default": False},
                "region": {"type": "string", "description": "Specify a region to prioritize search results."},
                "year": {"type": "integer", "description": "Filter results by release year."},
                "primary_release_year": {"type": "integer", "description": "Filter results by primary release year."}
            },
            "required": ["query"]
        }
    },
    "get_movie_details": {
        "web_hook_url": "https://swaig-server.signalwire.me/swaig",
        "purpose": "Retrieve detailed information about a movie",
        "function": "get_movie_details",
        "argument": {
            "type": "object",
            "properties": {
                "movie_id": {"type": "integer", "description": "The TMDb ID of the movie."},
                "language": {"type": "string", "description": "Language of the results.", "default": "en-US"},
                "append_to_response": {"type": "string", "description": "Additional requests to append to the result."}
            },
            "required": ["movie_id"]
        }
    },
    "discover_movies": {
        "web_hook_url": "https://swaig-server.signalwire.me/swaig",
        "purpose": "Discover movies by different criteria",
        "function": "discover_movies",
        "argument": {
            "type": "object",
            "properties": {
                "language": {"type": "string", "description": "Language of the results.", "default": "en-US"},
                "region": {"type": "string", "description": "Specify a region to filter release dates."},
                "sort_by": {"type": "string", "description": "Sort results by criteria.", "default": "popularity.desc"},
                "include_adult": {"type": "boolean", "description": "Whether to include adult content.", "default": False},
                "include_video": {"type": "boolean", "description": "Whether to include movies that have a video.", "default": False},
                "page": {"type": "integer", "description": "Page number for pagination.", "default": 1},
                "primary_release_year": {"type": "integer", "description": "Filter movies released in a specific year."},
                "primary_release_date_gte": {"type": "string", "description": "Filter movies released on or after this date (YYYY-MM-DD)."},
                "primary_release_date_lte": {"type": "string", "description": "Filter movies released on or before this date (YYYY-MM-DD)."},
                "with_genres": {"type": "string", "description": "Comma-separated genre IDs to filter by."},
                "with_cast": {"type": "string", "description": "Comma-separated person IDs to filter by cast."},
                "with_crew": {"type": "string", "description": "Comma-separated person IDs to filter by crew."},
                "with_keywords": {"type": "string", "description": "Comma-separated keyword IDs to filter by."},
                "with_runtime_gte": {"type": "integer", "description": "Filter movies with runtime greater than or equal to this value."},
                "with_runtime_lte": {"type": "integer", "description": "Filter movies with runtime less than or equal to this value."}
            },
            "required": []
        }
    },
    "get_trending_movies": {
        "web_hook_url": "https://swaig-server.signalwire.me/swaig",
        "purpose": "Retrieve a list of movies that are currently trending",
        "function": "get_trending_movies",
        "argument": {
            "type": "object",
            "properties": {
                "time_window": {"type": "string", "description": "Time window to fetch trends for ('day' or 'week').", "enum": ["day", "week"], "default": "week"},
                "language": {"type": "string", "description": "Language of the results.", "default": "en-US"},
                "page": {"type": "integer", "description": "Page number for pagination.", "default": 1}
            },
            "required": []
        }
    },
    "get_movie_recommendations": {
        "web_hook_url": "https://swaig-server.signalwire.me/swaig",
        "purpose": "Get recommendations based on a specific movie",
        "function": "get_movie_recommendations",
        "argument": {
            "type": "object",
            "properties": {
                "movie_id": {"type": "integer", "description": "The TMDb ID of the movie."},
                "language": {"type": "string", "description": "Language of the results.", "default": "en-US"},
                "page": {"type": "integer", "description": "Page number for pagination.", "default": 1}
            },
            "required": ["movie_id"]
        }
    },
    "get_genre_list": {
        "web_hook_url": "https://swaig-server.signalwire.me/swaig",
        "purpose": "Retrieve the list of official genres",
        "function": "get_genre_list",
        "argument": {
            "type": "object",
            "properties": {
                "language": {"type": "string", "description": "Language of the results.", "default": "en-US"}
            },
            "required": []
        }
    },
    "get_upcoming_movies": {
        "web_hook_url": "https://swaig-server.signalwire.me/swaig",
        "purpose": "Retrieve a list of upcoming movies",
        "function": "get_upcoming_movies",
        "argument": {
            "type": "object",
            "properties": {
                "language": {"type": "string", "description": "Language of the results.", "default": "en-US"},
                "region": {"type": "string", "description": "Specify a region to filter release dates."}
            },
            "required": []
        }
    },
    "get_now_playing_movies": {
        "web_hook_url": "https://swaig-server.signalwire.me/swaig",
        "purpose": "Retrieve a list of movies currently playing in theaters",
        "function": "get_now_playing_movies",
        "argument": {
            "type": "object",
            "properties": {
                "language": {"type": "string", "description": "Language of the results.", "default": "en-US"},
                "region": {"type": "string", "description": "Specify a region to filter release dates."}
            },
            "required": []
        }
    },
    "get_similar_movies": {
        "web_hook_url": "https://swaig-server.signalwire.me/swaig",
        "purpose": "Retrieve a list of movies similar to a given movie",
        "function": "get_similar_movies",
        "argument": {
            "type": "object",
            "properties": {
                "movie_id": {"type": "integer", "description": "The TMDb ID of the movie."},
                "language": {"type": "string", "description": "Language of the results.", "default": "en-US"}
            },
            "required": ["movie_id"]
        }
    },
    "multi_search": {
        "web_hook_url": "https://swaig-server.signalwire.me/swaig",
        "purpose": "Search for movies, TV shows, and people in a single request",
        "function": "multi_search",
        "argument": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "The search query."},
                "language": {"type": "string", "description": "Language of the results.", "default": "en-US"},
                "page": {"type": "integer", "description": "Page number for pagination.", "default": 1},
                "include_adult": {"type": "boolean", "description": "Whether to include adult content.", "default": False},
                "region": {"type": "string", "description": "Specify a region to prioritize search results."}
            },
            "required": ["query"]
        }
    }
}

# Define the /swaig handler
@app.route('/swaig', methods=['POST'])
def swaig_handler():
    data = request.json
    action = data.get('action')

    if action == "get_signature":
        requested_functions = data.get("functions", [])
        host_url = request.host_url.rstrip('/')  # Get the request host URL

        response = [
            {**SWAIG_FUNCTION_SIGNATURES[func], "web_hook_url": f"{host_url}/swaig"}
            for func in requested_functions
            if func in SWAIG_FUNCTION_SIGNATURES
        ]
        return jsonify(response)

    else:
        function_name = data.get('function')
        argument = data.get('argument', {})
        params = argument.get('parsed', [{}])[0]  # Extract the first parsed argument
        print(f"function_name: {function_name}, params: {params}")
        # Map function names to actual functions
        function_map = {
            "search_movie": search_movie,
            "get_movie_details": get_movie_details,
            "discover_movies": discover_movies,
            "get_trending_movies": get_trending_movies,
            "get_movie_recommendations": get_movie_recommendations,
            "get_genre_list": get_genre_list,
            "get_upcoming_movies": get_upcoming_movies,
            "get_now_playing_movies": get_now_playing_movies,
            "get_similar_movies": get_similar_movies,
            "multi_search": multi_search
        }

        if function_name in function_map:
            response = function_map[function_name](**params)
            return jsonify({ "response": response })
        else:
            return jsonify({"error": "Function not found"}), 404



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
