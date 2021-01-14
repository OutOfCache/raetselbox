#include <bcm2835.h>
#include <iostream>
#include "si7021_2.h"

using namespace std;

const uint8_t ADDR = 0x40;

int main()
{
if(bcm2835_init()!=0)
{
cout << "Fehler"<<endl;
}
if(bcm2835_i2c_begin()!=0)
{
cout << "Fehler i2c"<<endl;
}

bcm2835_i2c_setSlaveAddress(ADDR);
SI7021<bcm2835_i2c_write_read_rs> si7021;

while(1)
{
cout << "-------------------------"<<endl;
cout << "Aktuelle Temp: "<< si7021.get_temperatur()<<endl;
cout << "Aktuelle Luft: "<< si7021.get_rel_humidity() <<endl;

cout << "-------------------------"<<endl;

bcm2835_delay(1000);

}



}