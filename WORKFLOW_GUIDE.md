# Hướng Dẫn Quy Trình Tạo Video Threads Viral Bằng Remotion

Tài liệu này hướng dẫn chi tiết quy trình từ A đến Z để tự động sản xuất video dạng "Đọc bình luận Threads trên nền video nấu ăn (Satisfying Cooking B-Roll)" chuẩn TikTok / Reels / Shorts.

---

## 1. Kiến Trúc Dự Án

```
threads-remotion/
├── PROMPTS.md                   # Tổng hợp prompt và kịch bản chuẩn
├── WORKFLOW_GUIDE.md             # Hướng dẫn chi tiết từng bước
├── README.md                     # Tài liệu tổng quan dự án
├── gen_threads_light_voices.py   # Script tạo giọng đọc AI & timeline tự động
├── public/
│   ├── cooking_bg.mp4           # Video nền chế biến món ăn chuẩn 9:16
│   ├── threads_light_audio.mp3  # Audio hoàn chỉnh gồm các giọng đọc nối tiếp
│   └── voice_parts/             # Các file audio từng phân đoạn
└── src/
    ├── Root.tsx                 # Đăng ký Composition
    ├── ThreadsCommentReader.tsx # Component Remotion render giao diện Threads
    └── threads_light_timeline.json # File lưu frame timing tự động
```

---

## 2. Quy Trình Sản Xuất 4 Bước

### Bước 1: Nghiên Cứu Topic & Viết Script
1. Chọn chủ đề có tính tranh luận cao hoặc chạm vào cảm xúc đời thực trên Threads (tâm lý, mưu sinh, thói quen khó nói...).
2. Cấu trúc bài viết:
   - **OP (Câu hỏi):** Nêu bật hiện tượng gây tò mò ("Tại sao...?").
   - **Bình luận 1 (Tâm lý tự vệ):** Giải thích nguồn gốc cảm xúc sâu xa.
   - **Bình luận 2 (Trải nghiệm thực tế):** Đưa ra tình huống cụ thể (trả lời thì bị chèo kéo dai, im lặng thì người ta đi).
   - **Bình luận 3 (Thấu cảm):** Góc nhìn trưởng thành sau khi tự bươn chải.
   - **Bình luận 4 (Lời kết mở):** Kêu gọi tương tác, bình luận.

### Bước 2: Tạo Giọng Đọc Đa Giọng Bằng Python (`edge-tts`)
Chạy script:
```bash
python gen_threads_light_voices.py
```
- Script tự động kết nối API `edge-tts`:
  - Giọng nam: `vi-VN-NamMinhNeural`
  - Giọng nữ: `vi-VN-HoaiMyNeural`
- Tăng tốc độ đọc lên `1.35x` và kích âm lượng lên `1.45x` bằng `ffmpeg`.
- Đo chính xác thời lượng từng câu và xuất ra file `src/threads_light_timeline.json` (tính theo số frame ở 30 FPS).
- Ghép nối thành file âm thanh hoàn chỉnh `public/threads_light_audio.mp3`.

### Bước 3: Chuẩn Bị Video Nền Nấu Ăn (Cooking B-Roll)
1. Tải clip nấu ăn / chiên rán / cắt thái độ nét cao (Full HD / 4K).
2. Dùng FFmpeg crop và scale chuẩn tỷ lệ 9:16 (720x1280) không dính tạp âm:
```bash
ffmpeg -y -i raw_cooking.webm -vf "scale=-1:1280,crop=720:1280" -an -c:v libx264 -preset fast -crf 20 public/cooking_bg.mp4
```

### Bước 4: Render Bằng Remotion
Component `ThreadsCommentReader.tsx` chịu trách nhiệm:
- Hiển thị video nền nấu ăn chạy mượt mà (`<OffthreadVideo />`).
- Phủ lớp gradient mờ tối để làm nổi bật thẻ bài viết.
- Thẻ bình luận nền trắng Threads Light hiển thị **từng cái một**:
  - Dùng hiệu ứng Spring Physics (`damping: 13, mass: 0.65, stiffness: 135`) để thẻ nảy vào êm ái khi tới lượt đọc.
  - Tự động chuyển thẻ ngay khi dứt câu của người đó.
  - Header Threads làm mờ dạng kính mờ (Frosted Glass).

Chạy lệnh render:
```bash
npx remotion render ThreadsCommentReader out/threads_cooking_viral.mp4 --concurrency=4
```

---

## 3. Khắc Phục Các Lỗi Thường Gặp

1. **Lỗi WSServerHandshakeError trên edge-tts:**
   - Cập nhật gói lên phiên bản mới nhất: `pip install --upgrade edge-tts`.
2. **Lỗi Encoding Unicode trên Windows Terminal:**
   - Thêm `sys.stdout.reconfigure(encoding='utf-8')` vào đầu script Python để in tiếng Việt có dấu an toàn.
3. **Execution Policy của PowerShell với npm:**
   - Dùng `npx.cmd` và `npm.cmd` thay vì `npx` hoặc `npm`.
