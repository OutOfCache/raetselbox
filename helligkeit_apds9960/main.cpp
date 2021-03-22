#include <bcm2835.h>
#include <iostream>
#include "apds9960.h"


const uint8_t ADDR = 0x39;

int main() {
APDS9960<bcm2835_i2c_write, bcm2835_i2c_read> apds9960;
if(!bcm2835_init()) {
std::cout <<"BCM INIT ERROR" <<std::endl;
}
bcm2835_i2c_begin();
bcm2835_i2c_setSlaveAddress(ADDR);
apds9960.init();
bcm2835_delay(1000);

apds9960.power_on();
apds9960.proximity_on_without_interrupt();
bcm2835_delay(10);

while(1) {
    apds9960.power_on();
apds9960.proximity_on_without_interrupt();
bcm2835_delay(10);
    std::cout<<std::to_string(apds9960.get_register_value(APDS9960_REGISTER::PROX_DATA))<< std::endl;
    bcm2835_delay(500);
}
}

//compile befehl: 
//g++ main.cpp -o ./build/main -lbcm2835
//ausfuehren: sudo ./build/main 
