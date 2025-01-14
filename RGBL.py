import numpy as np
import cv2

def weighted_average(block):
    """對一個 50x50 區塊應用加權平均，中央係數最高，向外遞減"""
    size = block.shape[0]  # 這應該是 50
    weights = np.zeros((size, size), dtype=np.float32)

    # 計算權重，中央最高，向外遞減
    for i in range(size):
        for j in range(size):
            # 計算與中心的距離
            dist = np.sqrt((i - size // 2) ** 2 + (j - size // 2) ** 2)
            weights[i, j] = 1 / (1 + dist)  # 距離越遠，權重越小（避免除 0）

    # 正規化權重
    weights /= np.sum(weights)

    # 計算加權平均
    return np.sum(block * weights)

def downscale_image(image, block_size=50):
    """將圖片壓縮，每個 50x50 區塊變成 1 個像素"""
    h, w = image.shape[:2]
    new_h, new_w = h // block_size, w // block_size  # 降維後的新尺寸

    reduced_image = np.zeros((new_h, new_w), dtype=np.float32)

    for i in range(new_h):
        for j in range(new_w):
            block = image[i * block_size:(i + 1) * block_size, j * block_size:(j + 1) * block_size]
            reduced_image[i, j] = weighted_average(block)

    return reduced_image

def load_and_convert_image(image_path):
    """讀取圖片並轉換成降維的 R, G, B, L 矩陣"""
    img = cv2.imread(image_path)

    # 轉換為 RGB 格式
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    R, G, B = img_rgb[:, :, 0], img_rgb[:, :, 1], img_rgb[:, :, 2]

    # 轉換為灰階（亮度矩陣）
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 壓縮 R, G, B, L 矩陣
    R_small = downscale_image(R)
    G_small = downscale_image(G)
    B_small = downscale_image(B)
    L_small = downscale_image(img_gray)

    return R_small, G_small, B_small, L_small

# 測試用
image_path = "C:/Users/Leju/Desktop/test/RGBL/HermannGrid.png"  # 你的赫爾曼方格圖片
R, G, B, L = load_and_convert_image(image_path)

# 顯示結果
print("R 矩陣（降維後）：\n", R)
print("G 矩陣（降維後）：\n", G)
print("B 矩陣（降維後）：\n", B)
print("L 矩陣（亮度，降維後）：\n", L)
