#ifndef SI7021_2_H

#include <cstdint>

template <uint8_t (*write_read_rs)(char*cmd, uint32_t cmd_len, char*buf, uint32_t buf_len)>

class SI7021{
public:
float get_temperatur() {
char cmd = 0xE3;
char result[2] = {0};
uint16_t raw_temp=0;
write_read_rs(&cmd,1,result,2);
raw_temp |=result[0] <<8;
raw_temp |= result[1];
return ((175.72f*raw_temp)/65536.0f)-46.85f;
}

float get_rel_humidity() {
char cmd = 0xE5;
char result[2] = {0};
uint16_t raw_rel_hum=0;
write_read_rs(&cmd,1,result,2);
raw_rel_hum |=result[0] <<8;
raw_rel_hum |= result[1];
return ((125.0f*raw_rel_hum)/65536.0f)-6.0f;
}


};

#define SI7021_2_H
#endif