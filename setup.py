"""
Setup script for the Apple Music to Spotify transfer program
"""

import os
import sys

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print("✅ Python version is compatible")

def check_environment_variables():
    """Check if required environment variables are set"""
    required_vars = ['SPOTIFY_CLIENT_ID', 'SPOTIFY_CLIENT_SECRET']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these variables or create a .env file")
        return False
    
    print("✅ All required environment variables are set")
    return True

def create_env_file():
    """Create a .env file from the example"""
    if os.path.exists('.env'):
        print("✅ .env file already exists")
        return
    
    if os.path.exists('.env.example'):
        import shutil
        shutil.copy('.env.example', '.env')
        print("✅ Created .env file from .env.example")
        print("   Please edit .env with your actual credentials")
    else:
        print("❌ .env.example file not found")

def install_dependencies():
    """Install required dependencies"""
    try:
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False
    return True

def main():
    print("🔧 Setting up Apple Music to Spotify Transfer Program")
    print("=" * 60)
    
    # Check Python version
    check_python_version()
    
    # Create .env file if it doesn't exist
    create_env_file()
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Check environment variables
    if not check_environment_variables():
        print("\n📝 Next steps:")
        print("1. Get Spotify API credentials from https://developer.spotify.com/dashboard")
        print("2. Edit the .env file with your credentials")
        print("3. Run the program again")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("You can now run the transfer program with:")
    print("python transfer_playlist.py --help")

if __name__ == "__main__":
    main()
