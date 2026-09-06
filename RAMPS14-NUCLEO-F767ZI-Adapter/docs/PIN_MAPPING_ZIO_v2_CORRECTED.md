# Pin Mapping Zio v2 — corrected

This is a new additive revision. Earlier mapping files are preserved for history and must not be used for fabrication.

## Reference basis
- NUCLEO-F767ZI: ST UM1974, Table 19.
- RAMPS 1.4: standard Mega/RAMPS assignments.
- No Morpho connectors are used.

## Stepper control
| Function | RAMPS/Mega pin | NUCLEO label | STM32 | Connector pin |
|---|---:|---:|---|---|
| X_STEP | 54/A0 | D32 | PA0 | CN10-29 |
| X_DIR | 55/A1 | D28 | PD13 | CN10-19 |
| X_ENABLE | 38 | D29 | PD12 | CN10-21 |
| Y_STEP | 60/A6 | D33 | PB0 | CN10-31 |
| Y_DIR | 61/A7 | D30 | PD11 | CN10-23 |
| Y_ENABLE | 56/A2 | D31 | PE2 | CN10-25 |
| Z_STEP | 46 | D36 | PB10 | CN10-32 |
| Z_DIR | 48 | D34 | PE0 | CN10-33 |
| Z_ENABLE | 62/A8 | D37 | PE15 | CN10-30 |
| E0_STEP | 26 | D35 | PB11 | CN10-34 |
| E0_DIR | 28 | D38 | PE14 | CN10-28 |
| E0_ENABLE | 24 | D39 | PE12 | CN10-26 |
| E1_STEP | 36 | D40 | PE10 | CN10-24 |
| E1_DIR | 34 | D41 | PE7 | CN10-20 |
| E1_ENABLE | 30 | D42 | PE8 | CN10-18 |

## Endstops
| Function | RAMPS pin | NUCLEO label | STM32 | Connector pin |
|---|---:|---:|---|---|
| X_MIN | D3 | D43 | PC8 | CN8-2 |
| X_MAX | D2 | D44 | PC9 | CN8-4 |
| Y_MIN | D14 | D45 | PC10 | CN8-6 |
| Y_MAX | D15 | D46 | PC11 | CN8-8 |
| Z_MIN | D18 | D47 | PC12 | CN8-10 |
| Z_MAX | D19 | D48 | PD2 | CN8-12 |

## Temperature ADC
| Function | RAMPS analog pin | NUCLEO label | STM32 | Connector pin |
|---|---:|---:|---|---|
| TEMP0 | A13 | A0 | PA3 / ADC123_IN3 | CN9-1 |
| TEMP1 | A15 | A1 | PC0 / ADC123_IN10 | CN9-3 |
| TEMP_BED | A14 | A2 | PC3 / ADC123_IN13 | CN9-5 |

## RAMPS MOSFET controls
| Function | RAMPS net | NUCLEO label | STM32 | Connector pin |
|---|---:|---:|---|---|
| Hotend | D10 | D10 | PD14 / TIM4_CH3 | CN7-16 |
| Fan | D9 | D9 | PD15 / TIM4_CH4 | CN7-18 |
| Bed | D8 | D6 | PE9 / TIM1_CH1 | CN10-4 |

## Important electrical correction
TMC2209 digital input-high threshold is specified as 0.7 × VIO. On a RAMPS-style module where VIO is 5 V, 3.3 V from the STM32 is not guaranteed to meet VIH. Therefore STEP, DIR and ENABLE shall be translated to 5 V using AHCT-family buffers powered from RAMPS +5 V. Direct 3.3 V drive is not the production design.

## Production rule
- U1/U2/U3: 74AHCT244, VCC = +5V_RAMPS_LOGIC, for 15 STEP/DIR/ENABLE signals plus D8/D9/D10.
- U4: 74LVC541A, VCC = +3V3_NUCLEO, for 6 endstop inputs; inputs are 5 V tolerant.
- Thermistor channels are attenuated to the STM32 ADC range.
- Common ground only between the two boards; do not bridge the two 5 V rails.
