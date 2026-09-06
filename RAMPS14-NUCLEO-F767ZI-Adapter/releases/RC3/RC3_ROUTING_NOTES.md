# RC3 Routed Placement

Changes vs RC2:

- Board outline remains exactly 70.00 mm × 133.34 mm.
- The complete Arduino Mega/RAMPS mating header pad pattern is represented using coordinates from the RAMPS Eagle `ARDUINO_MEGA_SHIELD` footprint.
- The RAMPS header pattern is rotated 90° so all mating header pads fit inside the 70 mm NUCLEO width.
- NUCLEO CN7/CN8/CN9/CN10 stay at their NUCLEO-relative coordinates.
- U1-U3 (74AHCT244) and U4 (74LVC541A) are placed in a dedicated interface zone.
- Signal nets are split into 3.3-V and 5-V domains across the buffers.
- Copper tracks have been added on F.Cu and B.Cu so the board no longer consists only of ratsnest lines.
- Thermistor paths are routed through a 100k upper divider resistor to the ADC domain.

Important: this is an engineering routed RC, not yet a manufacturing release. A full KiCad DRC and physical first-fit with the exact RAMPS 1.4 clone are still required before ordering.
