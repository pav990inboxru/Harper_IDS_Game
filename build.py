"""
Build script for Stay Out Timer application using PyInstaller
Creates a standalone executable with a STALKER-themed icon
"""
import PyInstaller.__main__
import os
import sys

def build_application():
    """Build the Stay Out Timer application"""
    # Define the build parameters
    # On Windows the syntax is --add-data="src;dest", on Unix it's --add-data="src:dest"
    import platform
    if platform.system() == "Windows":
        data_separator = ";"
    else:
        data_separator = ":"
    
    args = [
        'stay_out_timer.py',  # The main script
        '--name=StayOutTimer',  # Name of the executable
        '--onefile',  # Create a single executable file
        '--windowed',  # Don't show console window
        '--icon=stalker_icon.ico',  # Use the STALKER-themed icon
        f'--add-data=settings.json{data_separator}.',  # Include settings file
        f'--add-data=state.json{data_separator}.',  # Include state file
        '--collect-all=pygame',  # Include pygame modules
        '--clean',  # Clean up temporary files
    ]
    
    # Run PyInstaller with the arguments
    print("Building Stay Out Timer application...")
    PyInstaller.__main__.run(args)
    print("Build completed! Check the 'dist' folder for the executable.")

if __name__ == "__main__":
    build_application()