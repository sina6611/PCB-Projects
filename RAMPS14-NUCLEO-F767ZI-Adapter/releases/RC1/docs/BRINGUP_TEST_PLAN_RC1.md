# Bring-up / Verification Plan RC1

1. Assemble adapter without RAMPS and without NUCLEO.
2. Check shorts between +5V, +3V3 and GND.
3. Mount adapter to NUCLEO only; power NUCLEO by USB.
4. Verify +3V3 on adapter, and confirm +5V_RAMPS remains absent.
5. Remove power; mount RAMPS and supply RAMPS logic/power as intended.
6. Verify common GND and +5V at AHCT VCC.
7. Toggle each STEP/DIR/ENABLE GPIO at low frequency and scope both sides of each AHCT channel.
8. Verify 3.3V input produces ~5V logic on RAMPS side.
9. Verify endstop input low/high transitions produce clean 0/3.3V at STM32 side.
10. Inject 0–5V into each TEMP input through a lab source and confirm ADC node never exceeds ~3.33V.
11. Test D10/D9/D8 with no heater loads first; scope RAMPS MOSFET gate/control nodes.
12. Install one TMC2209 and one motor; test X only.
13. Repeat Y/Z/E0/E1.
14. Connect endstops, thermistors, fan and heaters one subsystem at a time.
15. Only after successful first-article fit and electrical validation generate production Gerbers.
