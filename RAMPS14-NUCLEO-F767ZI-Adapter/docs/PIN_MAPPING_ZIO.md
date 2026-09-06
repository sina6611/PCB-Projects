# Pin Mapping — RAMPS 1.4 to NUCLEO-F767ZI via Zio headers only

This revision intentionally does **not** use the Morpho connectors. The adapter mates only with the NUCLEO-F767ZI Zio/Arduino headers CN7, CN8, CN9 and CN10.

## Core stepper signals

| RAMPS function | RAMPS / Mega pin | NUCLEO Zio pin | STM32 pin | NUCLEO connector |
|---|---:|---:|---|---|
| X_STEP | 54 / A0 | D32 | PA0 | CN10 pin 29 |
| X_DIR | 55 / A1 | D28 | PD13 | CN10 pin 19 |
| X_ENABLE | 38 | D29 | PD12 | CN10 pin 21 |
| Y_STEP | 60 / A6 | D33 | PB0 | CN10 pin 31 |
| Y_DIR | 61 / A7 | D30 | PD11 | CN10 pin 23 |
| Y_ENABLE | 56 / A2 | D31 | PE2 | CN10 pin 25 |
| Z_STEP | 46 | D36 | PB10 | CN10 pin 32 |
| Z_DIR | 48 | D34 | PE0 | CN10 pin 33 |
| Z_ENABLE | 62 / A8 | D37 | PE15 | CN10 pin 30 |
| E0_STEP | 26 | D35 | PB11 | CN10 pin 34 |
| E0_DIR | 28 | D38 | PE14 | CN10 pin 28 |
| E0_ENABLE | 24 | D39 | PE12 | CN10 pin 26 |
| E1_STEP | 36 | D40 | PE10 | CN10 pin 24 |
| E1_DIR | 34 | D41 | PE7 | CN10 pin 20 |
| E1_ENABLE | 30 | D42 | PE8 | CN10 pin 18 |

## Endstops

| RAMPS function | RAMPS / Mega pin | NUCLEO Zio pin | STM32 pin | NUCLEO connector |
|---|---:|---:|---|---|
| X_MIN | D3 | D43 | PC8 | CN8 pin 2 |
| X_MAX | D2 | D44 | PC9 | CN8 pin 4 |
| Y_MIN | D14 | D45 | PC10 | CN8 pin 6 |
| Y_MAX | D15 | D46 | PC11 | CN8 pin 8 |
| Z_MIN | D18 | D47 | PC12 | CN8 pin 10 |
| Z_MAX | D19 | D48 | PD2 | CN8 pin 12 |

## Temperature inputs

RAMPS 1.4 uses analog inputs A13, A15 and A14 for TEMP0, TEMP1 and bed temperature respectively. These analog nodes are remapped to three ADC-capable NUCLEO pins.

| RAMPS function | RAMPS analog pin | NUCLEO Zio pin | STM32 ADC pin | NUCLEO connector |
|---|---:|---:|---|---|
| TEMP0 | A13 | A0 | PA3 / ADC123_IN3 | CN9 pin 1 |
| TEMP1 | A15 | A1 | PC0 / ADC123_IN10 | CN9 pin 3 |
| TEMP_BED | A14 | A2 | PC3 / ADC123_IN13 | CN9 pin 5 |

These signals require attenuation/protection before the STM32 ADC because stock RAMPS thermistor circuits are referenced to 5 V.

## Power outputs

| RAMPS function | RAMPS pin | NUCLEO Zio pin | STM32 pin | NUCLEO connector | Note |
|---|---:|---:|---|---|---|
| Hotend / MOSFET A | D10 | D10 | PD14 / TIM4_CH3 | CN7 pin 16 | Hardware PWM |
| Fan / MOSFET B | D9 | D9 | PD15 / TIM4_CH4 | CN7 pin 18 | Hardware PWM |
| Heated bed / MOSFET C | D8 | D6 | PE9 / TIM1_CH1 | CN10 pin 4 | Remapped for hardware PWM |

The adapter therefore connects NUCLEO D6 to the RAMPS D8 net; the labels do not need to match physically because the adapter performs the remapping.

## Design rule

- No CN11/CN12 Morpho use.
- NUCLEO mating is only CN7/CN8/CN9/CN10.
- RAMPS 1.4 retains its standard Mega-format pin assignment.
- Firmware must use the STM32/Zio mapping in this document, not the original Mega pin numbers.
