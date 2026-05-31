import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
import os

from env_simulator import build_plant

# =====================================
# 输出文件夹
# =====================================
SAVE_DIR = "stability_results"
os.makedirs(SAVE_DIR, exist_ok=True)

Kp = 55.0
Ki = 12.0
Kd = 0.6

s = ctrl.tf('s')

Gp = build_plant()

# PID控制器
C = Kp + Ki/s + Kd*s

# 开环
L = C * Gp

# 闭环
T = ctrl.feedback(L, 1)

# =====================================
# 1. 闭环极点分析
# =====================================
print("\n========== Closed-loop Poles ==========")

poles = ctrl.poles(T)

for i, p in enumerate(poles):
    print(f"Pole {i+1}: {p}")

plt.figure(figsize=(6,6))

plt.scatter(
    np.real(poles),
    np.imag(poles),
    marker='x',
    s=100
)

plt.axvline(0, linestyle='--')
plt.axhline(0, linestyle='--')

plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.title("Closed-loop Pole Map")
plt.grid(True)

plt.savefig(f"{SAVE_DIR}/pole_map.png")
plt.close()

print("pole_map.png 已保存")

# =====================================
# 2. Bode图
# =====================================
print("\n========== Frequency Analysis ==========")

gm, pm, wg, wp = ctrl.margin(L)

print(f"Gain Margin  = {gm}")
print(f"Phase Margin = {pm:.3f} deg")
print(f"Wcg          = {wg}")
print(f"Wcp          = {wp}")

plt.figure()

ctrl.bode_plot(
    L,
    dB=True,
    Hz=False,
    deg=True
)

plt.savefig(f"{SAVE_DIR}/bode_plot.png")
plt.close()

print("bode_plot.png 已保存")

# =====================================
# 3. 闭环性能指标
# =====================================
print("\n========== Closed-loop Performance ==========")

info = ctrl.step_info(T)

for key, value in info.items():
    print(f"{key}: {value}")

print("\n分析完成")
print(f"图片已保存到: {SAVE_DIR}")

# =====================================
# 4. 根轨迹
# =====================================
print("\n========== Rlocus ==========")
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
import os

from env_simulator import build_plant

# =====================================
# 输出文件夹
# =====================================
SAVE_DIR = "stability_results"
os.makedirs(SAVE_DIR, exist_ok=True)

Kp = 55.0
Ki = 12.0
Kd = 0.6

s = ctrl.tf('s')

Gp = build_plant()

# PID控制器
C = Kp + Ki/s + Kd*s

# 开环
L = C * Gp

# 闭环
T = ctrl.feedback(L, 1)

# =====================================
# 1. 闭环极点分析
# =====================================
print("\n========== Closed-loop Poles ==========")

poles = ctrl.poles(T)

for i, p in enumerate(poles):
    print(f"Pole {i+1}: {p}")

plt.figure(figsize=(6,6))

plt.scatter(
    np.real(poles),
    np.imag(poles),
    marker='x',
    s=100
)

plt.axvline(0, linestyle='--')
plt.axhline(0, linestyle='--')

plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.title("Closed-loop Pole Map")
plt.grid(True)

plt.savefig(f"{SAVE_DIR}/pole_map.png")
plt.close()

print("pole_map.png 已保存")

# =====================================
# 2. Bode图
# =====================================
print("\n========== Frequency Analysis ==========")

gm, pm, wg, wp = ctrl.margin(L)

print(f"Gain Margin  = {gm}")
print(f"Phase Margin = {pm:.3f} deg")
print(f"Wcg          = {wg}")
print(f"Wcp          = {wp}")

plt.figure()

ctrl.bode_plot(
    L,
    dB=True,
    Hz=False,
    deg=True
)

plt.savefig(f"{SAVE_DIR}/bode_plot.png")
plt.close()

print("bode_plot.png 已保存")

# =====================================
# 3. 闭环性能指标
# =====================================
print("\n========== Closed-loop Performance ==========")

info = ctrl.step_info(T)

for key, value in info.items():
    print(f"{key}: {value}")

print("\n分析完成")
print(f"图片已保存到: {SAVE_DIR}")

# =====================================
# 4. 根轨迹
# =====================================
print("\n========== Root Locus ==========")
plt.figure(figsize=(7,6))
ctrl.root_locus(L, grid=True)
plt.title("Root Locus")
plt.savefig(f"{SAVE_DIR}/root_locus.png")
plt.close()
print("root_locus.png 已保存")

# =====================================
# 5. Nyquist Plot
# =====================================
print("\n========== Nyquist Analysis ==========")
plt.figure(figsize=(7,7))
ctrl.nyquist_plot(L)
plt.grid(True)
plt.title("Nyquist Plot")
plt.savefig(f"{SAVE_DIR}/nyquist_plot.png")
plt.close()
print("nyquist_plot.png 已保存")

