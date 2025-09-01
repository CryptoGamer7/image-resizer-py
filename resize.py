from PIL import Image
import sys, pathlib
if len(sys.argv) < 4:
    print("Usage: python resize.py <input> <width> <height>")
    sys.exit(1)
inp, w, h = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
img = Image.open(inp)
img = img.resize((w, h), Image.LANCZOS)
out = pathlib.Path(inp).with_name(f"resized_{w}x{h}_" + pathlib.Path(inp).name)
img.save(out)
print("OK ->", out)
