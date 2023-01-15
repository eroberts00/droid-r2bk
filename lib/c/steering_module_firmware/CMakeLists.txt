cmake_minimum_required(VERSION 3.12)

include($ENV{PICO_SDK_PATH}/pico_sdk_init.cmake)

pico_sdk_init()
project(steering_module_firmware)

add_executable(main main.c)

# pull in common dependencies
target_link_libraries(main pico_stdlib)

# create map/bin/hex/uf2 file etc.
pico_add_extra_outputs(main)
