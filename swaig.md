# SWAIG Functions to TMDb API Mappings

This document provides a detailed mapping of each SignalWire AI Gateway (SWAIG) function to the corresponding The Movie Database (TMDb) API endpoints. This will assist in integrating TMDb API calls within your AI agent's functions, enabling real-time movie data retrieval.

---

## Function Mappings

### 1. `search_movie`

**Purpose**: Search for movies by title.

#### SWAIG Function Definition

```json
{
  "name": "search_movie",
  "purpose": "Search for movies by title.",
  "argument": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The movie title to search for."
      },
      "language": {
        "type": "string",
        "description": "Language of the results.",
        "default": "en-US"
      },
      "page": {
        "type": "integer",
        "description": "Page number for pagination.",
        "default": 1
      },
      "include_adult": {
        "type": "boolean",
        "description": "Whether to include adult (pornographic) content.",
        "default": false
      },
      "region": {
        "type": "string",
        "description": "Specify a region to prioritize search results."
      },
      "year": {
        "type": "integer",
        "description": "Filter results by release year."
      },
      "primary_release_year": {
        "type": "integer",
        "description": "Filter results by primary release year."
      }
    },
    "required": ["query"]
  }
}
```

#### Corresponding TMDb API Endpoint

- **Endpoint**: `/search/movie`
- **Documentation**: [Search Movies](https://developers.themoviedb.org/3/search/search-movies)

#### Parameter Mapping

| SWAIG Parameter        | TMDb API Parameter     |
|------------------------|------------------------|
| `query`                | `query`                |
| `language`             | `language`             |
| `page`                 | `page`                 |
| `include_adult`        | `include_adult`        |
| `region`               | `region`               |
| `year`                 | `year`                 |
| `primary_release_year` | `primary_release_year` |

#### Example API Call

```http
GET https://api.themoviedb.org/3/search/movie?api_key=YOUR_API_KEY&query=Inception&language=en-US&page=1&include_adult=false
```

---

### 2. `get_movie_details`

**Purpose**: Retrieve detailed information about a movie.

#### SWAIG Function Definition

```json
{
  "name": "get_movie_details",
  "purpose": "Retrieve detailed information about a movie.",
  "argument": {
    "type": "object",
    "properties": {
      "movie_id": {
        "type": "integer",
        "description": "The TMDb ID of the movie."
      },
      "language": {
        "type": "string",
        "description": "Language of the results.",
        "default": "en-US"
      },
      "append_to_response": {
        "type": "string",
        "description": "Additional requests to append to the result."
      }
    },
    "required": ["movie_id"]
  }
}
```

#### Corresponding TMDb API Endpoint

- **Endpoint**: `/movie/{movie_id}`
- **Documentation**: [Get Movie Details](https://developers.themoviedb.org/3/movies/get-movie-details)

#### Parameter Mapping

| SWAIG Parameter        | TMDb API Parameter      |
|------------------------|-------------------------|
| `movie_id`             | `{movie_id}` (path parameter) |
| `language`             | `language`              |
| `append_to_response`   | `append_to_response`    |

#### Example API Call

```http
GET https://api.themoviedb.org/3/movie/550?api_key=YOUR_API_KEY&language=en-US
```

---

### 3. `discover_movies`

**Purpose**: Discover movies by different criteria.

#### SWAIG Function Definition

```json
{
  "name": "discover_movies",
  "purpose": "Discover movies by different criteria.",
  "argument": {
    "type": "object",
    "properties": {
      "language": {
        "type": "string",
        "description": "Language of the results.",
        "default": "en-US"
      },
      "region": {
        "type": "string",
        "description": "Specify a region to filter release dates."
      },
      "sort_by": {
        "type": "string",
        "description": "Sort results by criteria.",
        "default": "popularity.desc"
      },
      "include_adult": {
        "type": "boolean",
        "description": "Whether to include adult content.",
        "default": false
      },
      "include_video": {
        "type": "boolean",
        "description": "Whether to include movies that have a video.",
        "default": false
      },
      "page": {
        "type": "integer",
        "description": "Page number for pagination.",
        "default": 1
      },
      "primary_release_year": {
        "type": "integer",
        "description": "Filter movies released in a specific year."
      },
      "primary_release_date_gte": {
        "type": "string",
        "description": "Filter movies released on or after this date (YYYY-MM-DD)."
      },
      "primary_release_date_lte": {
        "type": "string",
        "description": "Filter movies released on or before this date (YYYY-MM-DD)."
      },
      "with_genres": {
        "type": "string",
        "description": "Comma-separated genre IDs to filter by."
      },
      "with_cast": {
        "type": "string",
        "description": "Comma-separated person IDs to filter by cast."
      },
      "with_crew": {
        "type": "string",
        "description": "Comma-separated person IDs to filter by crew."
      },
      "with_keywords": {
        "type": "string",
        "description": "Comma-separated keyword IDs to filter by."
      },
      "with_runtime_gte": {
        "type": "integer",
        "description": "Filter movies with runtime greater than or equal to this value."
      },
      "with_runtime_lte": {
        "type": "integer",
        "description": "Filter movies with runtime less than or equal to this value."
      }
    },
    "required": []
  }
}
```

#### Corresponding TMDb API Endpoint

- **Endpoint**: `/discover/movie`
- **Documentation**: [Discover Movies](https://developers.themoviedb.org/3/discover/movie-discover)

#### Parameter Mapping

All parameters map directly to the TMDb API parameters.

#### Example API Call

```http
GET https://api.themoviedb.org/3/discover/movie?api_key=YOUR_API_KEY&language=en-US&sort_by=popularity.desc&with_genres=28,12&primary_release_year=2021
```

---

### 4. `get_trending_movies`

**Purpose**: Retrieve a list of movies that are currently trending.

#### SWAIG Function Definition

```json
{
  "name": "get_trending_movies",
  "purpose": "Retrieve a list of movies that are currently trending.",
  "argument": {
    "type": "object",
    "properties": {
      "time_window": {
        "type": "string",
        "description": "Time window to fetch trends for ('day' or 'week').",
        "enum": ["day", "week"],
        "default": "week"
      },
      "language": {
        "type": "string",
        "description": "Language of the results.",
        "default": "en-US"
      },
      "page": {
        "type": "integer",
        "description": "Page number for pagination.",
        "default": 1
      }
    },
    "required": []
  }
}
```

#### Corresponding TMDb API Endpoint

- **Endpoint**: `/trending/{media_type}/{time_window}`
  - `media_type`: `movie`
  - `time_window`: `day` or `week`
- **Documentation**: [Get Trending](https://developers.themoviedb.org/3/trending/get-trending)

#### Parameter Mapping

| SWAIG Parameter | TMDb API Parameter           |
|-----------------|------------------------------|
| `time_window`   | `{time_window}` (path parameter) |
| `language`      | `language`                   |
| `page`          | `page`                       |

#### Example API Call

```http
GET https://api.themoviedb.org/3/trending/movie/week?api_key=YOUR_API_KEY&language=en-US&page=1
```

---

### 5. `get_movie_recommendations`

**Purpose**: Get recommendations based on a specific movie.

#### SWAIG Function Definition

```json
{
  "name": "get_movie_recommendations",
  "purpose": "Get recommendations based on a specific movie.",
  "argument": {
    "type": "object",
    "properties": {
      "movie_id": {
        "type": "integer",
        "description": "The TMDb ID of the movie."
      },
      "language": {
        "type": "string",
        "description": "Language of the results.",
        "default": "en-US"
      },
      "page": {
        "type": "integer",
        "description": "Page number for pagination.",
        "default": 1
      }
    },
    "required": ["movie_id"]
  }
}
```

#### Corresponding TMDb API Endpoint

- **Endpoint**: `/movie/{movie_id}/recommendations`
- **Documentation**: [Get Movie Recommendations](https://developers.themoviedb.org/3/movies/get-movie-recommendations)

#### Parameter Mapping

| SWAIG Parameter | TMDb API Parameter        |
|-----------------|---------------------------|
| `movie_id`      | `{movie_id}` (path parameter) |
| `language`      | `language`                |
| `page`          | `page`                    |

#### Example API Call

```http
GET https://api.themoviedb.org/3/movie/550/recommendations?api_key=YOUR_API_KEY&language=en-US&page=1
```

---

### 6. `get_movie_credits`

**Purpose**: Retrieve cast and crew information for a movie.

#### SWAIG Function Definition

```json
{
  "name": "get_movie_credits",
  "purpose": "Retrieve cast and crew information for a movie.",
  "argument": {
    "type": "object",
    "properties": {
      "movie_id": {
        "type": "integer",
        "description": "The TMDb ID of the movie."
      },
      "language": {
        "type": "string",
        "description": "Language of the results.",
        "default": "en-US"
      }
    },
    "required": ["movie_id"]
  }
}
```

#### Corresponding TMDb API Endpoint

- **Endpoint**: `/movie/{movie_id}/credits`
- **Documentation**: [Get Movie Credits](https://developers.themoviedb.org/3/movies/get-movie-credits)

#### Parameter Mapping

| SWAIG Parameter | TMDb API Parameter        |
|-----------------|---------------------------|
| `movie_id`      | `{movie_id}` (path parameter) |
| `language`      | `language`                |

#### Example API Call

```http
GET https://api.themoviedb.org/3/movie/550/credits?api_key=YOUR_API_KEY&language=en-US
```

---

### 7. `get_person_details`

**Purpose**: Retrieve detailed information about a person.

#### SWAIG Function Definition

```json
{
  "name": "get_person_details",
  "purpose": "Retrieve detailed information about a person.",
  "argument": {
    "type": "object",
    "properties": {
      "person_id": {
        "type": "integer",
        "description": "The TMDb ID of the person."
      },
      "language": {
        "type": "string",
        "description": "Language of the results.",
        "default": "en-US"
      },
      "append_to_response": {
        "type": "string",
        "description": "Additional requests to append to the result."
      }
    },
    "required": ["person_id"]
  }
}
```

#### Corresponding TMDb API Endpoint

- **Endpoint**: `/person/{person_id}`
- **Documentation**: [Get Person Details](https://developers.themoviedb.org/3/people/get-person-details)

#### Parameter Mapping

| SWAIG Parameter      | TMDb API Parameter      |
|----------------------|-------------------------|
| `person_id`          | `{person_id}` (path parameter) |
| `language`           | `language`              |
| `append_to_response` | `append_to_response`    |

#### Example API Call

```http
GET https://api.themoviedb.org/3/person/287?api_key=YOUR_API_KEY&language=en-US
```

---

### 8. `get_genre_list`

**Purpose**: Retrieve the list of official genres.

#### SWAIG Function Definition

```json
{
  "name": "get_genre_list",
  "purpose": "Retrieve the list of official genres.",
  "argument": {
    "type": "object",
    "properties": {
      "language": {
        "type": "string",
        "description": "Language of the results.",
        "default": "en-US"
      }
    },
    "required": []
  }
}
```

#### Corresponding TMDb API Endpoint

- **Endpoint**: `/genre/movie/list`
- **Documentation**: [Get Movie Genres](https://developers.themoviedb.org/3/genres/get-movie-list)

#### Parameter Mapping

| SWAIG Parameter | TMDb API Parameter |
|-----------------|--------------------|
| `language`      | `language`         |

#### Example API Call

```http
GET https://api.themoviedb.org/3/genre/movie/list?api_key=YOUR_API_KEY&language=en-US
```

---

### 9. `get_upcoming_movies`

**Purpose**: Retrieve movies that are soon to be released.

#### SWAIG Function Definition

```json
{
  "name": "get_upcoming_movies",
  "purpose": "Retrieve movies that are soon to be released.",
  "argument": {
    "type": "object",
    "properties": {
      "language": {
        "type": "string",
        "description": "Language of the results.",
        "default": "en-US"
      },
      "region": {
        "type": "string",
        "description": "Specify a region to filter release dates."
      },
      "page": {
        "type": "integer",
        "description": "Page number for pagination.",
        "default": 1
      }
    },
    "required": []
  }
}
```

#### Corresponding TMDb API Endpoint

- **Endpoint**: `/movie/upcoming`
- **Documentation**: [Get Upcoming Movies](https://developers.themoviedb.org/3/movies/get-upcoming)

#### Parameter Mapping

| SWAIG Parameter | TMDb API Parameter |
|-----------------|--------------------|
| `language`      | `language`         |
| `region`        | `region`           |
| `page`          | `page`             |

#### Example API Call

```http
GET https://api.themoviedb.org/3/movie/upcoming?api_key=YOUR_API_KEY&language=en-US&page=1
```

---

### 10. `get_now_playing_movies`

**Purpose**: Retrieve movies currently playing in theaters.

#### SWAIG Function Definition

```json
{
  "name": "get_now_playing_movies",
  "purpose": "Retrieve movies currently playing in theaters.",
  "argument": {
    "type": "object",
    "properties": {
      "language": {
        "type": "string",
        "description": "Language of the results.",
        "default": "en-US"
      },
      "region": {
        "type": "string",
        "description": "Specify a region to filter release dates."
      },
      "page": {
        "type": "integer",
        "description": "Page number for pagination.",
        "default": 1
      }
    },
    "required": []
  }
}
```

#### Corresponding TMDb API Endpoint

- **Endpoint**: `/movie/now_playing`
- **Documentation**: [Get Now Playing Movies](https://developers.themoviedb.org/3/movies/get-now-playing)

#### Parameter Mapping

| SWAIG Parameter | TMDb API Parameter |
|-----------------|--------------------|
| `language`      | `language`         |
| `region`        | `region`           |
| `page`          | `page`             |

#### Example API Call

```http
GET https://api.themoviedb.org/3/movie/now_playing?api_key=YOUR_API_KEY&language=en-US&page=1
```

---

### 11. `get_similar_movies`

**Purpose**: Retrieve movies similar to a specified movie.

#### SWAIG Function Definition

```json
{
  "name": "get_similar_movies",
  "purpose": "Retrieve movies similar to a specified movie.",
  "argument": {
    "type": "object",
    "properties": {
      "movie_id": {
        "type": "integer",
        "description": "The TMDb ID of the movie."
      },
      "language": {
        "type": "string",
        "description": "Language of the results.",
        "default": "en-US"
      },
      "page": {
        "type": "integer",
        "description": "Page number for pagination.",
        "default": 1
      }
    },
    "required": ["movie_id"]
  }
}
```

#### Corresponding TMDb API Endpoint

- **Endpoint**: `/movie/{movie_id}/similar`
- **Documentation**: [Get Similar Movies](https://developers.themoviedb.org/3/movies/get-similar-movies)

#### Parameter Mapping

| SWAIG Parameter | TMDb API Parameter        |
|-----------------|---------------------------|
| `movie_id`      | `{movie_id}` (path parameter) |
| `language`      | `language`                |
| `page`          | `page`                    |

#### Example API Call

```http
GET https://api.themoviedb.org/3/movie/550/similar?api_key=YOUR_API_KEY&language=en-US&page=1
```

---

### 12. `multi_search`

**Purpose**: Search for movies, TV shows, and people with a single query.

#### SWAIG Function Definition

```json
{
  "name": "multi_search",
  "purpose": "Search for movies, TV shows, and people with a single query.",
  "argument": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The search query."
      },
      "language": {
        "type": "string",
        "description": "Language of the results.",
        "default": "en-US"
      },
      "page": {
        "type": "integer",
        "description": "Page number for pagination.",
        "default": 1
      },
      "include_adult": {
        "type": "boolean",
        "description": "Whether to include adult content.",
        "default": false
      },
      "region": {
        "type": "string",
        "description": "Specify a region to prioritize search results."
      }
    },
    "required": ["query"]
  }
}
```

#### Corresponding TMDb API Endpoint

- **Endpoint**: `/search/multi`
- **Documentation**: [Multi Search](https://developers.themoviedb.org/3/search/multi-search)

#### Parameter Mapping

| SWAIG Parameter   | TMDb API Parameter |
|-------------------|--------------------|
| `query`           | `query`            |
| `language`        | `language`         |
| `page`            | `page`             |
| `include_adult`   | `include_adult`    |
| `region`          | `region`           |

#### Example API Call

```http
GET https://api.themoviedb.org/3/search/multi?api_key=YOUR_API_KEY&language=en-US&query=Tom%20Hanks&page=1&include_adult=false
```

---

## Notes on Integration

- **API Key**: Replace `YOUR_API_KEY` with your actual TMDb API key in all API calls.
- **Path Parameters**: `{movie_id}` and `{person_id}` are path parameters and should be replaced with actual IDs.
- **Default Parameters**: If certain parameters are not provided, defaults are used as specified in the SWAIG function definitions.
- **Pagination**: For endpoints that support pagination, use the `page` parameter to navigate through results.

## Handling Responses

- The responses from TMDb APIs are typically in JSON format.
- Parse the JSON responses to extract relevant information.
- Handle errors gracefully by checking for error codes in the response.

## Example Integration Flow

When the AI agent needs to fulfill a user's request:

1. **Determine Required Function**: Based on the user's input, select the appropriate SWAIG function.
2. **Collect Parameters**: Extract necessary parameters from the user's input or use defaults.
3. **Invoke SWAIG Function**: Call the SWAIG function, which in turn makes the TMDb API call.
4. **Process API Response**: Parse the response and extract needed data.
5. **Compose AI Response**: Use the data to formulate a response to the user.
6. **Return Response**: Send the response back to the user via the communication channel.

---

## Example Use Case

**User**: "Can you tell me about the latest action movies?"

**Process**:

1. **Function Used**: `discover_movies`
2. **Parameters**:
   - `with_genres`: Get the genre ID for 'Action' from `get_genre_list` function.
   - `sort_by`: `release_date.desc`
   - `language`: Default (`en-US`)
3. **API Call**:

```http
GET https://api.themoviedb.org/3/discover/movie?api_key=YOUR_API_KEY&language=en-US&sort_by=release_date.desc&with_genres=28
```

4. **Response Handling**: Parse the response to get a list of the latest action movies.
5. **AI Response**: Provide the user with information about the latest action movies.

---

## Conclusion

By mapping SWAIG functions to TMDb API endpoints, you can seamlessly integrate real-time movie data into your AI agent, enhancing its ability to provide accurate and current information to users.

---

**Note**: Ensure compliance with TMDb's [terms of use](https://www.themoviedb.org/documentation/api/terms-of-use), including proper attribution and adherence to rate limits.

---

Overall, this mapping will help you implement each function effectively, ensuring your AI agent can utilize the TMDb API to its full potential.