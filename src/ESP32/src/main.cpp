#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <NTPClient.h>
#include <WiFiUdp.h>
#include <DHT.h>

#define X_AXLE_VIBRATION_SENSOR 35
#define Y_AXLE_VIBRATION_SENSOR 32
#define Z_AXLE_VIBRATION_SENSOR 33

#define RAIN_GAUGE_SENSOR 12

#define WIND_SENSOR 34

#define DHTPIN 4 
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "Wokwi-GUEST";
const char* password = "";

const char* spreadsheet = "https://script.google.com/macros/s/AKfycbzuqYS4u2zJx5Zs1hSL66OYEG9CPDTYsocCGs4X14D45rsrn9bMVLTLcj4TfVRr6lWi/exec";

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org", 7200, 60000);

const int upgrade_delay = 1000;

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  Serial.println("Conectado ao WiFi com Sucesso!");
  
  dht.begin();

  timeClient.begin();
  timeClient.update();

  pinMode(X_AXLE_VIBRATION_SENSOR, INPUT);
  pinMode(Y_AXLE_VIBRATION_SENSOR, INPUT);
  pinMode(Z_AXLE_VIBRATION_SENSOR, INPUT);
  pinMode(RAIN_GAUGE_SENSOR, INPUT_PULLUP);
  pinMode(WIND_SENSOR, INPUT);

}

void loop() {

 if (WiFi.status() == WL_CONNECTED) { 
    HTTPClient http;
    http.begin(spreadsheet);
    http.addHeader("Content-Type", "application/json");
  
  timeClient.update();
  String formattedTime = timeClient.getFormattedTime();

  bool valueRainGauge = digitalRead(RAIN_GAUGE_SENSOR) == LOW ? true : false;

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  
  int valueXAxle = analogRead(X_AXLE_VIBRATION_SENSOR);
  int valueYAxle = analogRead(Y_AXLE_VIBRATION_SENSOR);
  int valueZAxle = analogRead(Z_AXLE_VIBRATION_SENSOR);

  double valueWind = analogRead(WIND_SENSOR);
  double convertsLightWind = map(valueWind, 0, 4095, 0, 100); 

  String jsonData = "{";
  jsonData += "\"method\":\"append\",";
  jsonData += "\"temperature\":" + String(temperature) + ",";
  jsonData += "\"humidity\":" + String(humidity) + ",";
  jsonData += "\"timestamp\":\"" + formattedTime + "\",";
  jsonData += "\"pulviometric\":" + String(valueRainGauge ? "true" : "false") + ",";
  jsonData += "\"wind\":" + String(valueWind) + ",";
  jsonData += "\"xaxlevibration\":" + String(valueXAxle) + ",";
  jsonData += "\"yaxlevibration\":" + String(valueYAxle) + ",";
  jsonData += "\"zaxlevibration\":" + String(valueZAxle);
  jsonData += "}";
      
  int httpResponseCode = http.POST(jsonData);

  if (httpResponseCode > 0) {
    String response = http.getString();
    Serial.println(httpResponseCode);
    Serial.println(response);
  } else {
    Serial.println("Erro ao enviar as informações: " + String(httpResponseCode));
  }

    http.end();
  } else {
    Serial.println("WiFi Desconectado!");
  }

delay(upgrade_delay);

}