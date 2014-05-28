char inData[7]; 
char inChar;
byte index = 0;
String RollPitchData;
int commaPosition = 0; 

void setup()
{
Serial.begin(9600);
Serial2.begin(9600);
}

void loop()
{
  if(Comp("100,200")==0){
    Serial.println("Correct Data");
  }
  else{
    Serial.println("Incorrect Data");
  }

}  
/*
void loop()
{
  
if(Serial2.available()) 
  {
    for(index=0;index<=7;index++) // One less than the size of the array
    {
      inChar = Serial2.read(); // Read a character
      Serial.println(inChar);    
      inData[index] = inChar; // Store it
      index++;
      //inData[index] = '\n'; // Null terminate the string
     }
  }
}
delay(10);
Serial.print(inData);
//index=0;

  
RollPitchData = inData;//"100,300";
 
commaPosition = RollPitchData.indexOf(',');
if(commaPosition != -1)
  {
    String pitchstr = RollPitchData.substring(0,commaPosition);
    int pitch = pitchstr.toInt();
    //Serial.println(pitch);
    String rollstr = RollPitchData.substring(commaPosition+1, RollPitchData.length());
    RollPitchData = RollPitchData.substring(commaPosition+1, RollPitchData.length());
    //int roll = RollPitchData.toInt();
    //Serial.println(roll);
    //Serial.println(RollPitchData);
  }
commaPosition =0;
}
*/

char Comp(char* This){

 if(Serial2.available())
  {
    if(index < 7) // One less than the size of the array
    {
      inChar = Serial2.read(); 
      inData[index] = inChar;
      index++; 
      //inData[index] = '\0'; // Null terminate the string
    }
  }
  delay(50);
  Serial.println(inData);
  if(strcmp(inData,This)  == 0){
    for(int i=0;i<19;i++){
      inData[i]=0;
    }
    index=0;
    return(0);

  }
  else{
    return(1);
 }
}
