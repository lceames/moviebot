# Movie Expert AI Agent

## Overview

The Movie Expert AI Agent is a sophisticated assistant designed to provide detailed information about movies, directors, actors, genres, and personalized recommendations. It leverages the SignalWire AI Gateway (SWAIG) for real-time communication, OpenAI's GPT models for natural language processing, and The Movie Database (TMDb) API for up-to-date movie data.

## Features

- **Movie Search**: Find movies by title using the `search_movie` function.
- **Detailed Movie Information**: Retrieve comprehensive details about a movie with `get_movie_details`.
- **Movie Discovery**: Discover movies based on genres, release year, and popularity using `discover_movies`.
- **Trending Movies**: Get a list of currently trending movies with `get_trending_movies`.
- **Recommendations**: Receive movie recommendations based on a specific movie using `get_movie_recommendations`.
- **Cast and Crew Information**: Access detailed cast and crew information with `get_movie_credits`.
- **Person Details**: Fetch detailed information about actors and directors using `get_person_details`.
- **Genre List**: Retrieve a list of official movie genres with `get_genre_list`.
- **Upcoming Movies**: Get information on movies soon to be released using `get_upcoming_movies`.
- **Now Playing**: Find movies currently playing in theaters with `get_now_playing_movies`.
- **Similar Movies**: Discover movies similar to a specified movie using `get_similar_movies`.
- **Multi-Search**: Perform a broad search across movies, TV shows, and people with `multi_search`.

## Architecture

The AI agent is built on the following components:

- **SignalWire AI Gateway (SWAIG)**: Facilitates real-time communication and integrates AI functionalities.
- **OpenAI GPT Models**: Provides natural language understanding and generation capabilities.
- **TMDb API**: Supplies real-time movie data, ensuring the AI provides accurate and current information.

## Getting Started

### Prerequisites

- **API Key**: Obtain an API key from TMDb to access their API.
- **SignalWire Account**: Set up an account with SignalWire to use their AI Gateway.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/briankwest/moviebot.git
   cd moviebot
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**:
   Replace `YOUR_API_KEY` in the code with your actual TMDb API key.

### Usage

Run the AI agent using the command:
```bash
python app.py
```

Interact with the AI agent through the configured communication channels to get movie information and recommendations.

## Development

### Adding New Features

To add new features or functions, follow these steps:

1. **Define New SWAIG Functions**: Map new functionalities to TMDb API endpoints.
2. **Update AI Agent**: Integrate the new functions into the AI agent's capabilities.
3. **Test**: Ensure the new features work as expected and handle errors gracefully.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **SignalWire**: For providing the AI Gateway.
- **OpenAI**: For the GPT models.
- **TMDb**: For the comprehensive movie database.

## Contact

For questions or support, please contact [your-email@example.com](mailto:your-email@example.com).

