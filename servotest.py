import time
import ypwm  # 假設你正在使用的舵機控制庫

# 測試舵機在水平軸和垂直軸的運動

def test_servo():
    # 測試水平軸 (H_channel = 0)
    print("測試水平軸...")
    for angle in range(0, 181, 30):  # 從 0 到 180 度，每次步進 30 度
        ypwm.Servo180(0, angle)
        print(f"水平軸移動到 {angle} 度")
        time.sleep(1)  # 等待 1 秒鐘，觀察舵機移動

    # 測試垂直軸 (V_channel = 1)
    print("測試垂直軸...")
    for angle in range(50, 101, 10):  # 從 50 到 100 度，每次步進 10 度
        ypwm.Servo180(1, angle)
        print(f"垂直軸移動到 {angle} 度")
        time.sleep(1)

if __name__ == "__main__":
    print("開始舵機測試")
    test_servo()
    print("舵機測試完成")
