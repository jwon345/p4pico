#include "pico/stdlib.h"
#include <stdio.h>
#include "pico/cyw43_arch.h"
#include "hardware/gpio.h"
#include "hardware/adc.h"

const float sleepTime = 500;


int main() {

    for(int a = 0; a < 10; a++)
    {
        sleep_ms(200);
        printf("initing\n");
    }

    stdio_init_all();
    cyw43_arch_init();

    gpio_init(1);
    gpio_init(2);
    gpio_init(3);

    gpio_set_dir(1, GPIO_OUT);
    gpio_set_dir(2, GPIO_OUT);
    gpio_set_dir(3, GPIO_OUT);
    
    gpio_put(1,1);


    // adc_init();
    // // // Make sure GPIO is high-impedance, no pullups etc
    // adc_gpio_init(26);
    // // // Select ADC input 0 (GPIO26)
    // adc_select_input(0);

    while (true) {

        gpio_put(3,1);
        for (int a = 0; a < 3; a++)
        {
            cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 1);
            gpio_put(2,1);
            sleep_ms(sleepTime);
            cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 0);
            gpio_put(2,0);
            sleep_ms(sleepTime);
            gpio_put(3,0);
        }



        // const float conversion_factor = 3.3f / (1 << 12);
        // uint16_t result = adc_read();
        // printf("Raw value: 0x%03x, voltage: %f V\n", result, result * conversion_factor);
    }
}