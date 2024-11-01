from flask import Flask, request, jsonify, send_file
import requests
import os
from signalwire_swaig.core import SWAIG, Parameter

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
HTTP_USERNAME = os.getenv("HTTP_USERNAME")
HTTP_PASSWORD = os.getenv("HTTP_PASSWORD")
TMDB_BASE_URL = "https://api.themoviedb.org/3"

swaig = SWAIG(app, auth=(HTTP_USERNAME, HTTP_PASSWORD) if HTTP_USERNAME and HTTP_PASSWORD else None)

def call_tmdb_api(endpoint, params):
    url = f"{TMDB_BASE_URL}{endpoint}"
    params['api_key'] = TMDB_API_KEY
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

@swaig.endpoint("Search for movies by title",
    query=Parameter("string", "The movie title to search for"),
    language=Parameter("string", "Language of the results", required=False),
    page=Parameter("integer", "Page number for pagination", required=False),
    include_adult=Parameter("boolean", "Whether to include adult content", required=False),
    region=Parameter("string", "Specify a region to prioritize search results", required=False),
    year=Parameter("integer", "Filter results by release year", required=False),
    primary_release_year=Parameter("integer", "Filter results by primary release year", required=False))
def search_movie(query, language="en-US", page=1, include_adult=False, region=None, year=None, primary_release_year=None):
    endpoint = "/search/movie"
    params = {
        "query": query,
        "language": language,
        "page": page,
        "include_adult": include_adult,
        "region": region,
        "year": year,
        "primary_release_year": primary_release_year
    }
    response = call_tmdb_api(endpoint, params)
    if 'results' in response:
        return format_movie_search_results(response['results'])
    return response

@swaig.endpoint("Get detailed movie information",
    movie_id=Parameter("integer", "The TMDb ID of the movie"),
    language=Parameter("string", "Language of the results", required=False))
def get_movie_details(movie_id, language="en-US"):
    endpoint = f"/movie/{movie_id}"
    params = {"language": language}
    response = call_tmdb_api(endpoint, params)
    if response and 'id' in response:
        return format_movie_details(response)
    return response

@swaig.endpoint("Get movie recommendations",
    movie_id=Parameter("integer", "The TMDb ID of the movie"),
    language=Parameter("string", "Language of the results", required=False))
def get_movie_recommendations(movie_id, language="en-US"):
    endpoint = f"/movie/{movie_id}/recommendations"
    params = {"language": language}
    response = call_tmdb_api(endpoint, params)
    if 'results' in response:
        return format_movie_recommendations_results(response['results'])
    return response

@swaig.endpoint("Get trending movies",
    time_window=Parameter("string", "Time window (day/week)", required=False),
    language=Parameter("string", "Language of the results", required=False))
def get_trending_movies(time_window="week", language="en-US"):
    endpoint = f"/trending/movie/{time_window}"
    params = {"language": language}
    response = call_tmdb_api(endpoint, params)
    if 'results' in response:
        return format_trending_movies_results(response['results'])
    return response

@swaig.endpoint("Discover movies by different criteria",
    language=Parameter("string", "Language of the results", required=False),
    region=Parameter("string", "Specify a region to filter release dates", required=False),
    sort_by=Parameter("string", "Sort results by criteria", required=False),
    include_adult=Parameter("boolean", "Whether to include adult content", required=False),
    include_video=Parameter("boolean", "Whether to include movies that have a video", required=False),
    page=Parameter("integer", "Page number for pagination", required=False),
    primary_release_year=Parameter("integer", "Filter movies released in a specific year", required=False),
    primary_release_date_gte=Parameter("string", "Filter movies released on or after this date (YYYY-MM-DD)", required=False),
    primary_release_date_lte=Parameter("string", "Filter movies released on or before this date (YYYY-MM-DD)", required=False),
    with_genres=Parameter("string", "Comma-separated genre IDs to filter by", required=False),
    with_cast=Parameter("string", "Comma-separated person IDs to filter by cast", required=False),
    with_crew=Parameter("string", "Comma-separated person IDs to filter by crew", required=False),
    with_keywords=Parameter("string", "Comma-separated keyword IDs to filter by", required=False),
    with_runtime_gte=Parameter("integer", "Filter movies with runtime greater than or equal to this value", required=False),
    with_runtime_lte=Parameter("integer", "Filter movies with runtime less than or equal to this value", required=False))
def discover_movies(language="en-US", region=None, sort_by="popularity.desc", include_adult=False, include_video=False, 
                   page=1, primary_release_year=None, primary_release_date_gte=None, primary_release_date_lte=None,
                   with_genres=None, with_cast=None, with_crew=None, with_keywords=None, with_runtime_gte=None, with_runtime_lte=None):
    endpoint = "/discover/movie"
    params = locals()
    response = call_tmdb_api(endpoint, params)
    if 'results' in response:
        return format_discover_movies_results(response['results'])
    return response

