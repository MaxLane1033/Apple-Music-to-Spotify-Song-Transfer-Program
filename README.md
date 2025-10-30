# Apple Music to Spotify Song Transfer Program

A Python application that allows users to transfer their Apple Music playlists to Spotify. The program scrapes songs from Apple Music playlists and creates corresponding playlists on Spotify using the Spotify Web API.

## Features

- Scrape Apple Music playlist data
- Search for songs on Spotify
- Create new playlists on Spotify
- Add found songs to Spotify playlists
- Handle authentication with both services
- Progress tracking and error handling

## How It Works

1. **Authentication**: The program authenticates with Spotify using OAuth 2.0
2. **Apple Music Scraping**: Uses web scraping to extract song information from Apple Music
3. **Spotify Search**: Searches for each song on Spotify using the Spotify Web API
4. **Playlist Creation**: Creates a new playlist on Spotify
5. **Song Addition**: Adds found songs to the new Spotify playlist

## File Structure

- `transfer_playlist.py`: Main application script
- `spotify_client.py`: Spotify API client
- `apple_music_scraper.py`: Apple Music scraping functionality
- `config.py`: Configuration and settings
- `requirements.txt`: Python dependencies


