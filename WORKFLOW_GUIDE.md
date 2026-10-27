# Hướng Dẫn Quy Trình Tạo Video Threads Viral Full HD (3s Chuyển Cảnh ASMR)

Tài liệu này hướng dẫn chi tiết quy trình sản xuất video dạng **"Đọc từng thẻ bình luận Threads trên nền video ASMR & Thí nghiệm chuyển cảnh 3 giây/lần"** chuẩn độ phân giải Full HD (1080x1920) tối ưu thuật toán giữ chân người xem của TikTok / Reels / Shorts.

---

## 1. Cơ Chế Giữ Chân Người Xem (High Retention Secret)

1. **Chu kỳ Dopamine 3 giây:** Não bộ người xem mạng xã hội sẽ chán nếu khung hình đứng yên quá 3-4 giây. Bằng cách chuyển cảnh mỗi 3 giây (90 frames) giữa các cảnh ASMR cắt cát động lực học, thái sushi 4K, nhỏ giọt espresso siêu cận, xèo xèo bơ cá hồi và phản ứng hóa học cầu vồng, người xem luôn bị cuốn hút thị giác.
2. **Thẻ đơn Threads Light làm mờ nền:** Thẻ trắng nổi ở trung tâm, đọc tới đâu xuất hiện tới đó với hiệu ứng Spring nảy nhẹ.
3. **Độ phân giải Full HD 1080x1920:** Đảm bảo độ sắc nét tuyệt đối trên mọi màn hình điện thoại cao cấp.

---

## 2. Kiến Trúc Dự Án

```
threads-remotion/
├── PROMPTS.md                   # Tổng hợp prompt và kịch bản chuẩn
├── WORKFLOW_GUIDE.md             # Hướng dẫn chi tiết quy trình
├── README.md                     # Tài liệu dự án
├── build_asmr_montage.py         # Script tự động cắt ghép 19 cảnh ASMR 3s chuẩn 1080p
├── gen_threads_light_voices.py   # Script tạo giọng đọc AI & timeline tự động
├── public/
│   ├── asmr_montage_1080p.mp4   # Video nền 19 cảnh ASMR 1080x1920
│   ├── threads_light_audio.mp3  # Audio đa giọng đọc hoàn chỉnh
│   └── clips/                   # 19 clip cắt 3 giây
└── src/
    ├── Root.tsx                 # Đăng ký Composition
    ├── ThreadsCommentReader.tsx # Component Remotion render 1080x1920
    └── threads_light_timeline.json # File timing tự động
```

---

## 3. Các Bước Vận Hành Tự Động

### Bước 1: Tạo kịch bản & Giọng đọc AI
```bash
python gen_threads_light_voices.py
```
- Sử dụng `edge-tts` với `vi-VN-NamMinhNeural` và `vi-VN-HoaiMyNeural`.
- Tốc độ đọc: `1.35x` dứt khoát, âm lượng: `1.45x`.
- Tự động xuất `threads_light_timeline.json`.

### Bước 2: Tạo Montage Nền ASMR 3 Giây/Cảnh (Full HD)
```bash
python build_asmr_montage.py
```
- Tự động cắt 19 phân đoạn 3.08 giây từ kho footage chất lượng cao:
  - Cắt cát động lực học bằng dao lam (Kinetic Sand ASMR)
  - Đầu bếp Nhật thái cá hồi sashimi 4K
  - Bọt kem Espresso vàng óng chảy siêu cận cảnh (Macro Crema)
  - Chảo bơ nóng xèo xèo cá hồi áp chảo
  - Phản ứng hóa học đổi màu cầu vồng (Rainbow Liquid Experiment)
  - Bàn xoay gốm vuốt đất sét êm dịu (Pottery Wheel)
- Ghép nối thành file `public/asmr_montage_1080p.mp4` chuẩn 1080x1920 @ 30 FPS.

### Bước 3: Render Video Hoàn Thiện
```bash
npx remotion render ThreadsCommentReader out/threads_asmr_viral_1080p.mp4 --concurrency=4
```
Video xuất xưởng tại thư mục `out/` chuẩn Full HD dọc.
