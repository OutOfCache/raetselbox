#ifndef SRC2_APDS9960_H
#define SRC2_APDS9960_H

#include <cstdint>
#include "apds9960_enums.h"

template <uint8_t (*i2c_write)(const char* buf, uint32_t len), uint8_t (*i2c_read)(char* buf, uint32_t len)>
class APDS9960 {
public:
APDS9960() : enable_register(0x00), i2c_write_buffer{0}, i2c_read_buffer{0} {}

uint8_t init() {
uint8_t state =0;
state = this->set_register(APDS9960_REGISTER::ENABLE,0x00);
if(state==0){
this->enable_register=0x00;
}
return state;
}

uint8_t power_on() {
return this->set_register(APDS9960_REGISTER::ENABLE,this->enable_register | APDS9960_CONTROLS::ENABLE_POWER_ON);
}

uint8_t proximity_on_without_interrupt() {
    return this->set_register(APDS9960_REGISTER::ENABLE,this->enable_register | APDS9960_CONTROLS::ENABLE_POWER_ON |APDS9960_CONTROLS::ENABLE_PROX);
}

uint8_t get_register_value(uint8_t addr) {
i2c_read_buffer[0] = addr;
i2c_write(this->i2c_read_buffer,1);
i2c_read(this->i2c_read_buffer,1);
return this->i2c_read_buffer[0];
}


private:
uint8_t enable_register;
char i2c_write_buffer[2];
char i2c_read_buffer[32];


uint8_t set_register(uint8_t addr, uint8_t value) {
uint8_t state =0;
i2c_write_buffer[0]=addr;
i2c_write_buffer[1] = value;
state = i2c_write(this->i2c_write_buffer,2);
return state;
}
};
#endif
