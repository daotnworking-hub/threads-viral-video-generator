# 📱 Threads Viral Video Automation (Full HD 1080p • 3s ASMR Scene Switching)

Tự động hóa sản xuất video viral chủ đề Threads (định dạng 9:16 dọc cho TikTok, Reels, YouTube Shorts) với độ phân giải **Full HD (1080x1920)**, cơ chế **chuyển cảnh 3 giây/lần** với kho footage ASMR & Thí nghiệm cuốn hút thị giác và giọng đọc AI đa nhân vật.

---

## ✨ Điểm Nổi Bật

- 🎬 **Chuyển cảnh 3 giây/lần (Chu kỳ Dopamine cao):** Tự động chuyển cảnh liên tục giữa các thước phim ASMR cắt cát động lực học, thái sushi 4K, nhỏ giọt espresso siêu cận, chảo bơ xèo xèo và phản ứng hóa học cầu vồng.
- 📱 **Độ phân giải Full HD (1080 × 1920):** Sắc nét từng chi tiết trên mọi màn hình điện thoại.
- 💬 **1 Thẻ bình luận duy nhất tại mỗi thời điểm:** Đọc tới đâu chuyển sang thẻ đó với hiệu ứng Spring Animation mượt mà.
- 🎨 **Giao diện Threads Light 100% nguyên bản:** Header Threads dạng kính mờ, avatar bo tròn với badge dấu cộng `+`, thống kê tương tác (`♡`, `💬`, `🔁`, `➢`), thanh phản hồi dưới cùng.
- 🎙️ **Giọng đọc AI đa nhân vật:** Luân phiên Giọng Nam (`vi-VN-NamMinhNeural`) và Giọng Nữ (`vi-VN-HoaiMyNeural`), tốc độ 1.35x dứt khoát, âm lượng to rõ.

---

## 🚀 Cài Đặt & Sử Dụng

### 1. Cài đặt thư viện:
```bash
npm install
pip install edge-tts gTTS
```

### 2. Tạo giọng đọc & Timeline:
```bash
python gen_threads_light_voices.py
```

### 3. Tạo montage nền ASMR chuyển cảnh 3s:
```bash
python build_asmr_montage.py
```

### 4. Xuất video hoàn chỉnh:
```bash
npx remotion render ThreadsCommentReader out/threads_asmr_viral_1080p.mp4 --concurrency=4
```

---

## 📂 Cấu Trúc Thư Mục

- `PROMPTS.md`: Lưu trữ toàn bộ Prompt và kịch bản chuẩn cho video.
- `WORKFLOW_GUIDE.md`: Hướng dẫn chi tiết quy trình 3s chuyển cảnh.
- `build_asmr_montage.py`: Script tự động tạo video nền 19 cảnh ASMR 1080p.
- `gen_threads_light_voices.py`: Script Python tạo giọng đọc và đồng bộ hóa frame.
- `src/ThreadsCommentReader.tsx`: Component Remotion Full HD 1080x1920.

---

## 📄 Bản Quyền & Giấy Phép
Dự án được xây dựng và phát triển bởi **daotnworking-hub**.
Giấy phép: MIT License.
