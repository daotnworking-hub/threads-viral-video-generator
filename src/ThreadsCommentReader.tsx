import React from "react";
import {
  AbsoluteFill,
  Audio,
  Composition,
  interpolate,
  OffthreadVideo,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

export const ThreadsCommentReaderComposition = () => {
  return (
    <Composition
      id="ThreadsCommentReader"
      component={ThreadsCommentReaderComponent}
      durationInFrames={1724}
      fps={30}
      width={1080}
      height={1920}
    />
  );
};

interface CardSegment {
  id: string;
  isPost?: boolean;
  startFrame: number;
  endFrame: number;
  author: string;
  handle: string;
  avatarBg: string;
  avatarChar: string;
  time: string;
  likes: string;
  replies: string;
  reposts: string;
  shares: string;
  text: string;
}

const CARDS: CardSegment[] = [
  {
    id: "post",
    isPost: true,
    startFrame: 10,
    endFrame: 172,
    author: "Chuyện Người Lớn",
    handle: "chuyennguoilon.vn",
    avatarBg: "linear-gradient(135deg, #111111 0%, #333333 100%)",
    avatarChar: "C",
    time: "5h",
    likes: "58,7K",
    replies: "5,2K",
    reposts: "19,8K",
    shares: "17,9K",
    text: "Tại sao người lớn khi ngồi quán ăn hay cà phê, thường có thói quen né tránh ánh mắt của những người bán vé số dạo?",
  },
  {
    id: "c1",
    startFrame: 181,
    endFrame: 605,
    author: "Minh Trí",
    handle: "minhtri.journey",
    avatarBg: "linear-gradient(135deg, #1e3c72, #2a5298)",
    avatarChar: "T",
    time: "4h",
    likes: "19,8K",
    replies: "542",
    reposts: "2,1K",
    shares: "1,4K",
    text: "Không phải vì vô tâm hay coi thường đâu bạn. Người lớn né tránh là vì họ sợ lòng trắc ẩn của chính mình.\n\nNhiều khi trong ví chỉ còn vài chục nghìn lo cho ngày mai, nhìn vào đôi mắt khắc khổ của các cô chú là mềm lòng ngay. Né đi là cách để bảo vệ bản thân khỏi cảm giác bất lực vì muốn giúp mà không đủ sức.",
  },
  {
    id: "c2",
    startFrame: 613,
    endFrame: 1118,
    author: "Hoàng Mai",
    handle: "hoangmai.life",
    avatarBg: "linear-gradient(135deg, #ee0979, #ff6a00)",
    avatarChar: "M",
    time: "3h",
    likes: "28,5K",
    replies: "912",
    reposts: "4,2K",
    shares: "3,1K",
    text: "Chuẩn luôn bạn ơi. Với lại ở quán xá có một thực tế là: chỉ cần bạn ngước lên trả lời một câu dù rất lịch sự, người ta cũng sẽ thấy có hy vọng và đứng lại nài nỉ, chèo kéo rất lâu.\n\nCòn nếu mình vờ không nghe, không nhìn thì người ta mời một lúc không thấy tín hiệu rồi sẽ tự rời đi. Người lớn né tránh là để không rơi vào tình huống khó xử cho cả hai bên.",
  },
  {
    id: "c3",
    startFrame: 1126,
    endFrame: 1472,
    author: "Quang Huy",
    handle: "quanghuy.story",
    avatarBg: "linear-gradient(135deg, #0ba360, #3cba92)",
    avatarChar: "H",
    time: "2h",
    likes: "35,2K",
    replies: "1,2K",
    reposts: "5,4K",
    shares: "4,1K",
    text: "Đúng vậy ạ. Hồi nhỏ mình cũng trách sao người lớn lạnh lùng thế. Đến khi tự đi làm kiếm từng đồng, gánh vác tiền nhà tiền điện mới hiểu.\n\nÁnh mắt né tránh đó không phải là lạnh nhạt, mà là một tiếng thở dài bất lực của những người lớn cũng đang chật vật mưu sinh.",
  },
  {
    id: "c4",
    startFrame: 1480,
    endFrame: 1670,
    author: "Thanh Thảo",
    handle: "thanhthao_talks",
    avatarBg: "linear-gradient(135deg, #7F00FF, #E100FF)",
    avatarChar: "S",
    time: "1h",
    likes: "12,6K",
    replies: "315",
    reposts: "1,1K",
    shares: "890",
    text: "Mỗi người một hoàn cảnh, từ chối hay ủng hộ đều cần sự tôn trọng.\n\nCòn bạn, bạn nghĩ sao về thói quen này của người lớn?",
  },
];

export const ThreadsCommentReaderComponent: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Find currently active card (1 card on screen at a time)
  const activeCard = CARDS.find((c) => frame >= c.startFrame - 4 && frame <= c.endFrame + 6);
  const isOutro = frame > 1672;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#000000",
        overflow: "hidden",
        fontFamily:
          "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
      }}
    >
      {/* Crisp Multi-Voice Audio */}
      <Audio src={staticFile("threads_light_audio.mp3")} />

      {/* Dynamic 1080p Fast-Paced Montage Background (Cuts every 3s: ASMR Kinetic Sand, Sizzling Salmon, Wok Fire, Rainbow Liquid) */}
      <AbsoluteFill>
        <OffthreadVideo
          src={staticFile("asmr_montage_1080p.mp4")}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
          }}
        />
      </AbsoluteFill>

      {/* Cinematic Contrast Vignette to guarantee 100% card readability */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(to bottom, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0.2) 30%, rgba(0,0,0,0.25) 70%, rgba(0,0,0,0.7) 100%)",
          pointerEvents: "none",
        }}
      />

      {/* Top Floating Threads Brand Header (Frosted Glass Pill) */}
      <div
        style={{
          position: "absolute",
          top: 72,
          left: 0,
          right: 0,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          zIndex: 30,
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 14,
            backgroundColor: "rgba(255, 255, 255, 0.94)",
            backdropFilter: "blur(24px)",
            padding: "12px 38px",
            borderRadius: 40,
            boxShadow: "0 12px 40px rgba(0, 0, 0, 0.28)",
            border: "1.5px solid rgba(255, 255, 255, 0.9)",
          }}
        >
          {/* Threads Logo */}
          <svg width="36" height="36" viewBox="0 0 192 192" fill="none">
            <path
              d="M141.537 88.9883C140.71 88.5919 139.87 88.2104 139.019 87.8451C137.537 60.5382 122.616 44.905 97.5619 44.745C97.4121 44.7441 97.2625 44.7437 97.1132 44.7437C70.0805 44.7437 53.0784 62.9067 53.0784 94.7554C53.0784 126.604 70.0805 144.767 97.1132 144.767C114.779 144.767 128.272 136.212 135.215 120.579L120.301 112.55C115.65 122.955 106.914 128.093 96.9634 128.093C79.8454 128.093 69.7521 114.869 69.7521 94.7554C69.7521 74.6419 79.8454 61.4178 96.9634 61.4178C112.275 61.5152 121.579 71.0592 122.766 89.9678C117.382 91.5645 107.031 93.6496 95.8344 94.1375C73.4357 95.1134 59.9922 105.793 59.9922 121.737C59.9922 137.037 72.8464 148.293 90.9636 148.293C111.458 148.293 124.938 135.854 129.626 123.682C133.565 137.893 145.451 146.402 161.42 146.402C177.389 146.402 189.275 135.342 189.275 119.398C189.275 103.454 177.389 92.394 161.42 92.394C157.065 92.394 152.923 93.3031 149.102 94.945C148.47 91.9566 147.247 89.2065 145.495 86.8797L141.537 88.9883ZM93.1872 132.327C81.8211 132.327 75.2974 125.867 75.2974 116.326C75.2974 106.786 82.8088 100.222 96.6577 99.6198C104.992 99.2562 112.721 97.9405 118.239 96.6346C117.204 118.423 107.185 132.327 93.1872 132.327Z"
              fill="#000000"
            />
          </svg>
          <span style={{ fontSize: 30, fontWeight: 800, color: "#000000", letterSpacing: -0.4 }}>
            Threads
          </span>
        </div>
      </div>

      {/* Main Single Active Comment Card Container */}
      <div
        style={{
          position: "absolute",
          top: "48%",
          left: 44,
          right: 44,
          transform: "translateY(-50%)",
          zIndex: 20,
        }}
      >
        {activeCard && (() => {
          // Spring entrance
          const enterSpring = spring({
            frame: frame - activeCard.startFrame,
            fps,
            config: { damping: 13, mass: 0.65, stiffness: 135 },
          });

          // Exit fade
          const exitOpacity = interpolate(
            frame,
            [activeCard.endFrame - 6, activeCard.endFrame],
            [1, 0],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
          );

          const scale = interpolate(enterSpring, [0, 1], [0.88, 1]);
          const translateY = interpolate(enterSpring, [0, 1], [50, 0]);

          return (
            <div
              key={activeCard.id}
              style={{
                backgroundColor: "#FFFFFF",
                borderRadius: 36,
                padding: "38px 36px 30px 36px",
                boxShadow:
                  "0 35px 90px rgba(0, 0, 0, 0.48), 0 0 35px rgba(255, 255, 255, 0.2)",
                border: "1.5px solid rgba(255, 255, 255, 0.95)",
                transform: `scale(${scale}) translateY(${translateY}px)`,
                opacity: enterSpring * exitOpacity,
              }}
            >
              {/* Header: Avatar, Name, Handle, Time, Reaction */}
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "space-between",
                  marginBottom: 24,
                }}
              >
                <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
                  {/* Avatar with Threads Plus Badge */}
                  <div style={{ position: "relative" }}>
                    <div
                      style={{
                        width: 70,
                        height: 70,
                        borderRadius: "50%",
                        background: activeCard.avatarBg,
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        color: "#FFFFFF",
                        fontWeight: 800,
                        fontSize: 30,
                      }}
                    >
                      {activeCard.avatarChar}
                    </div>
                    {/* Iconic Black + badge */}
                    <div
                      style={{
                        position: "absolute",
                        bottom: -2,
                        right: -2,
                        width: 25,
                        height: 25,
                        borderRadius: "50%",
                        backgroundColor: "#000000",
                        border: "3px solid #FFFFFF",
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        color: "#FFFFFF",
                        fontSize: 17,
                        fontWeight: 900,
                        lineHeight: 1,
                      }}
                    >
                      +
                    </div>
                  </div>

                  <div>
                    <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                      <span
                        style={{
                          fontSize: 28,
                          fontWeight: 700,
                          color: "#000000",
                          letterSpacing: -0.3,
                        }}
                      >
                        {activeCard.author}
                      </span>
                      <span style={{ fontSize: 20, color: "#888888" }}>•</span>
                      <span style={{ fontSize: 20, color: "#777777" }}>{activeCard.time}</span>
                    </div>
                    <span style={{ fontSize: 20, color: "#777777", fontWeight: 400 }}>
                      @{activeCard.handle}
                    </span>
                  </div>
                </div>

                {/* Right Badge: Reaction Heart Pill & Dots */}
                <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                  <div
                    style={{
                      display: "flex",
                      alignItems: "center",
                      gap: 6,
                      backgroundColor: "#FFF0F2",
                      padding: "6px 16px",
                      borderRadius: 20,
                    }}
                  >
                    <span style={{ color: "#E0245E", fontSize: 20 }}>❤️</span>
                    <span style={{ color: "#E0245E", fontSize: 19, fontWeight: 700 }}>
                      {activeCard.likes}
                    </span>
                  </div>
                  <span style={{ fontSize: 28, color: "#888888" }}>•••</span>
                </div>
              </div>

              {/* Comment Content Body */}
              <div
                style={{
                  fontSize: activeCard.isPost ? 35 : 32,
                  fontWeight: activeCard.isPost ? 650 : 500,
                  lineHeight: 1.55,
                  color: "#111111",
                  marginBottom: 26,
                  whiteSpace: "pre-line",
                  letterSpacing: -0.2,
                }}
              >
                {activeCard.text}
              </div>

              {/* Bottom Action Bar */}
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 32,
                  paddingTop: 20,
                  borderTop: "1.5px solid #F0F0F0",
                }}
              >
                {/* Heart */}
                <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#222222" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
                  </svg>
                  <span style={{ fontSize: 22, fontWeight: 600, color: "#222222" }}>{activeCard.likes}</span>
                </div>

                {/* Reply */}
                <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#222222" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" />
                  </svg>
                  <span style={{ fontSize: 22, fontWeight: 600, color: "#222222" }}>{activeCard.replies}</span>
                </div>

                {/* Repost */}
                <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#222222" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M17 1l4 4-4 4" />
                    <path d="M3 11V9a4 4 0 0 1 4-4h14" />
                    <path d="M7 23l-4-4 4-4" />
                    <path d="M21 13v2a4 4 0 0 1-4 4H3" />
                  </svg>
                  <span style={{ fontSize: 22, fontWeight: 600, color: "#222222" }}>{activeCard.reposts}</span>
                </div>

                {/* Share */}
                <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#222222" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
                    <line x1="22" y1="2" x2="11" y2="13" />
                    <polygon points="22 2 15 22 11 13 2 9 22 2" />
                  </svg>
                  <span style={{ fontSize: 22, fontWeight: 600, color: "#222222" }}>{activeCard.shares}</span>
                </div>
              </div>
            </div>
          );
        })()}

        {/* Outro Call-to-action Card */}
        {isOutro && (
          <div
            style={{
              backgroundColor: "rgba(255, 255, 255, 0.96)",
              backdropFilter: "blur(20px)",
              borderRadius: 36,
              padding: "44px 36px",
              textAlign: "center",
              boxShadow: "0 35px 90px rgba(0,0,0,0.48)",
              border: "1.5px solid rgba(255, 255, 255, 0.95)",
            }}
          >
            <div style={{ fontSize: 60, marginBottom: 16 }}>💬</div>
            <div style={{ fontSize: 36, fontWeight: 800, color: "#000000", marginBottom: 14 }}>
              Góc nhìn của bạn là gì?
            </div>
            <div style={{ fontSize: 27, color: "#444444", lineHeight: 1.5 }}>
              Bạn nghĩ người lớn né tránh là để tự vệ hay vô tâm? Hãy chia sẻ bên dưới nhé! 👇
            </div>
          </div>
        )}
      </div>

      {/* Floating Bottom Engagement Bar (Threads Style) */}
      <div
        style={{
          position: "absolute",
          bottom: 52,
          left: 44,
          right: 44,
          height: 84,
          backgroundColor: "rgba(255, 255, 255, 0.93)",
          backdropFilter: "blur(24px)",
          borderRadius: 42,
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          paddingLeft: 32,
          paddingRight: 22,
          boxShadow: "0 14px 45px rgba(0,0,0,0.32)",
          border: "1.5px solid rgba(255, 255, 255, 0.85)",
          zIndex: 30,
        }}
      >
        <span style={{ color: "#777777", fontSize: 23, fontWeight: 500 }}>
          Gửi câu trả lời cho chủ bài viết...
        </span>
        <div
          style={{
            width: 54,
            height: 54,
            borderRadius: "50%",
            backgroundColor: "#000000",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <line x1="22" y1="2" x2="11" y2="13" />
            <polygon points="22 2 15 22 11 13 2 9 22 2" />
          </svg>
        </div>
      </div>
    </AbsoluteFill>
  );
};
