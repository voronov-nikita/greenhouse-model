#include <Servo.h>
#include <stDHT.h>

#define dw digitalWrite
#define ar analogRead

int list_pin_read[6] = {A0, A1, A2, A3, A4, A5};

DHT sensor(DHT11);
Servo servo;

void setup() {
  Serial.begin(9600);

  // подключение пина для сервопривода + поворот до 0 градусов
  // пусть 0 градусов - это начальное положение сервопривода
  servo.attach(6);
  servo.write(0);
  
  // определение пинов для почвы
  for (int i=7; i<=12; i++) pinMode(i, OUTPUT);   
  
  // определение пинов для воздуха
  for (int i=2; i<2+4; i++){
    pinMode(i, INPUT);
  }    
}

void loop() {
  
  String command = (String) Serial.parseInt();
  // здесь мы распределяем что есть команда, а что пин для опроса
  String first = command.substring(0, 1);
  int second = command.substring(1).toInt();
  switch(first.toInt()){
    case 1: data_soil_sensors(second); break;
    case 2: data_dh_sensors(second); break;
    case 3: open_close(); break;
    
  }                   
}

// формирование ответа на запрос определенного пина у датчика почвы.
// пин чтения категорически должен быть на 7 меньше в индексной форме у массива list_pin_read
// пины нумеруются от 7 до 12 включительно!
void data_soil_sensors(int pin){
  dw(pin, 1);
  delay(10);
    
  float sensor_value = ar(list_pin_read[pin-7-1]);
  dw(pin, 0);
  Serial.println(map(sensor_value, 0, 1023, 0, 100));
}

//  формирование ответа на запрос определенного пина у датчика DH11.
// пины нумеруются от 2 до 5 включительно!
void data_dh_sensors(int pin){
  dw(pin, 1);
  float temperature = sensor.readTemperature(pin);
  float humidity = sensor.readHumidity(pin);
  // вывод
  Serial.print(temperature);
  Serial.print(" ");
  Serial.println(humidity);
  dw(pin, 0);
}

// изменение положения сервопривода относительно текущего положения
void open_close(){
  int angle = servo.read();
  if (angle==90) servo.write(0);
  if (angle==0) servo.write(90);
}
