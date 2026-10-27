import subprocess
import os

OUT_DIR = "public/clips"
os.makedirs(OUT_DIR, exist_ok=True)

# 19 ultra-satisfying 1080p clips combining multiple viral topics:
# - Thiên văn & Vũ trụ sâu (NASA 4K Black hole, Bubble Nebula, Aurora)
# - Thí nghiệm khoa học & ASMR kỳ diệu (Freezing soap bubble ice, Rainbow liquid, Kinetic sand)
# - Ẩm thực & Nấu ăn (4K Sushi chef sashimi slice, Golden espresso crema, Sizzling butter salmon)
# - Nghệ thuật thủ công (Pottery wheel wet clay shaping)
CLIPS = [
    # 0. Thiên văn: NASA 4K Black Hole Lensing (Hố đen bẻ cong không thời gian)
    ("public/black_hole.webm", 2.0, "01_space_black_hole_lensing"),
    # 1. ASMR Cắt cát: Kinetic Sand Razor Slice (Dao lam cắt cát động lực học)
    ("public/kineticsand.webm", 2.0, "02_asmr_kinetic_sand_slice"),
    # 2. Ẩm thực: 4K Sushi Chef Sashimi Slicing (Thái cá hồi điêu luyện)
    ("public/sushi_knife.webm", 1.0, "03_culinary_sushi_sashimi"),
    # 3. Vũ trụ: 3D Approaching Bubble Nebula (Tinh vân vũ trụ 3D)
    ("public/bubble_nebula.webm", 2.0, "04_space_bubble_nebula"),
    # 4. Thí nghiệm ASMR: Freezing Ice Crystals on Soap Bubble (Đóng băng tuyết siêu cận)
    ("public/freezing_bubble.webm", 2.0, "05_asmr_freezing_soap_bubble"),
    # 5. Cà phê: Macro Espresso Crema Dripping (Bọt kem cà phê vàng óng)
    ("public/espresso.webm", 5.0, "06_macro_espresso_crema"),
    # 6. Thiên văn: Aurora Borealis Cosmic Dancing Lights (Cực quang vẫy sóng bầu trời đêm)
    ("public/aurora.webm", 4.0, "07_space_aurora_borealis"),
    # 7. Nấu ăn: Sizzling Butter Salmon Fillet (Áp chảo cá hồi xèo xèo)
    ("public/cooking_salmon.webm", 6.0, "08_culinary_salmon_butter_sizzle"),
    # 8. Hóa học: Rainbow Chemical Liquid Color Swirl (Thí nghiệm đổi màu kỳ ảo)
    ("public/rainbow_exp.webm", 10.0, "09_science_rainbow_chemical_swirl"),
    # 9. Thủ công: Wet Clay Spinning Pottery Wheel (Vuốt gốm êm dịu)
    ("public/pottery.webm", 4.0, "10_craft_pottery_wheel_clay"),
    # 10. Thiên văn: NASA Black Hole Event Horizon Warp (Chân trời sự kiện Lỗ Đen)
    ("public/black_hole.webm", 9.0, "11_space_black_hole_event_horizon"),
    # 11. ASMR Cắt cát: Kinetic Sand Layer Shave (Gọt từng lớp cát mịn)
    ("public/kineticsand.webm", 14.0, "12_asmr_sand_multilayer_shave"),
    # 12. Thí nghiệm ASMR: Soap Bubble Frost Feathering (Cánh hoa tuyết nở trên bong bóng)
    ("public/freezing_bubble.webm", 8.0, "13_asmr_ice_crystal_feathering"),
    # 13. Ẩm thực: Sushi Chef Master Slice 2 (Dao bếp Nhật Bản cắt gọt)
    ("public/sushi_knife.webm", 4.0, "14_culinary_sushi_knife_finish"),
    # 14. Vũ trụ: Deep Space Bubble Nebula Glowing Gas (Khí bụi vũ trụ phát sáng)
    ("public/bubble_nebula.webm", 15.0, "15_space_nebula_cosmic_gas"),
    # 15. Cà phê: Golden Espresso Stream Crema (Dòng chảy espresso đậm đặc)
    ("public/espresso.webm", 16.0, "16_macro_espresso_stream"),
    # 16. Thiên văn: Aurora Green Wave Ribbon Timelapse (Dải lụa cực quang chuyển động)
    ("public/aurora.webm", 25.0, "17_space_aurora_ribbon_timelapse"),
    # 17. Nấu ăn: Salmon Golden Sear Finish (Cá hồi xém cạnh bốc khói thơm)
    ("public/cooking_salmon.webm", 18.0, "18_culinary_salmon_sear_finish"),
    # 18. Hóa học: Rainbow Fluid Bloom (Sự nở rộ của chất lỏng phản ứng hóa học)
    ("public/rainbow_exp.webm", 26.0, "19_science_rainbow_fluid_bloom"),
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
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "22",
        "-an",
        out_path
    ]
    print(f"Extracting clip {i+1}/19: {desc} ({src})...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

# Write concat list
concat_list = f"{OUT_DIR}/concat_list.txt"
with open(concat_list, "w", encoding="utf-8") as f:
    for c in clip_files:
        f.write(f"file '{os.path.basename(c)}'\n")

print("Concatenating into public/asmr_montage_1080p.mp4...")
concat_cmd = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", concat_list,
    "-c", "copy",
    "public/asmr_montage_1080p.mp4"
]
subprocess.run(concat_cmd, check=True)
print("ASMR Multi-Topic Montage 1080p successfully generated!")
