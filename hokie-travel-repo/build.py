"""Builds the single-file prototype: embeds every image in src/assets into src/template.html.
Usage: python3 build.py   ->  writes hokie-travel-prototype.html"""
import base64, os, pathlib
root = pathlib.Path(__file__).parent
A = root / "src" / "assets"
MAP = {
    "LOGO": "logo.png", "WORDMARK": "wordmark.png", "ROUTE": "loading-route.png", "MAP": "map.jpg",
    "NAV_BUS": "nav-bus.png", "NAV_BIKE": "nav-bike.png", "NAV_CARPOOL": "nav-carpool.png",
    "NAV_RENTAL": "nav-rental.png", "NAV_CAL": "nav-cal.png",
}
html = (root / "src" / "template.html").read_text(encoding="utf-8")
for key, fname in MAP.items():
    mime = "image/jpeg" if fname.endswith(".jpg") else "image/png"
    data = base64.b64encode((A / fname).read_bytes()).decode()
    html = html.replace("{{" + key + "}}", f"data:{mime};base64,{data}")
# Optional Google Maps key for live bus directions: GMAPS_KEY env var or src/gmaps-key.txt.
# Leave both empty to build without a key (teammates can paste one in the app with the 🔑 button).
# Never commit the key file, and don't publish a build that has a key in it.
key = os.environ.get("GMAPS_KEY", "").strip()
kf = root / "src" / "gmaps-key.txt"
if not key and kf.exists():
    key = kf.read_text(encoding="utf-8").strip()
html = html.replace("{{GMAPS_KEY}}", key.replace('"', ""))
print("Google Maps key:", "built in" if key else "none (paste one in the app)")
assert "{{" not in html, "unreplaced placeholder left in template"
(root / "hokie-travel-prototype.html").write_text(html, encoding="utf-8")
print("Built hokie-travel-prototype.html")

# Ready-to-host copy for GitHub Pages / Netlify: site/index.html + home-screen icon.
site = root / "site"; site.mkdir(exist_ok=True)
(site / "index.html").write_text(html, encoding="utf-8")
try:
    from PIL import Image
    Image.open(A / "logo.png").convert("RGB").resize((180, 180), Image.LANCZOS).save(site / "apple-touch-icon.png")
except ImportError:
    import shutil; shutil.copy(A / "logo.png", site / "apple-touch-icon.png")
if key:
    print("WARNING: site/index.html contains your Google key. Rebuild without it before uploading anywhere public.")
print("Wrote site/ (upload the files inside it to your host)")
