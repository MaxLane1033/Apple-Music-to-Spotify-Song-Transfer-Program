"""
Spotify API client for playlist management
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from config import Config

class SpotifyClient:
    def __init__(self):
        self.config = Config()
        self.sp = None
        
    def authenticate(self):
        """Authenticate with Spotify using OAuth 2.0"""
        try:
            scope = "playlist-modify-public playlist-modify-private user-read-private"
            
            self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=self.config.SPOTIFY_CLIENT_ID,
                client_secret=self.config.SPOTIFY_CLIENT_SECRET,
                redirect_uri=self.config.SPOTIFY_REDIRECT_URI,
                scope=scope,
                cache_path=".spotify_cache"
            ))
            
            # Test authentication
            user = self.sp.current_user()
            print(f"Authenticated as: {user['display_name']}")
            return True
            
        except Exception as e:
            print(f"Authentication failed: {str(e)}")
            return False
    
    def create_playlist(self, name, description="Transferred from Apple Music"):
        """Create a new playlist on Spotify"""
        try:
            user = self.sp.current_user()
            playlist = self.sp.user_playlist_create(
                user['id'],
                name,
                public=True,
                description=description
            )
            return playlist['id']
        except Exception as e:
            print(f"Failed to create playlist: {str(e)}")
            return None
    
    def search_track(self, title, artist):
        """Search for a track on Spotify"""
        try:
            # Try different search queries for better results
            search_queries = [
                f"track:{title} artist:{artist}",
                f"{title} {artist}",
                f'"{title}" "{artist}"'
            ]
            
            for query in search_queries:
                results = self.sp.search(q=query, type='track', limit=5)
                
                if results['tracks']['items']:
                    # Return the first result
                    return results['tracks']['items'][0]['id']
            
            return None
            
        except Exception as e:
            print(f"Search failed for '{title}' by '{artist}': {str(e)}")
            return None
    
    def add_track_to_playlist(self, playlist_id, track_id):
        """Add a track to a playlist"""
        try:
            self.sp.playlist_add_items(playlist_id, [track_id])
            return True
        except Exception as e:
            print(f"Failed to add track to playlist: {str(e)}")
            return False
    
    def get_playlist_info(self, playlist_id):
        """Get information about a playlist"""
        try:
            playlist = self.sp.playlist(playlist_id)
            return {
                'name': playlist['name'],
                'description': playlist['description'],
                'tracks': playlist['tracks']['total']
            }
        except Exception as e:
            print(f"Failed to get playlist info: {str(e)}")
            return None
    
    def get_user_playlists(self):
        """Get all playlists for the current user"""
        try:
            playlists = self.sp.current_user_playlists()
            return playlists['items']
        except Exception as e:
            print(f"Failed to get user playlists: {str(e)}")
            return []
