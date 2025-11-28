"""
This script creates a STALKER-themed icon for the Stay Out Timer application.
The icon will be saved as a .ico file for use with PyInstaller.
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_stalker_icon():
    """Create a STALKER-themed icon"""
    # Create a 256x256 image
    img = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw a compass-like circle (STALKER theme)
    # Outer circle
    draw.ellipse([10, 10, 246, 246], fill=(50, 50, 50, 255), outline=(100, 100, 100, 255), width=3)
    
    # Inner circle
    draw.ellipse([50, 50, 206, 206], fill=(30, 30, 30, 255), outline=(80, 80, 80, 255), width=2)
    
    # Draw a needle pointing north (like a compass)
    # Red part (north)
    draw.polygon([(128, 60), (118, 128), (138, 128)], fill=(200, 0, 0, 255))
    # Blue part (south)
    draw.polygon([(128, 196), (118, 128), (138, 128)], fill=(0, 0, 200, 255))
    
    # Draw a central circle
    draw.ellipse([118, 118, 138, 138], fill=(200, 200, 200, 255))
    
    # Draw "S" for STALKER
    try:
        # Try to use a font, fallback to default if not available
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    draw.text((105, 95), "S", fill=(200, 200, 200, 255), font=font)
    
    # Save as ICO
    img.save('stalker_icon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print("STALKER-themed icon created: stalker_icon.ico")

if __name__ == "__main__":
    create_stalker_icon()