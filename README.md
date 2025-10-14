# Apple Music to Spotify Song Transfer Program

A Python application that allows users to transfer their Apple Music playlists to Spotify. The program scrapes songs from Apple Music playlists and creates corresponding playlists on Spotify using the Spotify Web API.

## Features

- Scrape Apple Music playlist data
- Search for songs on Spotify
- Create new playlists on Spotify
- Add found songs to Spotify playlists
- Handle authentication with both services
- Progress tracking and error handling

## Requirements

- Python 3.8+
- Spotify Developer Account
- Apple Music account access
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Apple-Music-to-Spotify-Song-Transfer-Program
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Spotify Developer App:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new app
   - Note down your Client ID and Client Secret
   - Add `http://localhost:8080/callback` to Redirect URIs

4. Set up environment variables:
```bash
export SPOTIFY_CLIENT_ID="your_client_id"
export SPOTIFY_CLIENT_SECRET="your_client_secret"
```

## Usage

### Basic Usage

```bash
python transfer_playlist.py --apple_username "your_apple_music_username" --playlist_name "Your Playlist Name"
```

### Command Line Options

- `--apple_username`: Your Apple Music username
- `--playlist_name`: Name of the Apple Music playlist to transfer
- `--spotify_playlist_name`: Name for the new Spotify playlist (optional)
- `--limit`: Maximum number of songs to transfer (optional)

### Example

```bash
python transfer_playlist.py \
  --apple_username "john_doe" \
  --playlist_name "My Favorites" \
  --spotify_playlist_name "Transferred Favorites" \
  --limit 50
```

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

## Configuration

The program uses environment variables for configuration:

- `SPOTIFY_CLIENT_ID`: Your Spotify app's client ID
- `SPOTIFY_CLIENT_SECRET`: Your Spotify app's client secret
- `SPOTIFY_REDIRECT_URI`: Redirect URI (default: http://localhost:8080/callback)

## Limitations

- Apple Music scraping may be limited by their terms of service
- Some songs may not be found on Spotify
- Rate limiting applies to both Apple Music and Spotify APIs
- Requires manual authentication for Spotify

## Error Handling

The program includes comprehensive error handling for:
- Network connectivity issues
- Authentication failures
- Song not found errors
- API rate limiting
- Invalid playlist names

## Security Notes

- Never commit your Spotify credentials to version control
- Use environment variables for sensitive information
- The program only requests necessary permissions from Spotify

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is for personal use only. Please respect the terms of service of both Apple Music and Spotify. The authors are not responsible for any misuse of this software.
