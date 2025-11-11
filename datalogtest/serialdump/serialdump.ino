void setup(){
    Serial.begin(115200);

    int i = 0;
    int j = -66;
    int k = 66;

    while(true){

        i += 1;
        j += 1;
        k += 1;

        if (i > 100){
            i = -100;
        }
        if (j > 100){
            j = -100;
        }
        if (k > 100){
            k = -100;
        }
        
        Serial.println(String(i) + " " + String(j) + " " + String(k)); //6 bytes
        
        delay(10);
    }
}

void loop(){
    
}