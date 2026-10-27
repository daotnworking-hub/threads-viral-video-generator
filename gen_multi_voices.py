import asyncio
import edge_tts
import subprocess
import os

parts = [
    {
        "id": "intro",
        "voice": "vi-VN-NamMinhNeural",
        "rate": "+45%",
        "text": "Tại sao người lớn khi ngồi quán ăn hay cà phê, lại hay né tránh ánh mắt của những người bán vé số dạo?",
    },
    {
        "id": "c1",
        "voice": "vi-VN-NamMinhNeural",
        "rate": "+45%",
        "text": "Nói thật là sợ mua mở hàng một người xong là cả quán bu lại. Có hôm ngồi quán ốc, vừa mở ví mua hai tờ cho một cụ già, ba phút sau năm cô chú khác vây quanh bàn mời tiếp. Không mua nữa thì bị nhìn như tội đồ. Từ đó mình học cách né ánh mắt ngay từ đầu.",
    },
    {
        "id": "c2",
        "voice": "vi-VN-HoaiMyNeural",
        "rate": "+45%",
        "text": "Là một đứa hướng nội, cảm giác phải từ chối một người già cúi đầu nài nỉ làm mình stress cả buổi tối. Cắm mặt vào điện thoại vờ bấm phím không phải vì vô cảm, mà vì mình không đủ dũng khí nhìn vào mắt người ta rồi nói chữ: Dạ không.",
    },
    {
        "id": "c3",
        "voice": "vi-VN-NamMinhNeural",
        "rate": "+45%",
        "text": "Lương bảy triệu, tiền trọ ba triệu, cuối tháng tài khoản còn đúng năm mươi ngàn ăn mì gói. Nhiều lúc muốn thương người khác lắm mà nhìn lại ví thấy chính mình còn đáng thương hơn. Trưởng thành là nhận ra bản thân cũng chỉ đang chật vật sinh tồn.",
    },
    {
        "id": "outro",
        "voice": "vi-VN-HoaiMyNeural",
        "rate": "+45%",
        "text": "Còn bạn, khi gặp người bán vé số bạn thường sẽ xử lý thế nào?",
    },
]

async def generate():
    out_dir = r"c:\Users\Dao\Downloads\threads-remotion\public\voice_parts"
    for p in parts:
        filepath = os.path.join(out_dir, f"{p['id']}.mp3")
        print(f"Generating {p['id']} with {p['voice']}...")
        comm = edge_tts.Communicate(text=p['text'], voice=p['voice'], rate=p['rate'])
        await comm.save(filepath)
        print(f"Done {p['id']}")

if __name__ == "__main__":
    asyncio.run(generate())
