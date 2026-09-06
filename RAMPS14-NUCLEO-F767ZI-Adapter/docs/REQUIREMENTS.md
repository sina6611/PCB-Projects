# Requirements

## Hardware

- ST NUCLEO-F767ZI
- RAMPS 1.4 shield
- TMC2209 stepper-driver modules on RAMPS where applicable

## Mechanical requirement

The adapter PCB shall be mounted directly between the two boards:

`RAMPS 1.4 (top) -> Adapter PCB (middle) -> NUCLEO-F767ZI (bottom)`

The NUCLEO interface shall use only the Arduino/Zio header set **CN7, CN8, CN9 and CN10**. The Morpho headers CN11/CN12 are explicitly excluded.

## Functional signals

### Stepper axes
- X STEP / DIR / ENABLE
- Y STEP / DIR / ENABLE
- Z STEP / DIR / ENABLE
- E0 STEP / DIR / ENABLE
- E1 STEP / DIR / ENABLE

### Endstops
- X_MIN / X_MAX
- Y_MIN / Y_MAX
- Z_MIN / Z_MAX

### Power-control logic
- RAMPS D8
- RAMPS D9
- RAMPS D10

### Analog inputs
- TEMP0 = RAMPS A13
- TEMP1 = RAMPS A15
- TEMP_BED = RAMPS A14

## Electrical constraints

- STM32 side logic voltage: 3.3 V.
- RAMPS compatibility must be checked net-by-net against the actual attached circuits.
- Any signal able to exceed the STM32 absolute maximum must be conditioned before reaching the NUCLEO.
- Thermistor inputs shall be scaled/protected for the STM32 ADC range.
- Ground must be common between the adapter, NUCLEO and RAMPS logic.
- High-current bed/heater/motor current shall not be routed through the adapter PCB.

## Release policy

No Gerbers may be marked production-ready until:

- the complete Zio pin map is verified,
- schematic ERC is clean,
- PCB DRC is clean,
- connector geometry is verified against actual NUCLEO-F767ZI and RAMPS 1.4 hardware,
- power and voltage-domain review is complete.
