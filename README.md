# 📱 Threads Viral Video Automation (Remotion + AI Voices)

Tự động hóa sản xuất video viral chủ đề Threads (định dạng 9:16 dọc cho TikTok, Reels, YouTube Shorts) với giọng đọc AI đa nhân vật và video nền nấu ăn (Satisfying Cooking B-Roll).

---

## ✨ Điểm Nổi Bật

- 🎨 **Giao diện Threads Light 100% nguyên bản:** Avatar bo tròn với badge dấu cộng `+`, username, dấu tick, reaction heart, thống kê tương tác (`♡`, `💬`, `🔁`, `➢`).
- ⚡ **Từng thẻ bình luận xuất hiện theo giọng đọc:** Đọc tới đâu chuyển thẻ tới đó với hiệu ứng Spring Animation mượt mà.
- 🍳 **Video nền nấu ăn hấp dẫn (Satisfying Cooking B-Roll):** Giữ chân người xem (high retention rate) theo chuẩn thuật toán TikTok / Reels.
- 🎙️ **Giọng đọc AI đa nhân vật:** Luân phiên Giọng Nam (`vi-VN-NamMinhNeural`) và Giọng Nữ (`vi-VN-HoaiMyNeural`), tốc độ 1.35x dứt khoát, âm lượng to rõ.
- ⏱️ **Tự động tính toán Timeline:** Đo thời lượng từng câu thoại bằng `ffprobe` và khớp chính xác từng frame trong Remotion.

---

## 🚀 Cài Đặt & Sử Dụng

### 1. Cài đặt thư viện:
```bash
# Cài đặt Node modules cho Remotion
npm install

# Cài đặt gói Python cho TTS
pip install edge-tts gTTS
```

### 2. Tạo giọng đọc & Timeline:
```bash
python gen_threads_light_voices.py
```

### 3. Xem trước (Preview Remotion Studio):
```bash
npm start
```

### 4. Xuất video hoàn chỉnh:
```bash
npx remotion render ThreadsCommentReader out/threads_cooking_viral.mp4 --concurrency=4
```

---

## 📂 Cấu Trúc Thư Mục

- `PROMPTS.md`: Lưu trữ toàn bộ Prompt và kịch bản chuẩn cho video.
- `WORKFLOW_GUIDE.md`: Hướng dẫn chi tiết từng bước vận hành từ tìm topic đến render.
- `gen_threads_light_voices.py`: Script Python tạo giọng đọc và đồng bộ hóa frame.
- `src/ThreadsCommentReader.tsx`: Component Remotion hiển thị giao diện Threads.
- `public/cooking_bg.mp4`: Video nền nấu ăn chuẩn 9:16.
- `public/threads_light_audio.mp3`: File âm thanh giọng đọc hoàn chỉnh.

---

## 📄 Bản Quyền & Giấy Phép
Dự án được xây dựng và phát triển bởi **daotnworking-hub**.
Giấy phép: MIT License.
