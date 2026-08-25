import os
from PIL import Image, ImageDraw

def generate_favicons():
    size = (64, 64)
    # Create image with alpha channel
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Rounded rectangle background (Navy/Blue gradient style)
    draw.rounded_rectangle([2, 2, 61, 61], radius=16, fill=(0, 91, 191, 255), outline=(34, 211, 238, 200), width=2)
    
    # 2. Medical Cross (White)
    # Vertical bar
    draw.rounded_rectangle([28, 16, 35, 47], radius=3, fill=(255, 255, 255, 255))
    # Horizontal bar
    draw.rounded_rectangle([16, 28, 47, 35], radius=3, fill=(255, 255, 255, 255))

    # 3. Cyan Center Node & Corner Synapses
    draw.ellipse([29, 29, 34, 34], fill=(34, 211, 238, 255), outline=(255, 255, 255, 255))
    draw.ellipse([29, 14, 34, 19], fill=(34, 211, 238, 255))
    draw.ellipse([29, 44, 34, 49], fill=(34, 211, 238, 255))
    draw.ellipse([14, 29, 19, 34], fill=(34, 211, 238, 255))
    draw.ellipse([44, 29, 49, 34], fill=(34, 211, 238, 255))

    static_dir = os.path.join(os.getcwd(), "static")
    png_path = os.path.join(static_dir, "favicon.png")
    ico_path = os.path.join(static_dir, "favicon.ico")

    img.save(png_path, "PNG")
    img.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (64, 64)])
    print(f"Generated {png_path} and {ico_path}")

if __name__ == "__main__":
    generate_favicons()
