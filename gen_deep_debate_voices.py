import asyncio
import edge_tts
import subprocess
import os
import time

parts = [
    {
        "id": "d2_intro",
        "voice": "vi-VN-NamMinhNeural",
        "text": "Tại sao người lớn khi ngồi quán ăn hay cà phê, lại hay né tránh ánh mắt của những người bán vé số dạo?",
    },
    {
        "id": "d2_c1",
        "voice": "vi-VN-NamMinhNeural",
        "text": "Không phải vô tâm đâu. Người lớn né ánh mắt vì họ sợ lòng trắc ẩn của chính mình. Trong túi có khi chỉ còn vài chục nghìn lo cho ngày mai, nhìn vào đôi mắt khắc khổ của một cụ già là sẽ mềm lòng. Né đi là để bảo vệ bản thân khỏi cảm giác bất lực vì muốn giúp mà không đủ sức.",
    },
    {
        "id": "d2_c2",
        "voice": "vi-VN-HoaiMyNeural",
        "text": "Nhiều bạn cứ bảo sao không lắc đầu lịch sự mà phải giả vờ bấm điện thoại. Nói thật các bạn chưa ngồi quán vỉa hè giờ cao điểm rồi. Bạn chỉ cần ngước lên nhìn là người ta xem như có hy vọng, đứng chèo kéo dai dẳng. Lắc đầu một người thì năm người sau kéo tới. Né từ xa là cách duy nhất để có một bữa ăn yên ổn.",
    },
    {
        "id": "d2_c3",
        "voice": "vi-VN-NamMinhNeural",
        "text": "Hồi trẻ mình cũng hay thắc mắc sao bố mẹ đi ăn ngoài cứ lạnh lùng né tránh. Sau này tự đi làm kiếm từng đồng mới hiểu: người lớn ai cũng mang trên vai một đống gánh nặng cơm áo gạo tiền. Họ không có dư thừa năng lượng để gánh thêm nỗi buồn của người khác. Sự né tránh đó, thực chất là một sự kiệt sức.",
    },
    {
        "id": "d2_c4",
        "voice": "vi-VN-HoaiMyNeural",
        "text": "Nhìn vào mắt mà từ chối thì lương tâm cắn rứt, mà mua giúp thì chính mình cũng đang chật vật. Trưởng thành rồi mới nhận ra, người lớn né tránh ánh mắt người bán vé số... đơn giản là vì họ sợ phải đối diện với sự bất lực của chính bản thân mình.",
    },
    {
        "id": "d2_outro",
        "voice": "vi-VN-NamMinhNeural",
        "text": "Còn bạn, bạn nghĩ sự né tránh đó là vô tâm, hay là sự bất lực của người lớn?",
    },
]

async def generate():
    out_dir = r"c:\Users\Dao\Downloads\threads-remotion\public\voice_parts"
    for p in parts:
        raw_fp = os.path.join(out_dir, f"{p['id']}_raw.mp3")
        final_fp = os.path.join(out_dir, f"{p['id']}.mp3")
        print(f"Generating {p['id']} ({p['voice']})...")
        comm = edge_tts.Communicate(text=p['text'], voice=p['voice'])
        await comm.save(raw_fp)
        
        # Apply atempo=1.35 in FFmpeg for clean, snappy 1.35x speed
        cmd = [
            "ffmpeg", "-y", "-i", raw_fp,
            "-filter:a", "atempo=1.35",
            final_fp
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print(f"Speedup done for {p['id']}")
        await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(generate())
