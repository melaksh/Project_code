
String  RollPitchData = "100,200"; 
String  message = RollPitchData; 
int     commaPosition; 

void setup()
{
  Serial.begin(9600);
  
commaPosition = message.indexOf(',');
if(commaPosition != -1)
{
  String c = message.substring(0,commaPosition);
  int pitch = c.toInt();
  Serial.println(pitch);
  message = message.substring(commaPosition+1, message.length());
  int roll = message.toInt();
  Serial.println(roll);
}
   
   while(commaPosition >=0);
}

void loop()
{
  
}
