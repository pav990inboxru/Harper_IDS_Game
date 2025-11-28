from PIL import Image, ImageDraw, ImageFont
import os

def create_stalker_icon():
    # Create a 256x256 image with a STALKER-themed design
    img = Image.new('RGBA', (256, 256), color=(30, 30, 30, 255))  # Dark gray background
    draw = ImageDraw.Draw(img)
    
    # Draw a radiation symbol-like shape (common STALKER element)
    # Outer circle
    draw.ellipse([40, 40, 216, 216], outline=(180, 180, 0, 255), width=10)
    
    # Inner shape
    draw.ellipse([96, 96, 160, 160], outline=(180, 180, 0, 255), width=8)
    
    # Three blades
    # Blade 1 (top)
    draw.pieslice([80, 80, 176, 176], 60, 120, fill=(180, 180, 0, 255))
    # Blade 2 (bottom-left)
    draw.pieslice([80, 80, 176, 176], 180, 240, fill=(180, 180, 0, 255))
    # Blade 3 (bottom-right)
    draw.pieslice([80, 80, 176, 176], 300, 0, fill=(180, 180, 0, 255))
    
    # Add "S" for STALKER in the center
    try:
        # Try to use a default font
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 60)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Calculate text position to center it
    bbox = draw.textbbox((0, 0), "S", font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (256 - text_width) // 2
    y = (256 - text_height) // 2 - 10
    
    draw.text((x, y), "S", fill=(200, 200, 200, 255), font=font)
    
    # Save as ICO with multiple sizes
    img.save('stalker_icon_new.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print("STALKER icon created successfully!")

if __name__ == "__main__":
    create_stalker_icon()