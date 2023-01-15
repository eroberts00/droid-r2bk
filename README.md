# droid-r2bk
Firmware, software, and hardware designs for R2BK droid toy

## Connect to Raspberry PI Pico via USB Serial from WSL2

1. Install the `usbipd-win` USB/IP service: https://github.com/dorssel/usbipd-win

1. Connect the Pico device to a USB port.

1. Bind the Pico to the USB/IP subsystem from Windows. (This step only needs to be done the first time a device is used.)
    ```
    C:> usbipd list
    Connected:
    BUSID  VID:PID    DEVICE                                                        STATE
    1-5    258a:1007  USB Input Device                                              Not shared
    1-6    046d:c31c  USB Input Device                                              Not shared
    1-7    2e8a:000a  USB Serial Device (COM4), Reset                               Not shared
    2-1    046d:09a4  USB Video Device, USB Audio Device                            Not shared
    ```
    ```
    C:> usbipd bind -b 1-7
    ```

    ```
    C:> usbipd list
    Connected:
    BUSID  VID:PID    DEVICE                                                        STATE
    1-5    258a:1007  USB Input Device                                              Not shared
    1-6    046d:c31c  USB Input Device                                              Not shared
    1-7    2e8a:000a  USB Serial Device (COM4), Reset                               Shared
    2-1    046d:09a4  USB Video Device, USB Audio Device                            Not shared
    ```

1. Attach the USB/IP device to the WSL2 subsystem.

    ```
    C:> usbipd wsl attach -b 1-7
    ```

    ```
    C:> usbipd wsl list
    BUSID  VID:PID    DEVICE                                                        STATE
    1-5    258a:1007  USB Input Device                                              Not attached
    1-6    046d:c31c  USB Input Device                                              Not attached
    1-7    2e8a:000a  USB Serial Device (COM4), Reset                               Attached - Ubuntu
    2-1    046d:09a4  USB Video Device, USB Audio Device                            Not attached
    ```

1. Find the Linux USB device and connect via a serial console.

    ```
    ubuntu:droid-r2bk$ sudo lsusb
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 002: ID 2e8a:000a Raspberry Pi Pico
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    ```

    ```
    ubuntu:droid-r2bk$ sudo dmesg
    [  723.495146] vhci_hcd vhci_hcd.0: pdev(0) rhport(0) sockfd(3)
    [  723.496228] vhci_hcd vhci_hcd.0: devid(65543) speed(2) speed_str(full-speed)
    [  723.497392] vhci_hcd vhci_hcd.0: Device attached
    [  723.769557] vhci_hcd: vhci_device speed not set
    [  723.839551] usb 1-1: new full-speed USB device number 2 using vhci_hcd
    [  723.929546] vhci_hcd: vhci_device speed not set
    [  723.999559] usb 1-1: SetAddress Request (2) to port 0
    [  724.138538] usb 1-1: New USB device found, idVendor=2e8a, idProduct=000a, bcdDevice= 1.00
    [  724.139743] usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [  724.140605] usb 1-1: Product: Pico
    [  724.141128] usb 1-1: Manufacturer: Raspberry Pi
    [  724.141829] usb 1-1: SerialNumber: E660D051132EB428
    [  724.155388] cdc_acm 1-1:1.0: ttyACM0: USB ACM device
    ```

    ```
    ubuntu:droid-r2bk$ sudo minicom -D /dev/ttyACM0
    ```