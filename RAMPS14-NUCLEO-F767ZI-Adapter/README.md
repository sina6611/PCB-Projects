# RAMPS 1.4 ↔ NUCLEO-F767ZI Adapter PCB

Adapter PCB project for connecting a **RAMPS 1.4** shield to an **ST NUCLEO-F767ZI**.

## Current architecture

- Controller: **NUCLEO-F767ZI (STM32F767ZI)**
- Shield: **RAMPS 1.4**
- NUCLEO connection: **Arduino/Zio pin headers CN7, CN8, CN9, CN10 only**
- **ST Morpho CN11/CN12 must not be used**
- RAMPS side keeps the Arduino Mega/RAMPS-compatible header pattern
- Target stack: `RAMPS 1.4 → Adapter PCB → NUCLEO-F767ZI`

## Design scope

The adapter will route and condition:

- X/Y/Z/E0/E1 STEP, DIR, ENABLE
- X/Y/Z endstops
- D8 / D9 / D10 power-control logic
- TEMP0 / TEMP1 / TEMP_BED analog inputs
- Ground and required logic rails
- Optional TMC2209-related signals after pin-budget verification

## Electrical constraints

- STM32F767ZI GPIO logic is 3.3 V.
- RAMPS 1.4 was originally designed around 5 V Arduino Mega logic.
- Voltage compatibility must be verified net-by-net before final routing.
- Thermistor inputs require protection/scaling before STM32 ADC inputs.
- D8/D9/D10 gate-control paths require verified drive-level handling.

## Project status

**Design reset / requirements locked.**

Earlier experimental RevA/RevB concepts used the Morpho connector and are **not valid for fabrication**. The new design starts from the CN7/CN8/CN9/CN10 Zio headers and will be reviewed before Gerber release.

## Next milestones

1. Extract exact CN7/CN8/CN9/CN10 pin table from the NUCLEO-F767ZI documentation.
2. Build the RAMPS signal-to-Zio pin allocation.
3. Verify timer/PWM/ADC requirements and conflicts.
4. Create the production schematic in KiCad.
5. Create mechanical footprints and 3-board stack-up.
6. Route PCB and run ERC/DRC.
7. Generate Gerber, drill, BOM and assembly documentation.
