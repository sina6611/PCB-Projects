# RAMPS 1.4 ↔ NUCLEO-F767ZI Adapter RC3

Routed engineering candidate.

- Board outline: 70.00 mm × 133.34 mm (NUCLEO-F767ZI size)
- NUCLEO side: CN7/CN8/CN9/CN10 only
- No Morpho
- Full Arduino Mega/RAMPS mating header pad pattern represented from RAMPS Eagle footprint coordinates
- RAMPS header pattern rotated 90° so it fits inside the NUCLEO-width adapter
- U1-U3: 74AHCT244 output level shifting
- U4: 74LVC541A endstop input buffering
- Thermistor ADC divider paths included
- Copper tracks added on F.Cu and B.Cu

This revision does not overwrite RC1/RC2.

Status: engineering routed RC. Do not manufacture until KiCad DRC and physical fit with the exact RAMPS 1.4 clone are completed.