@swaig.endpoint("Get genre list",
    language=Parameter("string", "Language of the results", required=False))
def get_genre_list(language="en-US"):
    endpoint = "/genre/movie/list"
    params = {"language": language}
    response = call_tmdb_api(endpoint, params)
    if 'genres' in response:
        return format_genre_list(response['genres'])
    return response

@swaig.endpoint("Get upcoming movies",
    language=Parameter("string", "Language of the results", required=False),
    region=Parameter("string", "Specify a region to filter release dates", required=False))
def get_upcoming_movies(language="en-US", region=None):
    endpoint = "/movie/upcoming"
    params = {"language": language, "region": region}
    response = call_tmdb_api(endpoint, params)
    if 'results' in response:
        return format_upcoming_movies_results(response['results'])
    return response

@swaig.endpoint("Get now playing movies",
    language=Parameter("string", "Language of the results", required=False),
    region=Parameter("string", "Specify a region to filter release dates", required=False))
def get_now_playing_movies(language="en-US", region=None):
    endpoint = "/movie/now_playing"
    params = {"language": language, "region": region}
    response = call_tmdb_api(endpoint, params)
    if 'results' in response:
        return format_now_playing_movies_results(response['results'])
    return response

@swaig.endpoint("Get similar movies",
    movie_id=Parameter("integer", "The TMDb ID of the movie"),
    language=Parameter("string", "Language of the results", required=False))
def get_similar_movies(movie_id, language="en-US"):
    endpoint = f"/movie/{movie_id}/similar"
    params = {"language": language}
    response = call_tmdb_api(endpoint, params)
    if 'results' in response:
        return format_similar_movies_results(response['results'])
    return response

@swaig.endpoint("Multi-search for movies, TV shows, and people",
    query=Parameter("string", "The search query"),
    language=Parameter("string", "Language of the results", required=False),
    page=Parameter("integer", "Page number for pagination", required=False),
    include_adult=Parameter("boolean", "Whether to include adult content", required=False),
    region=Parameter("string", "Specify a region to prioritize search results", required=False))
def multi_search(query, language="en-US", page=1, include_adult=False, region=None):
    endpoint = "/search/multi"
    params = locals()
    response = call_tmdb_api(endpoint, params)
    if 'results' in response:
        return format_multi_search_results(response['results'])
    return response

@swaig.endpoint("Get movie credits",
    movie_id=Parameter("integer", "The TMDb ID of the movie"),
    language=Parameter("string", "Language of the results", required=False))
def get_movie_credits(movie_id, language="en-US"):
    endpoint = f"/movie/{movie_id}/credits"
    params = {"language": language}
    response = call_tmdb_api(endpoint, params)
    if 'cast' in response or 'crew' in response:
        return format_movie_credits(response)
    return response

@swaig.endpoint("Get person details",
    person_id=Parameter("integer", "The TMDb ID of the person"),
    language=Parameter("string", "Language of the results", required=False),
    append_to_response=Parameter("string", "Additional requests to append to the result", required=False))
def get_person_details(person_id, language="en-US", append_to_response=None):
    endpoint = f"/person/{person_id}"
    params = {"language": language}
    if append_to_response:
        params["append_to_response"] = append_to_response
    response = call_tmdb_api(endpoint, params)
    if 'id' in response:
        return format_person_details(response)
    return response

def format_movie_search_results(results):
    explanation = "These are the search results for movies based on your query:\n"
    formatted_results = [explanation]
    for movie in results[:5]:
        genre_ids = movie.get('genre_ids', [])
        formatted_results.append(
            f"id: {movie['id']} title: {movie['title']} release_date: {movie.get('release_date', 'N/A')} genre_ids: {', '.join(map(str, genre_ids))}"
        )
    return "\n".join(formatted_results)

def format_movie_details(movie):
    explanation = "Here are the detailed information about the movie:\n"
    formatted_details = [explanation]
    genres = ', '.join(genre['name'] for genre in movie.get('genres', []))
    production_companies = ', '.join(company['name'] for company in movie.get('production_companies', []))
    spoken_languages = ', '.join(language['name'] for language in movie.get('spoken_languages', []))
    
    formatted_details.append(
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
    )
    return "\n".join(formatted_details)

def format_movie_recommendations_results(results):
    explanation = "These are the recommended movies based on your selection:\n"
    formatted_results = [explanation]
    for movie in results[:5]:
        genre_ids = movie.get('genre_ids', [])
        formatted_results.append(
            f"id: {movie['id']} title: {movie['title']} release_date: {movie['release_date']} genre_ids: {', '.join(map(str, genre_ids))}"
        )
    return "\n".join(formatted_results)

