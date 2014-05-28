String str;
String data;
char d;
void setup()
{
  Serial2.begin(115200);
  Serial.begin(115200); 
}
void loop(){
    if(Serial2.available()) {
      //delay(20);
      int h= Serial2.available();
      char d = Serial2.read();
        if (d == '\n') {
            str=str.substring(1);  
            char t[str.length()+1];
            str.toCharArray(t, (sizeof(t)));
            Serial.println(str);
            int intdata = atoi(t);
            //Serial.println(intdata);
            str = String();
           }
        else {
            str.concat(d);
            //Serial.println(str);
        }
    }
}
