"""
Configuration settings for the Apple Music to Spotify transfer program
"""

import os
from typing import Optional

class Config:
    """Configuration class for environment variables and settings"""
    
    def __init__(self):
        # Spotify API credentials
        self.SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
        self.SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI', 'http://localhost:8080/callback')
        
        # Apple Music settings (if any)
        self.APPLE_MUSIC_USER_AGENT = os.getenv('APPLE_MUSIC_USER_AGENT', 
                                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36')
        
        # General settings
        self.REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '30'))
        self.MAX_RETRIES = int(os.getenv('MAX_RETRIES', '3'))
        self.RETRY_DELAY = float(os.getenv('RETRY_DELAY', '1.0'))
        
        # Rate limiting
        self.SPOTIFY_RATE_LIMIT_DELAY = float(os.getenv('SPOTIFY_RATE_LIMIT_DELAY', '0.1'))
        self.APPLE_MUSIC_RATE_LIMIT_DELAY = float(os.getenv('APPLE_MUSIC_RATE_LIMIT_DELAY', '1.0'))
    
    def validate_spotify_config(self) -> bool:
        """Validate that required Spotify configuration is present"""
        if not self.SPOTIFY_CLIENT_ID:
            print("❌ SPOTIFY_CLIENT_ID environment variable is not set")
            return False
        
        if not self.SPOTIFY_CLIENT_SECRET:
            print("❌ SPOTIFY_CLIENT_SECRET environment variable is not set")
            return False
        
        return True
    
    def get_spotify_scope(self) -> str:
        """Get the required Spotify OAuth scope"""
        return "playlist-modify-public playlist-modify-private user-read-private"
    
    def print_config(self):
        """Print current configuration (without sensitive data)"""
        print("Configuration:")
        print(f"  Spotify Client ID: {'*' * 8 if self.SPOTIFY_CLIENT_ID else 'Not set'}")
        print(f"  Spotify Client Secret: {'*' * 8 if self.SPOTIFY_CLIENT_SECRET else 'Not set'}")
        print(f"  Spotify Redirect URI: {self.SPOTIFY_REDIRECT_URI}")
        print(f"  Request Timeout: {self.REQUEST_TIMEOUT}s")
        print(f"  Max Retries: {self.MAX_RETRIES}")
        print(f"  Retry Delay: {self.RETRY_DELAY}s")

# Global config instance
config = Config()

if __name__ == "__main__":
    # Test configuration
    config.print_config()
    
    if config.validate_spotify_config():
        print("✅ Spotify configuration is valid")
    else:
        print("❌ Spotify configuration is invalid")
