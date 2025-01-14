import librosa
import numpy as np
import matplotlib.pyplot as plt

# 讀取音頻文件
audio_path = "C:/Users/Leju/Desktop/test/RGBL/yin-cha.mp3"  # 你的音頻文件
y, sr = librosa.load(audio_path, sr=None)  # sr=None 保持原始採樣率

# 轉換為頻譜 (Short-Time Fourier Transform)
D = np.abs(librosa.stft(y))

# 繪製頻譜
plt.figure(figsize=(10, 5))
librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), sr=sr, y_axis='log', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('音頻頻譜圖')
plt.xlabel('時間')
plt.ylabel('頻率')
plt.show()

# 頻率範圍（Hz）
low_freq = (20, 200)      # 低頻
mid_freq = (200, 4000)    # 中頻（人聲主要區間）
high_freq = (4000, 20000) # 高頻

# 轉換頻率索引
def get_freq_index(freq_range, sr, n_fft=2048):
    return (int(freq_range[0] / (sr / n_fft)), int(freq_range[1] / (sr / n_fft)))

low_idx = get_freq_index(low_freq, sr)
mid_idx = get_freq_index(mid_freq, sr)
high_idx = get_freq_index(high_freq, sr)

# 提取頻率區段
D_low = D[low_idx[0]:low_idx[1], :]
D_mid = D[mid_idx[0]:mid_idx[1], :]
D_high = D[high_idx[0]:high_idx[1], :]

# 計算能量
low_energy = np.mean(D_low)
mid_energy = np.mean(D_mid)
high_energy = np.mean(D_high)

print(f"低頻能量: {low_energy:.2f}")
print(f"中頻能量: {mid_energy:.2f}")
print(f"高頻能量: {high_energy:.2f}")

import librosa.display

# 計算音量
rms = librosa.feature.rms(y=y)

# 畫圖
plt.figure(figsize=(10, 4))
plt.plot(rms[0], label="音量 (RMS)")
plt.title("音量變化圖")
plt.xlabel("時間")
plt.ylabel("音量")
plt.legend()
plt.show()
