import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
import matplotlib.animation as animation

MAX_STEP = 1000 # 実行するステップ数
TRAVEL_DISTANCE = 0.01 # 移動距離
RADIUS = 1 # 半径
EXTENSION = 1.1 # グラフの表示領域をちょうどよく広げるための定数

fig, ax = plt.subplots(figsize=(6,6))

pos = np.zeros(2) # 玉の位置
dir = np.zeros(2) # 玉の移動方向

# ボールの初期位置を決定
while True:
    x = np.random.uniform(-RADIUS, RADIUS)
    y = np.random.uniform(-RADIUS, RADIUS)

    if math.sqrt(x**2 + y**2) <= 1.:
        pos[:] = [x, y]
        break

sc = ax.scatter(pos[0], pos[1])

ax.set_xlim(-RADIUS*EXTENSION, RADIUS*EXTENSION) # x軸の表示範囲
ax.set_ylim(-RADIUS*EXTENSION, RADIUS*EXTENSION) # y軸の表示範囲

title = ax.set_title("Frame: 0")

def update(frame):
    global pos

    while True:
        dx = np.random.uniform(-TRAVEL_DISTANCE, TRAVEL_DISTANCE)
        dy = np.random.uniform(-TRAVEL_DISTANCE, TRAVEL_DISTANCE)

        new_pos = pos + np.array([dx, dy])

        if np.linalg.norm(new_pos) <= 1.0:
            pos = new_pos
            break
    
    title.set_text(f"Frame: {frame}")

    # 散布図のデータ更新
    sc.set_offsets([pos])
    return sc, title

# アニメーション実行
ani = animation.FuncAnimation(fig, update, frames=MAX_STEP, interval=50, blit=True)

c = patches.Circle(xy=(0,0), radius=RADIUS, fill=False)
ax.add_patch(c)
plt.show()
# ani.save('circle_ball.gif', writer='pillow')