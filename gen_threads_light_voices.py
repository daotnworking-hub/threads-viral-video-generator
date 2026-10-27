import asyncio
import edge_tts
import os
import sys
import subprocess
import json
import time

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

SCRIPT_PARTS = [
    {
        "id": "post",
        "voice": "vi-VN-NamMinhNeural",
        "text": "Bạn có biết, tại sao người lớn khi ngồi quán ăn hay cà phê, thường có thói quen né tránh ánh mắt của những người bán vé số dạo?",
        "author": "Chuyện Người Lớn",
        "handle": "chuyennguoilon.vn",
        "time": "5h"
    },
    {
        "id": "c1",
        "voice": "vi-VN-NamMinhNeural",
        "text": "Không phải vì vô tâm hay coi thường đâu bạn. Người lớn né tránh là vì họ sợ lòng trắc ẩn của chính mình. Nhiều khi trong ví chỉ còn vài chục nghìn lo cho ngày mai, nhìn vào đôi mắt khắc khổ của các cô chú là mềm lòng ngay. Né đi là cách để bảo vệ bản thân khỏi cảm giác bất lực vì muốn giúp mà không đủ sức.",
        "author": "Minh Trí",
        "handle": "minhtri.journey",
        "time": "4h",
        "likes": "19.8K",
        "replies": "542"
    },
    {
        "id": "c2",
        "voice": "vi-VN-HoaiMyNeural",
        "text": "Chuẩn luôn bạn ơi. Với lại ở quán xá có một thực tế là: chỉ cần bạn ngước lên trả lời một câu dù rất lịch sự, người ta cũng sẽ thấy có hy vọng và đứng lại nài nỉ, chèo kéo rất lâu. Còn nếu mình vờ không nghe, không nhìn thì người ta mời một lúc không thấy tín hiệu rồi sẽ tự rời đi. Người lớn né tránh là để không rơi vào tình huống khó xử cho cả hai bên.",
        "author": "Hoàng Mai",
        "handle": "hoangmai.life",
        "time": "3h",
        "likes": "28.5K",
        "replies": "912"
    },
    {
        "id": "c3",
        "voice": "vi-VN-NamMinhNeural",
        "text": "Đúng vậy ạ. Hồi nhỏ mình cũng trách sao người lớn lạnh lùng thế. Đến khi tự đi làm kiếm từng đồng, gánh vác tiền nhà tiền điện mới hiểu. Ánh mắt né tránh đó không phải là lạnh nhạt, mà là một tiếng thở dài bất lực của những người lớn cũng đang chật vật mưu sinh.",
        "author": "Quang Huy",
        "handle": "quanghuy.story",
        "time": "2h",
        "likes": "35.2K",
        "replies": "1.2K"
    },
    {
        "id": "c4",
        "voice": "vi-VN-HoaiMyNeural",
        "text": "Mỗi người một hoàn cảnh, từ chối hay ủng hộ đều cần sự tôn trọng. Còn bạn, bạn nghĩ sao về thói quen này của người lớn?",
        "author": "Thanh Thảo",
        "handle": "thanhthao_talks",
        "time": "1h",
        "likes": "12.6K",
        "replies": "315"
    }
]

OUT_DIR = "public/voice_parts"
os.makedirs(OUT_DIR, exist_ok=True)

# Remove part 2 to force regenerate with new text
part2_raw = f"{OUT_DIR}/light_raw_2.mp3"
part2_fast = f"{OUT_DIR}/light_fast_2.mp3"
if os.path.exists(part2_raw):
    os.remove(part2_raw)
if os.path.exists(part2_fast):
    os.remove(part2_fast)

