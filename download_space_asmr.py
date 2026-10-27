import urllib.request
import os

new_downloads = [
    (
        "public/black_hole.webm",
        "https://upload.wikimedia.org/wikipedia/commons/9/92/Isolated_Black_Hole_Visualization_%28SVS14620_-_1-Orbiting_a_bare_black_hole-4K%29.webm"
    ),
    (
        "public/bubble_nebula.webm",
        "https://upload.wikimedia.org/wikipedia/commons/d/d3/Approaching_the_Bubble_Nebula.webm"
    ),
    (
        "public/aurora.webm",
        "https://upload.wikimedia.org/wikipedia/commons/d/df/Aurora_borealis_timelapse.webm"
    ),
    (
        "public/freezing_bubble.webm",
        "https://upload.wikimedia.org/wikipedia/commons/8/88/A_freezing_soap_bubble_in_McGregor%2C_Minnesota.webm"
    )
]

for dst, url in new_downloads:
    if os.path.exists(dst) and os.path.getsize(dst) > 1000000:
        print(f"Already exists: {dst} ({os.path.getsize(dst)} bytes)")
        continue
    print(f"Downloading {dst} from {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req) as resp, open(dst, 'wb') as out_file:
        chunk_size = 1024 * 512
        while True:
            chunk = resp.read(chunk_size)
            if not chunk:
                break
            out_file.write(chunk)
    print(f"Done: {dst} ({os.path.getsize(dst)} bytes)")
