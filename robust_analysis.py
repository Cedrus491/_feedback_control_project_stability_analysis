import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
import os

def build_plant(JL_new):
    """
    根据物理参数和推导出的传递函数，构建飞行器姿态被控对象 Gp(s)
    """
    s = ctrl.tf('s')
    
    # 物理参数录入
    Ks = 1.0
    K = 181.17      # 题目中指定的前置放大器增益
    K1 = 10.0
    K2 = 0.5
    Kt = 0.0        # 测速反馈系数为0，大幅简化分母
    Ra = 5.0
    La = 0.003
    Ki = 9.0
    Kb = 0.0636
    Jm = 0.0001
    JL = 0.01
    Bm = 0.005
    BL = 1.0
    N = 110.0
    
    # 计算折算到电机轴的总惯量和总摩擦
    Jt = Jm + (N**2) * JL
    Bt = Bm + (N**2) * BL
    
    # 根据手推公式构建开环传递函数 (包含 K=181.17)
    # 分子：N * K * K1 * Ks * Ki
    num = N * K * K1 * Ks * Ki
    
    # 分母：s * [ (Ra + La*s + K1*K2)*(Jt*s + Bt) + Ki*Kb ] (Kt=0的简化版)
    den_term1 = (Ra + La * s + K1 * K2) * (Jt * s + Bt)
    den_term2 = Ki * Kb
    
    Gp = num / (s * (den_term1 + den_term2))
    
    return Gp

# =====================================
# 输出文件夹
# =====================================
SAVE_DIR = "stability_results"
os.makedirs(SAVE_DIR, exist_ok=True)

Kp = 55.0
Ki = 12.0
Kd = 0.6

s = ctrl.tf('s')

Gp_original = build_plant(0.01)
Gp_high = build_plant(0.012)
Gp_low = build_plant(0.008)

# PID控制器
C = Kp + Ki/s + Kd*s

# 开环
L_original = C * Gp_original
L_high = C * Gp_high
L_low = C * Gp_low

# 闭环
T_original = ctrl.feedback(L_original, 1)
T_high = ctrl.feedback(L_high, 1)
T_low = ctrl.feedback(L_low, 1)
t = np.linspace(0,0.05,3000)

t1,y1 = ctrl.step_response(T_original,t)
t2,y2 = ctrl.step_response(T_high,t)
t3,y3 = ctrl.step_response(T_low,t)

plt.figure(figsize=(8,5))

plt.plot(t1,y1,label='Original')

plt.plot(t2,y2,label='JL +20%')

plt.plot(t3,y3,label='JL -20%')

plt.grid(True)

plt.xlabel("Time (s)")
plt.ylabel("Response")
plt.title("Robustness Analysis")
plt.legend()
plt.savefig("robustness_JL.png")