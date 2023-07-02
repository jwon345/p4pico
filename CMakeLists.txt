cmake_minimum_required(VERSION 3.13)
include(pico_sdk_import.cmake)

set(PICO_BOARD pico_w)
    
project(PicoFirmware)

# initialize the Raspberry Pi Pico SDK
pico_sdk_init()

add_executable(PicoFirmware
        Firmware.c
        )

target_link_libraries(PicoFirmware
        pico_stdlib              # for core functionality
        pico_cyw43_arch_none     # we need Wifi to access the GPIO, but we don't need anything else
        hardware_adc
        hardware_gpio
        )

# create map/bin/hex file etc.
pico_add_extra_outputs(my_PicoFirmware)