async def gen_voice(part, index):
    raw_path = f"{OUT_DIR}/light_raw_{index}.mp3"
    fast_path = f"{OUT_DIR}/light_fast_{index}.mp3"
    
    # If already generated and valid size (>5000 bytes), reuse
    if os.path.exists(fast_path) and os.path.getsize(fast_path) > 5000:
        print(f"Part {index} already exists, skipping generation.")
        return fast_path

    success = False
    for attempt in range(3):
        try:
            print(f"Generating voice for part {index} (attempt {attempt+1})...")
            comm = edge_tts.Communicate(part["text"], part["voice"])
            await comm.save(raw_path)
            if os.path.exists(raw_path) and os.path.getsize(raw_path) > 1000:
                success = True
                break
        except Exception as e:
            print(f"Error on attempt {attempt+1}: {e}")
            await asyncio.sleep(2)
            
    if not success:
        print(f"Fallback to gTTS for part {index}...")
        from gtts import gTTS
        tts = gTTS(text=part["text"], lang="vi", slow=False)
        tts.save(raw_path)
        
    # Speed up 1.35x and boost volume 1.45x
    cmd = [
        "ffmpeg", "-y", "-i", raw_path,
        "-filter:a", "atempo=1.35,volume=1.45",
        fast_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return fast_path

def get_duration(file_path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

async def main():
    fast_files = []
    for i, p in enumerate(SCRIPT_PARTS):
        fp = await gen_voice(p, i)
        fast_files.append(fp)
        await asyncio.sleep(0.5)
        
    durations = [get_duration(f) for f in fast_files]
    print("Durations of parts:", durations)
    
    fps = 30
    timeline = []
    
    # Part 0 is post question
    post_dur = durations[0]
    post_frames = int(post_dur * fps)
    
    current_frame = 10
    
    timeline.append({
        "id": "post",
        "author": SCRIPT_PARTS[0]["author"],
        "handle": SCRIPT_PARTS[0]["handle"],
        "time": SCRIPT_PARTS[0]["time"],
        "text": SCRIPT_PARTS[0]["text"],
        "startFrame": current_frame,
        "endFrame": current_frame + post_frames,
        "durationSec": post_dur
    })
    
    current_frame += post_frames + 12
    
    for i in range(1, len(SCRIPT_PARTS)):
        part_dur = durations[i]
        part_frames = int(part_dur * fps)
        p = SCRIPT_PARTS[i]
        
        timeline.append({
            "id": p["id"],
            "commentIndex": i,
            "author": p["author"],
            "handle": p["handle"],
            "time": p["time"],
            "likes": p["likes"],
            "replies": p["replies"],
            "text": p["text"],
            "startFrame": current_frame,
            "endFrame": current_frame + part_frames,
            "durationSec": part_dur
        })
        current_frame += part_frames + 10
        
    total_frames = current_frame + 45
    print(f"Total frames: {total_frames} ({total_frames/fps:.1f}s)")
    
    with open("src/threads_light_timeline.json", "w", encoding="utf-8") as f:
        json.dump({
            "fps": fps,
            "totalFrames": total_frames,
            "parts": timeline
        }, f, ensure_ascii=False, indent=2)
        
    print("Timeline saved to src/threads_light_timeline.json")
    
    # Create silence file for pause between parts (0.35s)
    silence_file = f"{OUT_DIR}/silence.mp3"
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
        "-t", "0.35", "-q:a", "9", silence_file
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    concat_list_path = f"{OUT_DIR}/concat_list.txt"
    with open(concat_list_path, "w", encoding="utf-8") as f:
        f.write(f"file 'silence.mp3'\n")
        for ff in fast_files:
            fname = os.path.basename(ff)
            f.write(f"file '{fname}'\n")
            f.write(f"file 'silence.mp3'\n")
            
    concat_cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list_path,
        "-c:a", "libmp3lame", "-b:a", "192k",
        "public/threads_light_audio.mp3"
    ]
    subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    final_dur = get_duration("public/threads_light_audio.mp3")
    print(f"Final audio duration: {final_dur:.2f}s ready at public/threads_light_audio.mp3")

if __name__ == "__main__":
    asyncio.run(main())
