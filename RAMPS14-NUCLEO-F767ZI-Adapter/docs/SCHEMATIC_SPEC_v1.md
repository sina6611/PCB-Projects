# Schematic Specification v1

Project: RAMPS 1.4 ↔ NUCLEO-F767ZI Adapter

This revision is additive and does not overwrite earlier files.

## 1. Mechanical / connector architecture

- Top side: female Arduino Mega / RAMPS 1.4 header pattern.
- Bottom side: male headers aligned only to NUCLEO-F767ZI Zio/Arduino connectors CN7, CN8, CN9 and CN10.
- Morpho CN11/CN12 are not used.
- RAMPS remains electrically and mechanically compatible with its original Mega pin assignment.

## 2. Stepper control channels

Five channels are implemented: X, Y, Z, E0, E1.

Each STEP, DIR and ENABLE path is:

`NUCLEO GPIO -> 47 ohm series resistor -> RAMPS signal`

Default population: direct 3.3 V drive because the installed TMC2209 modules accept 3.3 V logic.

Recommended footprints:
- 15 x 47 ohm 0603 series resistors.
- Optional unpopulated footprint per channel for a future 74AHCT buffer if a different driver module requires 5 V logic.

## 3. RAMPS MOSFET control outputs

Three RAMPS high-current switching nets are controlled by the adapter:

- RAMPS D10 = hotend heater
- RAMPS D9 = fan
- RAMPS D8 = heated bed

Use one 74AHCT125 or 74AHCT244 powered from RAMPS +5 V.

Path:

`STM32 3.3 V PWM -> AHCT input -> 5 V logic output -> 47 ohm -> RAMPS D8/D9/D10`

Requirements:
- 100 nF decoupling capacitor directly at buffer VCC.
- 4.7 uF local bulk capacitor on RAMPS +5 V logic rail.
- Buffer enables strapped to the active state.
- Never connect RAMPS +5 V directly to the NUCLEO +5 V rail in the first prototype.

## 4. Endstop inputs

Six endstop signals are supported:

X_MIN, X_MAX, Y_MIN, Y_MAX, Z_MIN, Z_MAX.

Preferred prototype circuit for each signal:

`RAMPS endstop signal -> 10 k series resistor -> STM32 GPIO`

plus:
- 10 k pull-up to 3.3 V on STM32 side, selectable by solder jumper.
- Optional 100 nF capacitor to GND on STM32 side for mechanical switch debounce/noise filtering.
- Optional BAT54S clamp footprint to 3.3 V/GND for additional protection.

The design must not rely on a 5 V pull-up from RAMPS entering the STM32 pin.

## 5. Thermistor / ADC interface

RAMPS thermistor nodes are 5 V-domain analog signals. Each channel uses:

`RAMPS TEMP -> 100 k series/top resistor -> ADC node`

ADC node to GND:
- 200 k resistor
- 100 nF capacitor

Transfer ratio approximately 0.667, so 5.0 V becomes approximately 3.33 V.

Channels:
- TEMP0 -> NUCLEO A0 / PA3
- TEMP1 -> NUCLEO A1 / PC0
- TEMP_BED -> NUCLEO A2 / PC3

Firmware must use the effective divider ratio when converting ADC readings to temperature.

## 6. Power domains

Three named domains:

- `GND_COMMON`
- `+3V3_NUCLEO`
- `+5V_RAMPS_LOGIC`

Rules:
- Grounds are common.
- NUCLEO remains USB powered during bring-up.
- RAMPS +5 V powers only the 5 V-side interface circuitry.
- No RAMPS 12/24 V power is routed through the adapter PCB.

## 7. Test points

Provide labeled test points for:

- +3V3_NUCLEO
- +5V_RAMPS_LOGIC
- GND
- X/Y/Z/E0/E1 STEP
- D8, D9, D10
- TEMP0, TEMP1, TEMP_BED ADC nodes
- all six endstops

## 8. PCB design rules

- 2-layer FR-4, 1.6 mm, 1 oz copper is sufficient.
- Solid GND plane on bottom layer where practical.
- Keep analog thermistor traces away from STEP/PWM traces.
- Place ADC RC filters close to CN9 / STM32 side.
- Place output series resistors close to the driver/buffer source.
- Use 0.25–0.30 mm signal traces minimum.
- Use wider traces for 3.3 V / 5 V logic rails.
- Clearly mark top-side RAMPS orientation and bottom-side NUCLEO orientation on silkscreen.

## 9. Prototype status

This specification is the electrical basis for the first real KiCad schematic. It is not yet a released-for-manufacture design. Mechanical connector coordinates must be verified against the official NUCLEO-F767ZI and Arduino Mega/RAMPS header drawings before Gerber release.
