import React from "react";
import {
  AbsoluteFill,
  Audio,
  Composition,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
} from "remotion";
import subtitles from "./subtitles.json";

interface SubtitleCue {
  startFrame: number;
  endFrame: number;
  text: string;
}

export const ThreadsVideoComposition = () => {
  return (
    <Composition
      id="ThreadsViralVideo"
      component={ThreadsVideoComponent}
      durationInFrames={2200}
      fps={30}
      width={720}
      height={1280}
    />
  );
};

export const ThreadsVideoComponent: React.FC = () => {
  const frame = useCurrentFrame();

  // Scene 1: 0 to 1080 (36s)
  // Transition 1: 1050 to 1080 (fade to scene 2)
  // Scene 2: 1050 to 1620 (19s)
  // Transition 2: 1590 to 1620 (fade back to scene 1)
  // Scene 3: 1590 to 2200 (20s)

  // Zoom calculations
  const scaleScene1 = interpolate(frame, [0, 1080], [1.0, 1.1], {
    extrapolateRight: "clamp",
  });
  const scaleScene2 = interpolate(frame, [1050, 1620], [1.02, 1.12], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const scaleScene3 = interpolate(frame, [1590, 2200], [1.08, 1.01], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Opacities for smooth crossfades
  const scene2Opacity = interpolate(frame, [1050, 1080, 1590, 1620], [0, 1, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Current active subtitle
  const activeCue = (subtitles as SubtitleCue[]).find(
    (cue) => frame >= cue.startFrame && frame <= cue.endFrame
  );

  return (
    <AbsoluteFill style={{ backgroundColor: "#0b0b0f", overflow: "hidden" }}>
      {/* Background Audio */}
      <Audio src={staticFile("final_audio.mp3")} />

      {/* Layer 1: Scene 1 / Scene 3 */}
      <AbsoluteFill
        style={{
          transform: `scale(${frame >= 1590 ? scaleScene3 : scaleScene1})`,
          transformOrigin: "center center",
        }}
      >
        <Img
          src={staticFile("bg1.jpg")}
          style={{ width: "100%", height: "100%", objectFit: "cover" }}
        />
      </AbsoluteFill>

      {/* Layer 2: Scene 2 (Weathered hands in rain) with crossfade */}
      <AbsoluteFill
        style={{
          opacity: scene2Opacity,
          transform: `scale(${scaleScene2})`,
          transformOrigin: "center 45%",
        }}
      >
        <Img
          src={staticFile("bg2.jpg")}
          style={{ width: "100%", height: "100%", objectFit: "cover" }}
        />
      </AbsoluteFill>

      {/* Cinematic Vignette */}
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(ellipse at center, rgba(0,0,0,0) 40%, rgba(0,0,0,0.65) 100%)",
          pointerEvents: "none",
        }}
      />

      {/* Bottom Subtitle Overlay */}
      <AbsoluteFill
        style={{
          justifyContent: "flex-end",
          alignItems: "center",
          paddingBottom: 180,
          paddingLeft: 40,
          paddingRight: 40,
        }}
      >
        {activeCue && (
          <div
            style={{
              backgroundColor: "rgba(0, 0, 0, 0.65)",
              backdropFilter: "blur(8px)",
              padding: "16px 28px",
              borderRadius: 20,
              border: "1px solid rgba(255, 255, 255, 0.12)",
              textAlign: "center",
              maxWidth: "92%",
              boxShadow: "0 8px 32px rgba(0, 0, 0, 0.5)",
              animation: "fadeIn 0.15s ease-out",
            }}
          >
            <p
              style={{
                margin: 0,
                color: "#ffffff",
                fontSize: 34,
                fontWeight: 700,
                fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, sans-serif",
                lineHeight: 1.45,
                textShadow: "0 2px 8px rgba(0, 0, 0, 0.8)",
                letterSpacing: "0.2px",
              }}
            >
              {activeCue.text}
            </p>
          </div>
        )}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
