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

### Bước 2: Tạo Montage Nền Đa Chủ Đề (Vũ Trụ • ASMR • Ẩm Thực) Chuyển Cảnh 3 Giây
```bash
python build_asmr_montage.py
```
- Tự động cắt và ghép 19 phân đoạn 3.08 giây từ các chủ đề hot trend thị giác cao:
  - **Thiên văn & Vũ trụ sâu:** Mô phỏng Lỗ đen 4K (NASA Goddard), Du hành Tinh vân (Bubble Nebula 3D), Dải lụa Cực quang phương Bắc (Aurora Borealis).
  - **Thí nghiệm khoa học & ASMR:** Tinh thể tuyết đóng băng bong bóng xà phòng siêu cận cảnh, Dao lam cạo cát động lực học, Phản ứng đổi màu hóa học cầu vồng.
  - **Ẩm thực & Chế biến:** Dao bếp thái cá hồi Sashimi 4K, Nhỏ giọt Espresso Crema vàng óng, Cá hồi áp chảo bơ xèo xèo.
  - **Thủ công nghệ thuật:** Bàn xoay vuốt gốm đất sét mượt mà.
- Ghép nối thành file `public/asmr_montage_1080p.mp4` chuẩn 1080x1920 @ 30 FPS không dính tạp âm bản quyền.

### Bước 3: Render Video Hoàn Thiện
```bash
npx remotion render ThreadsCommentReader out/threads_asmr_viral_1080p.mp4 --concurrency=4
```
Video xuất xưởng tại thư mục `out/` chuẩn Full HD dọc.
