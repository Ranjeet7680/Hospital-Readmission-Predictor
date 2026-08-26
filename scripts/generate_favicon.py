import os
from PIL import Image, ImageDraw

def generate_favicons():
    # 512x512 Master Canvas
    size = (512, 512)
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Background Rounded Rectangle with Deep Navy/Royal Blue Gradient Tone
    draw.rounded_rectangle([16, 16, 496, 496], radius=120, fill=(0, 91, 191, 255), outline=(34, 211, 238, 240), width=16)

    # 2. Medical Shield Path Outline
    shield_pts = [
        (256, 80),
        (420, 140),
        (420, 270),
        (256, 440),
        (92, 270),
        (92, 140)
    ]
    draw.polygon(shield_pts, fill=(0, 47, 108, 180), outline=(255, 255, 255, 220))

    # 3. Medical Cross (Pure White)
    # Vertical Bar
    draw.rounded_rectangle([216, 130, 296, 390], radius=24, fill=(255, 255, 255, 255))
    # Horizontal Bar
    draw.rounded_rectangle([130, 216, 390, 296], radius=24, fill=(255, 255, 255, 255))

    # 4. Cyan Glowing AI Synapse Nodes
    # Center Node
    draw.ellipse([226, 226, 286, 286], fill=(34, 211, 238, 255), outline=(255, 255, 255, 255), width=8)

    # Outer 4 Cross Tips Nodes
    node_r = 22
    for cx, cy in [(256, 145), (256, 375), (145, 256), (375, 256)]:
        draw.ellipse([cx - node_r, cy - node_r, cx + node_r, cy + node_r], fill=(34, 211, 238, 255), outline=(255, 255, 255, 255), width=6)

    # Diagonal AI Pulse Orbs
    orb_r = 14
    for cx, cy in [(180, 180), (332, 180), (180, 332), (332, 332)]:
        draw.ellipse([cx - orb_r, cy - orb_r, cx + orb_r, cy + orb_r], fill=(56, 189, 248, 255), outline=(255, 255, 255, 200), width=4)

    static_dir = os.path.join(os.getcwd(), "static")
    os.makedirs(static_dir, exist_ok=True)

    master_png = os.path.join(static_dir, "favicon.png")
    png_32 = os.path.join(static_dir, "favicon-32x32.png")
    png_16 = os.path.join(static_dir, "favicon-16x16.png")
    apple_touch = os.path.join(static_dir, "apple-touch-icon.png")
    ico_path = os.path.join(static_dir, "favicon.ico")
    root_ico = os.path.join(os.getcwd(), "favicon.ico")

    # Save 512x512
    img.save(master_png, "PNG")

    # Save 180x180 Apple Touch Icon
    img.resize((180, 180), Image.Resampling.LANCZOS).save(apple_touch, "PNG")

    # Save 32x32 and 16x16 PNGs
    img.resize((32, 32), Image.Resampling.LANCZOS).save(png_32, "PNG")
    img.resize((16, 16), Image.Resampling.LANCZOS).save(png_16, "PNG")

    # Save multi-resolution ICO
    img.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    img.save(root_ico, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])

    print(f"Generated all favicons in {static_dir} and root.")

if __name__ == "__main__":
    generate_favicons()
