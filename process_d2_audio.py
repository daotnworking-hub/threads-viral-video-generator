import subprocess
import json
import os

dir_path = r"c:\Users\Dao\Downloads\threads-remotion\public\voice_parts"
files = ["d2_intro.mp3", "d2_c1.mp3", "d2_c2.mp3", "d2_c3.mp3", "d2_c4.mp3", "d2_outro.mp3"]

durations = {}
for f in files:
    fp = os.path.join(dir_path, f)
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        fp
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    durations[f] = float(res.stdout.strip())
    print(f"{f}: {durations[f]:.3f}s")

gap = 0.28
timeline = []
cur_time = 0.0

sections = [
    ("intro", "d2_intro.mp3"),
    ("c1", "d2_c1.mp3"),
    ("c2", "d2_c2.mp3"),
    ("c3", "d2_c3.mp3"),
    ("c4", "d2_c4.mp3"),
    ("outro", "d2_outro.mp3")
]

for sec_id, fname in sections:
    dur = durations[fname]
    start_t = cur_time
    end_t = cur_time + dur
    timeline.append({
        "id": sec_id,
        "file": fname,
        "start": start_t,
        "end": end_t,
        "duration": dur,
        "startFrame": int(round(start_t * 30)),
        "endFrame": int(round(end_t * 30))
    })
    cur_time = end_t + gap

total_dur = cur_time
total_frames = int(round(total_dur * 30))

print("\n=== DEEP EXPLANATION TIMELINE (30 FPS) ===")
for item in timeline:
    print(f"{item['id']}: {item['start']:.2f}s -> {item['end']:.2f}s | Frame {item['startFrame']} -> {item['endFrame']}")
print(f"Total duration: {total_dur:.2f}s ({total_frames} frames)")

with open(r"c:\Users\Dao\Downloads\threads-remotion\src\d2_timeline.json", "w", encoding="utf-8") as out_f:
    json.dump({
        "totalDuration": total_dur,
        "totalFrames": total_frames,
        "sections": timeline
    }, out_f, indent=2)

filter_chains = []
for i, item in enumerate(timeline):
    delay_ms = int(item['start'] * 1000)
    filter_chains.append(f"[{i}:a]adelay={delay_ms}|{delay_ms}[a{i}]")

inputs_str = "".join([f"[a{i}]" for i in range(len(timeline))])
filter_chains.append(f"{inputs_str}amix=inputs={len(timeline)}:normalize=0[voice_raw]")
# Voice loud and clear
filter_chains.append("[voice_raw]volume=1.45[voice_boosted]")

bg_music = r"c:\Users\Dao\Downloads\threads_viral_video\bg_music.wav"
filter_chains.append(f"[{len(timeline)}:a]volume=0.18[m]")
filter_chains.append(f"[{len(timeline)+1}:a]volume=0.08[r]")
filter_chains.append(f"[voice_boosted][m][r]amix=inputs=3:duration=first:dropout_transition=2[final_a]")

full_filter = ";".join(filter_chains)

input_args = []
for sec_id, fname in sections:
    input_args.extend(["-i", os.path.join(dir_path, fname)])

input_args.extend(["-i", bg_music])
input_args.extend(["-f", "lavfi", "-i", f"anoisesrc=d={int(total_dur)+2}:c=pink:r=44100:a=0.015,lowpass=f=1200,highpass=f=250"])

out_audio = r"c:\Users\Dao\Downloads\threads-remotion\public\deep_debate_final_audio.mp3"

ffmpeg_cmd = [
    "ffmpeg", "-y",
    *input_args,
    "-filter_complex", full_filter,
    "-map", "[final_a]",
    "-t", f"{total_dur:.2f}",
    out_audio
]

print("\nRunning FFmpeg audio mix...")
subprocess.run(ffmpeg_cmd, check=True)
print("deep_debate_final_audio.mp3 created successfully!")
