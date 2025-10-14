"""
Main script for transferring Apple Music playlists to Spotify
"""

import argparse
import os
import sys
from spotify_client import SpotifyClient
from apple_music_scraper import AppleMusicScraper
from config import Config

def main():
    parser = argparse.ArgumentParser(description='Transfer Apple Music playlist to Spotify')
    parser.add_argument('--apple_username', type=str, required=True, 
                       help='Apple Music username')
    parser.add_argument('--playlist_name', type=str, required=True,
                       help='Name of the Apple Music playlist to transfer')
    parser.add_argument('--spotify_playlist_name', type=str, default=None,
                       help='Name for the new Spotify playlist (default: same as Apple Music)')
    parser.add_argument('--limit', type=int, default=None,
                       help='Maximum number of songs to transfer')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Set default Spotify playlist name
    if args.spotify_playlist_name is None:
        args.spotify_playlist_name = args.playlist_name
    
    print("🎵 Apple Music to Spotify Playlist Transfer")
    print("=" * 50)
    
    try:
        # Initialize clients
        print("Initializing Spotify client...")
        spotify_client = SpotifyClient()
        
        print("Initializing Apple Music scraper...")
        apple_scraper = AppleMusicScraper()
        
        # Authenticate with Spotify
        print("Authenticating with Spotify...")
        if not spotify_client.authenticate():
            print("❌ Failed to authenticate with Spotify")
            sys.exit(1)
        print("✅ Successfully authenticated with Spotify")
        
        # Get Apple Music playlist
        print(f"Scraping Apple Music playlist: '{args.playlist_name}'")
        apple_songs = apple_scraper.get_playlist_songs(
            args.apple_username, 
            args.playlist_name,
            limit=args.limit
        )
        
        if not apple_songs:
            print("❌ No songs found in Apple Music playlist")
            sys.exit(1)
        
        print(f"✅ Found {len(apple_songs)} songs in Apple Music playlist")
        
        # Create Spotify playlist
        print(f"Creating Spotify playlist: '{args.spotify_playlist_name}'")
        spotify_playlist_id = spotify_client.create_playlist(args.spotify_playlist_name)
        
        if not spotify_playlist_id:
            print("❌ Failed to create Spotify playlist")
            sys.exit(1)
        
        print(f"✅ Created Spotify playlist with ID: {spotify_playlist_id}")
        
        # Transfer songs
        print("Starting song transfer...")
        transferred_count = 0
        not_found_count = 0
        
        for i, song in enumerate(apple_songs, 1):
            if args.verbose:
                print(f"[{i}/{len(apple_songs)}] Searching for: {song['title']} - {song['artist']}")
            
            # Search for song on Spotify
            spotify_track_id = spotify_client.search_track(
                song['title'], 
                song['artist']
            )
            
            if spotify_track_id:
                # Add to playlist
                if spotify_client.add_track_to_playlist(spotify_playlist_id, spotify_track_id):
                    transferred_count += 1
                    if args.verbose:
                        print(f"  ✅ Added to Spotify playlist")
                else:
                    if args.verbose:
                        print(f"  ❌ Failed to add to playlist")
            else:
                not_found_count += 1
                if args.verbose:
                    print(f"  ❌ Song not found on Spotify")
        
        # Summary
        print("\n" + "=" * 50)
        print("🎉 Transfer Complete!")
        print(f"✅ Successfully transferred: {transferred_count} songs")
        print(f"❌ Not found on Spotify: {not_found_count} songs")
        print(f"📊 Success rate: {(transferred_count/len(apple_songs)*100):.1f}%")
        
        if transferred_count > 0:
            print(f"\n🔗 Your new Spotify playlist: {args.spotify_playlist_name}")
        
    except KeyboardInterrupt:
        print("\n❌ Transfer cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
