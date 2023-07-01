# Raspberry pi pico for part 4 project

## Requirements 
- WSL
- Raspberry pi pico SDK

## Pins and their functionalities
- pin 1 = enable for the LED driver -> always high
- pin 2 = Clock?
- pin 3 = Single pulse at the start of the cycle to push the single led

## How to build
1. Edit the CMakeLists.txt file point to path of Pico sdk
2. Make a directory named "build"
3. from the build run
```
cmake ..
```
4. the run the following to compile
```
make
```
5. A .elf file should be generated after compiling
6. plugin the pico into the PC while holding the boot button and a USB type device should be connected
7. drag and drop the .elf file into the pico
