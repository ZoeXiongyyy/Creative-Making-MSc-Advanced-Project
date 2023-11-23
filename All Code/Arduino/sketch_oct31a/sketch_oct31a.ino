#include <NewPing.h>
#include <Servo.h>

#define TRIGGER_PIN1  2  // 第一个超声波传感器的触发引脚
#define ECHO_PIN1     3  // 第一个超声波传感器的回声引脚
#define TRIGGER_PIN2  4  // 第二个超声波传感器的触发引脚
#define ECHO_PIN2     5  // 第二个超声波传感器的回声引脚
#define MAX_DISTANCE  100 // 最大测量距离，单位是厘米
#define SERVO_PIN     9   // 舵机连接的引脚
#define RESET_BUTTON_PIN  6  // 重置按钮连接的引脚

Servo myservo;
NewPing sonar1(TRIGGER_PIN1, ECHO_PIN1, MAX_DISTANCE);
NewPing sonar2(TRIGGER_PIN2, ECHO_PIN2, MAX_DISTANCE);
int pos = 90;  // 舵机的初始位置
int defaultDistance = 50;
const int relayPin1 = 8;  // 继电器连接到Arduino的D7引脚
const int relayPin2 = 7;  // 继电器连接到Arduino的D7引脚

void setup() {
  Serial.begin(9600);
  myservo.attach(SERVO_PIN); // 将舵机连接到定义的引脚上
  pinMode(RESET_BUTTON_PIN, INPUT_PULLUP); // 设置重置按钮为输入并启用内部上拉电阻
  myservo.write(pos); // 移动舵机到初始位置
  pinMode(relayPin1, OUTPUT);  // 设置为输出模式
  pinMode(relayPin2, OUTPUT); 
}

void loop() {
  delay(500); // 给传感器稳定时间
  int distance1 = sonar1.ping_cm();
  int distance2 = sonar2.ping_cm();
  int resetButtonState = digitalRead(RESET_BUTTON_PIN);

  if (resetButtonState == LOW) { // 如果重置按钮被按下
    pos = 90; // 设置舵机回到初始位置
    myservo.write(pos);
  } else {
    if (distance1 > 0 && distance1 < defaultDistance) { // 如果第一个传感器检测到的物体距离小于100厘米
      pos -= 5; // 舵机逆时针转动5度
      if (pos < 0) pos = 0; // 防止舵机转动超过极限
      myservo.write(pos);
      Serial.println("1");
      digitalWrite(relayPin1, HIGH);  // 打开继电器（气泵打开）
      delay(1000); 
      digitalWrite(relayPin1, LOW);
    } else if (distance2 > 0 && distance2 < defaultDistance) { // 如果第二个传感器检测到的物体距离小于100厘米
      pos += 5; // 舵机顺时针转动5度
      if (pos > 180) pos = 180; // 防止舵机转动超过极限
      myservo.write(pos);
      Serial.println("2");
      digitalWrite(relayPin2, HIGH); 
      delay(100);  // 持续5秒
      digitalWrite(relayPin2, LOW);
    }else{
      digitalWrite(relayPin1, LOW);  // 关闭继电器（气泵关闭）
      digitalWrite(relayPin2, LOW);  // 关闭继电器（气泵关闭）
      Serial.println("0");
    }
  }
  
  // 一些调试信息
  //Serial.print("Distance1: ");
  //Serial.print(distance1);
  //Serial.print("cm, Distance2: ");
 // Serial.print(distance2);
  //Serial.print("cm, Servo Position: ");
  //Serial.println(pos);

  delay(100); // 稍作延时，避免舵机响应过快
}
