from gpiozero import Servo, Motor
from time import sleep

# 서보 모터와 DC 모터 설정
servo = Servo(18)  # 서보 모터 제어 핀
motor = Motor(forward=23, backward=24)  # DC 모터 전진/후진 핀

# 서보 모터 제어 로직
print("서보 모터: 방향 전환 테스트")
servo.min()  # 왼쪽 방향
sleep(1)
servo.max()  # 오른쪽 방향
sleep(1)
servo.mid()  # 중앙
sleep(1)

# DC 모터 제어 로직
print("DC 모터: 이동 제어 테스트")
motor.forward(speed=0.5)  # 50% 속도로 전진
sleep(2)
motor.backward(speed=0.5)  # 50% 속도로 후진
sleep(2)
motor.stop()  # 정지
