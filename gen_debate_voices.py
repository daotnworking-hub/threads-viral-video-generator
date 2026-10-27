import asyncio
import edge_tts
import subprocess
import os

parts = [
    {
        "id": "d_intro",
        "voice": "vi-VN-NamMinhNeural",
        "rate": "+45%",
        "text": "Tại sao người lớn lại hay né tránh ánh mắt của những người bán vé số dạo?",
    },
    {
        "id": "d_c1",
        "voice": "vi-VN-NamMinhNeural",
        "rate": "+45%",
        "text": "Không mua thì nói một câu lịch sự, việc gì phải giả vờ cắm mặt vào điện thoại? Người ta đi bán kiếm sống chứ có ăn xin của mấy người đâu mà làm thái độ tránh như tránh tà vậy? Bớt đạo đức giả lại đi!",
    },
    {
        "id": "d_c2",
        "voice": "vi-VN-HoaiMyNeural",
        "rate": "+45%",
        "text": "Nói thì hay lắm! Thử một bữa ngồi ăn bị cả chục người dí vé số vào tận mặt xem. Lắc đầu từ chối nhẹ nhàng thì bị lườm nguýt, có khi còn bị chửi đổng. Tiền của tôi, thời gian của tôi, việc gì tôi phải tiếp chuyện để rước bực vào người?",
    },
    {
        "id": "d_c3",
        "voice": "vi-VN-NamMinhNeural",
        "rate": "+45%",
        "text": "Mấy bạn bớt ngây thơ lại đi! Ở thành phố đầy đường dây chăn dắt người già với trẻ con bán vé số. Cứ nghĩ mình mua là làm phước, thực chất là đang tiếp tay nuôi béo mấy thằng bảo kê đứng ở góc đường kia kìa!",
    },
    {
        "id": "d_outro",
        "voice": "vi-VN-HoaiMyNeural",
        "rate": "+45%",
        "text": "Một bên nói vô cảm, một bên bảo tự vệ. Theo bạn, ai mới là người nói đúng?",
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
