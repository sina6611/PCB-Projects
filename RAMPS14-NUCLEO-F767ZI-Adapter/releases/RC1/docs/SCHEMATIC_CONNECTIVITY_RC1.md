# RC1 Schematic Connectivity

## Output buffers (5 V)
Use U1-U3 = 74AHCT244, VCC=+5V_RAMPS, GND=GND.
All /OE pins tied low through 10k (optionally direct after prototype validation).
Each output then passes through 47R before the RAMPS header.

Assigned outputs:
U1: X_STEP, X_DIR, X_EN, Y_STEP, Y_DIR, Y_EN, Z_STEP, Z_DIR
U2: Z_EN, E0_STEP, E0_DIR, E0_EN, E1_STEP, E1_DIR, E1_EN, HOTEND
U3: FAN, BED; remaining channels reserved.

## Endstop buffer
U4 = 74LVC541A, VCC=+3V3, GND=GND.
Inputs receive RAMPS X_MIN/X_MAX/Y_MIN/Y_MAX/Z_MIN/Z_MAX.
Because LVC inputs are 5-V tolerant at 3.3-V VCC (verify chosen manufacturer part), outputs are safe 3.3-V signals to STM32.
Unused inputs must not float.

## Thermistors
For each TEMPx:
RAMPS_TEMP --100k--> ADC_NODE
ADC_NODE --200k--> GND
ADC_NODE --100nF--> GND
ADC_NODE --> NUCLEO A0/A1/A2 respectively.

## Power
GND common between RAMPS and NUCLEO.
+5V_RAMPS powers AHCT only.
+3V3_NUCLEO powers LVC input buffer only.
Do not bridge +5V_RAMPS to NUCLEO +5V in RC1.
NUCLEO powered by USB during bring-up.

## Manufacturing hold
Do not order RC1 until physical fit of the top RAMPS header pattern and stack height is confirmed on the actual RAMPS 1.4 clone.
