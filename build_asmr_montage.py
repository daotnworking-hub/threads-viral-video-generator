import subprocess
import os

OUT_DIR = "public/clips"
os.makedirs(OUT_DIR, exist_ok=True)

# 19 ultra-satisfying 1080p clips, each 3.08 seconds (total ~58.5s)
CLIPS = [
    ("public/kineticsand.webm", 2.0, "sand_razor_slice"),
    ("public/sushi_knife.webm", 1.0, "sushi_chef_knife_1"),
    ("public/espresso.webm", 5.0, "macro_espresso_crema_1"),
    ("public/cooking_salmon.webm", 6.0, "salmon_butter_sizzle_1"),
    ("public/rainbow_exp.webm", 10.0, "rainbow_liquid_exp_1"),
    ("public/pottery.webm", 3.0, "pottery_wheel_clay_1"),
    ("public/kineticsand.webm", 8.0, "sand_cube_collapse"),
    ("public/sushi_knife.webm", 4.0, "sushi_chef_knife_2"),
    ("public/espresso.webm", 12.0, "macro_espresso_crema_2"),
    ("public/cooking_salmon.webm", 18.0, "salmon_butter_sizzle_2"),
    ("public/rainbow_exp.webm", 24.0, "rainbow_liquid_exp_2"),
    ("public/pottery.webm", 10.0, "pottery_wheel_clay_2"),
    ("public/kineticsand.webm", 15.0, "sand_multilayer_slice"),
    ("public/espresso.webm", 20.0, "espresso_stream_flow"),
    ("public/cooking_salmon.webm", 28.0, "salmon_butter_sizzle_3"),
    ("public/rainbow_exp.webm", 38.0, "rainbow_liquid_exp_3"),
    ("public/pottery.webm", 18.0, "pottery_wheel_clay_3"),
    ("public/kineticsand.webm", 22.0, "sand_knife_crunch"),
    ("public/espresso.webm", 28.0, "espresso_crema_finish"),
]

clip_files = []
for i, (src, start, desc) in enumerate(CLIPS):
    out_path = f"{OUT_DIR}/clip_{i:02d}.mp4"
    clip_files.append(out_path)
    dur = "3.08"
    cmd = [
        "ffmpeg", "-y", "-ss", str(start), "-i", src,
        "-t", dur,
        "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
        "-r", "30",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "19",
        "-an",
        out_path
    ]
    print(f"Extracting clip {i+1}/19: {desc}...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

# Write concat list
concat_list = f"{OUT_DIR}/concat_list.txt"
with open(concat_list, "w", encoding="utf-8") as f:
    for c in clip_files:
        fname = os.path.basename(c)
        f.write(f"file '{fname}'\n")

final_montage = "public/asmr_montage_1080p.mp4"
concat_cmd = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", concat_list,
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-r", "30",
    final_montage
]
print("Stitching all 19 fast-paced clips together...")
subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
print("SUCCESS: public/asmr_montage_1080p.mp4 is ready!")
