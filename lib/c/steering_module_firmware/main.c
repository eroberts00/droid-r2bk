/**
 * Copyright (c) 2023, Elijah Roberts
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include <stdio.h>
#include "pico/stdlib.h"


#ifndef PICO_DEFAULT_LED_PIN
#error "Onboard LED is a required feature."
#endif

int main() {

    // Setup the onboard LED pin.
    const uint LED_PIN = PICO_DEFAULT_LED_PIN;
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    // Initialize stdio.
    stdio_init_all();


    // Loop.
    uint count = 0;
    while (true) {
        gpio_put(LED_PIN, 1);
        sleep_ms(500);
        gpio_put(LED_PIN, 0);
        sleep_ms(500);
        printf("Cycle: %d\n", count);
        count++;
    }
    return 0;
}