# Pin Mapping v3 — ST-verified Zio-only mapping

This is a NEW revision. Earlier mapping files are retained unchanged for history.

Source basis: ST UM1974 table for NUCLEO-F767ZI CN7/CN8/CN9/CN10. No Morpho connectors are used.

## Stepper outputs

| RAMPS function | RAMPS Mega pin | NUCLEO Zio name | STM32 pin | Physical Zio connector |
|---|---:|---:|---|---|
| X_STEP | 54 / A0 | D32 | PA0 | CN7-25 |
| X_DIR | 55 / A1 | D28 | PD13 | CN7-20 |
| X_ENABLE | 38 | D29 | PD12 | CN7-21 |
| Y_STEP | 60 / A6 | D33 | PB0 | CN7-26 |
| Y_DIR | 61 / A7 | D30 | PD11 | CN7-22 |
| Y_ENABLE | 56 / A2 | D31 | PE2 | CN7-23 |
| Z_STEP | 46 | D36 | PB10 | CN7-29 |
| Z_DIR | 48 | D34 | PE0 | CN7-27 |
| Z_ENABLE | 62 / A8 | D37 | PE15 | CN7-30 |
| E0_STEP | 26 | D35 | PB7 | CN7-28 |
| E0_DIR | 28 | D38 | PE14 | CN7-32 |
| E0_ENABLE | 24 | D39 | PE12 | CN7-33 |
| E1_STEP | 36 | D40 | PE10 | CN7-34 |
| E1_DIR | 34 | D41 | PE8 | CN7-35 |
| E1_ENABLE | 30 | D42 | PE7 | CN10-10 |

## Endstops

| RAMPS function | RAMPS Mega pin | NUCLEO Zio | STM32 pin | Physical connector |
|---|---:|---:|---|---|
| X_MIN | D3 | D43 | PC8 | CN8-2 |
| X_MAX | D2 | D44 | PC9 | CN8-4 |
| Y_MIN | D14 | D45 | PC10 | CN8-6 |
| Y_MAX | D15 | D46 | PC11 | CN8-8 |
| Z_MIN | D18 | D47 | PC12 | CN8-10 |
| Z_MAX | D19 | D48 | PD2 | CN8-12 |

## Thermistors / ADC

| RAMPS function | RAMPS analog | NUCLEO Zio | STM32 ADC | Physical connector |
|---|---:|---:|---|---|
| TEMP0 | A13 | A0 | PA3 / ADC123_IN3 | CN9-1 |
| TEMP1 | A15 | A1 | PC0 / ADC123_IN10 | CN9-3 |
| TEMP_BED | A14 | A2 | PC3 / ADC123_IN13 | CN9-5 |

## RAMPS power-control signals

| RAMPS function | RAMPS pin | NUCLEO Zio | STM32 pin | Physical connector | Drive method |
|---|---:|---:|---|---|---|
| HOTEND | D10 | D10 | PD14 / TIM4_CH3 | CN7-37 | 74AHCT buffer, hardware PWM capable |
| FAN | D9 | D9 | PD15 / TIM4_CH4 | CN7-38 | 74AHCT buffer, hardware PWM capable |
| HEATED_BED | D8 | D8 | PF12 | CN7-39 | 74AHCT buffer; software PWM / bang-bang |

## Important corrections versus older drafts

- D35 on this NUCLEO-F767ZI Zio header is PB7, not PB11.
- D41 is PE8; D42 is PE7.
- D8 is PF12 on CN7-39; D6 is PF14 on CN7-41. Older draft assignments that mapped D8 to PE9 were incorrect.
- CN7/CN8/CN9/CN10 physical pin numbers in this file follow the official ST connector table.

## Electrical policy

- All MCU->RAMPS digital outputs (STEP/DIR/ENABLE and D8/D9/D10) pass through 5 V-powered AHCT buffers for guaranteed 5 V-domain logic levels on RAMPS/TMC2209.
- Endstop returns are protected/translated so no 5 V pull-up can reach STM32 directly.
- Thermistor nodes are attenuated to <=3.3 V before STM32 ADC.
- Grounds are common.
- No Morpho connector is used.
