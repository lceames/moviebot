#!/bin/bash

BASE_URL="https://user:password@hostname.ngrok.io/swaig"

echo "Testing Movie API Endpoints..."
echo "-----------------------------"

echo "Testing search_movie..."
swaig_cli --url "${BASE_URL}" --function search_movie --json '{"query": "The Matrix", "language": "en-US", "page": 1, "include_adult": false}'
echo -e "\n"

echo "Testing get_movie_details..."
swaig_cli --url "${BASE_URL}" --function get_movie_details --json '{"movie_id": 603, "language": "en-US"}'
echo -e "\n"

echo "Testing get_movie_recommendations..."
swaig_cli --url "${BASE_URL}" --function get_movie_recommendations --json '{"movie_id": 603, "language": "en-US"}'
echo -e "\n"

echo "Testing get_trending_movies..."
swaig_cli --url "${BASE_URL}" --function get_trending_movies --json '{"time_window": "week", "language": "en-US"}'
echo -e "\n"

echo "Testing discover_movies..."
swaig_cli --url "${BASE_URL}" --function discover_movies --json '{"language": "en-US", "sort_by": "popularity.desc", "with_genres": "28,12", "primary_release_year": 2024}'
echo -e "\n"

echo "Testing get_genre_list..."
swaig_cli --url "${BASE_URL}" --function get_genre_list --json '{"language": "en-US"}'
echo -e "\n"

echo "Testing get_upcoming_movies..."
swaig_cli --url "${BASE_URL}" --function get_upcoming_movies --json '{"language": "en-US", "region": "US"}'
echo -e "\n"

echo "Testing get_now_playing_movies..."
swaig_cli --url "${BASE_URL}" --function get_now_playing_movies --json '{"language": "en-US", "region": "US"}'
echo -e "\n"

echo "Testing get_similar_movies..."
swaig_cli --url "${BASE_URL}" --function get_similar_movies --json '{"movie_id": 603, "language": "en-US"}'
echo -e "\n"

echo "Testing multi_search..."
swaig_cli --url "${BASE_URL}" --function multi_search --json '{"query": "Brad Pitt", "language": "en-US", "include_adult": false}'
echo -e "\n"

echo "Testing get_movie_credits..."
swaig_cli --url "${BASE_URL}" --function get_movie_credits --json '{"movie_id": 603, "language": "en-US"}'
echo -e "\n"

echo "Testing get_person_details..."
swaig_cli --url "${BASE_URL}" --function get_person_details --json '{"person_id": 287, "language": "en-US", "append_to_response": "movie_credits"}'
echo -e "\n"

echo "Testing get_signature for all functions..."
swaig_cli --url "${BASE_URL}" --get-signatures --function search_movie
swaig_cli --url "${BASE_URL}" --get-signatures --function get_movie_details
swaig_cli --url "${BASE_URL}" --get-signatures --function get_movie_recommendations
swaig_cli --url "${BASE_URL}" --get-signatures --function get_trending_movies
swaig_cli --url "${BASE_URL}" --get-signatures --function discover_movies
swaig_cli --url "${BASE_URL}" --get-signatures --function get_genre_list
swaig_cli --url "${BASE_URL}" --get-signatures --function get_upcoming_movies
swaig_cli --url "${BASE_URL}" --get-signatures --function get_now_playing_movies
swaig_cli --url "${BASE_URL}" --get-signatures --function get_similar_movies
swaig_cli --url "${BASE_URL}" --get-signatures --function multi_search
swaig_cli --url "${BASE_URL}" --get-signatures --function get_movie_credits
swaig_cli --url "${BASE_URL}" --get-signatures --function get_person_details
echo -e "\n"