def format_trending_movies_results(results):
    explanation = "These are the trending movies for the selected time window:\n"
    formatted_results = [explanation]
    for movie in results[:5]:
        genre_ids = movie.get('genre_ids', [])
        formatted_results.append(
            f"id: {movie['id']} title: {movie['title']} release_date: {movie['release_date']} genre_ids: {', '.join(map(str, genre_ids))}"
        )
    return "\n".join(formatted_results)

def format_discover_movies_results(results):
    explanation = "These are the movies discovered based on your criteria:\n"
    formatted_results = [explanation]
    for movie in results[:5]:
        genre_ids = movie.get('genre_ids', [])
        formatted_results.append(
            f"id: {movie['id']} title: {movie['title']} release_date: {movie['release_date']} genre_ids: {', '.join(map(str, genre_ids))}"
        )
    return "\n".join(formatted_results)

def format_genre_list(genres):
    explanation = "Here is the list of available movie genres with their IDs:\n"
    formatted_genres = [explanation]
    for genre in genres:
        formatted_genres.append(
            f"name: {genre['name']} id: {genre['id']}"
        )
    return "\n".join(formatted_genres)

def format_upcoming_movies_results(results):
    explanation = "These are the upcoming movies:\n"
    formatted_results = [explanation]
    for movie in results[:10]:
        genre_ids = movie.get('genre_ids', [])
        formatted_results.append(
            f"id: {movie['id']} title: {movie['title']} release_date: {movie['release_date']} genre_ids: {', '.join(map(str, genre_ids))}"
        )
    return "\n".join(formatted_results)

def format_now_playing_movies_results(results):
    explanation = "These are the movies currently playing in theaters:\n"
    formatted_results = [explanation]
    for movie in results[:10]:
        genre_ids = movie.get('genre_ids', [])
        formatted_results.append(
            f"id: {movie['id']} title: {movie['title']} release_date: {movie['release_date']} genre_ids: {', '.join(map(str, genre_ids))}"
        )
    return "\n".join(formatted_results)

def format_similar_movies_results(results):
    explanation = "These are movies similar to your selection:\n"
    formatted_results = [explanation]
    for movie in results[:5]:
        genre_ids = movie.get('genre_ids', [])
        formatted_results.append(
            f"id: {movie['id']} title: {movie['title']} release_date: {movie['release_date']} genre_ids: {', '.join(map(str, genre_ids))}"
        )
    return "\n".join(formatted_results)

def format_multi_search_results(results):
    explanation = "These are the results from your multi-search query:\n"
    formatted_results = [explanation]
    for item in results[:10]:
        if item['media_type'] == 'movie':
            genre_ids = item.get('genre_ids', [])
            formatted_results.append("movie:")
            formatted_results.append(
                f"id: {item['id']} title: {item['title']} release_date: {item['release_date']} genre_ids: {', '.join(map(str, genre_ids))}"
            )
        elif item['media_type'] == 'tv':
            genre_ids = item.get('genre_ids', [])
            formatted_results.append("tv show:")
            formatted_results.append(
                f"id: {item['id']} name: {item['name']} first_air_date: {item.get('first_air_date', 'N/A')} genre_ids: {', '.join(map(str, genre_ids))}"
            )
        elif item['media_type'] == 'person':
            formatted_results.append("person:")
            formatted_results.append(
                f"name: {item['name']} known_for: {', '.join([known['title'] if 'title' in known else known['name'] for known in item['known_for']])} known_for_department: {item['known_for_department']}"
            )
    return "\n".join(formatted_results)

def format_movie_credits(credits):
    explanation = "Here are the cast and crew details for the movie:\n"
    formatted_credits = [explanation]
    
    if 'cast' in credits:
        formatted_credits.append("cast:")
        for member in credits['cast']:
            formatted_credits.append(
                f"name: {member['name']} character: {member['character']}"
            )
    
    if 'crew' in credits:
        formatted_credits.append("crew:")
        for member in credits['crew']:
            formatted_credits.append(
                f"name: {member['name']} department: {member['department']} job: {member['job']}"
            )
    
    return "\n".join(formatted_credits)

def format_person_details(person):
    explanation = "Here are the details about the person:\n"
    formatted_details = [explanation]
    formatted_details.append(
        f"name: {person['name']}\n"
        f"biography: {person['biography']}\n"
        f"birthday: {person['birthday']}\n"
        f"place_of_birth: {person['place_of_birth']}\n"
        f"known_for: {', '.join([known['title'] if 'title' in known else known['name'] for known in person.get('known_for', [])])}"
    )
    return "\n".join(formatted_details)

@app.route('/', methods=['GET'])
@app.route('/swaig', methods=['GET'])       
def serve_moviebot_html():
    try:
        return send_file('moviebot.html')
    except Exception as e:
        return jsonify({"error": "Failed to serve moviebot.html"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
