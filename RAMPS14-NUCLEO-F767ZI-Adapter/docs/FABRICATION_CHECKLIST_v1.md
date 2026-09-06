# Fabrication Checklist v1

## Electrical review
- [ ] Confirm all 15 STEP/DIR/ENABLE signals pass through 74AHCT244 stages.
- [ ] Confirm D8/D9/D10 also pass through 74AHCT244 stages.
- [ ] Confirm U1/U2/U3 VCC = RAMPS +5 V only.
- [ ] Confirm U4 VCC = NUCLEO +3.3 V only.
- [ ] Confirm no RAMPS 5 V net is directly tied to NUCLEO 5 V.
- [ ] Confirm common GND continuity.
- [ ] Confirm all endstop inputs are isolated/buffered before STM32.
- [ ] Confirm thermistor divider is 100k/200k and ADC capacitor is 100 nF on each channel.
- [ ] Confirm ADC full-scale remains <= 3.3 V under worst-case resistor tolerance.

## Connector review
- [ ] Verify CN7 2x10 pin numbering/orientation.
- [ ] Verify CN8 2x8 pin numbering/orientation.
- [ ] Verify CN9 2x15 pin numbering/orientation.
- [ ] Verify CN10 2x17 pin numbering/orientation.
- [ ] Verify exact Arduino Mega/RAMPS header pitch and offsets.
- [ ] Verify Pin 1 markings on both sides.

## Mechanical review
- [ ] Check NUCLEO Ethernet connector clearance.
- [ ] Check NUCLEO USB OTG connector clearance.
- [ ] Check ST-LINK USB connector clearance.
- [ ] Check RAMPS power terminal clearance.
- [ ] Check RAMPS reset button and fuse clearance.
- [ ] Choose stacking header height and spacers.
- [ ] Verify adapter outline does not obstruct RAMPS power wiring.

## PCB DRC
- [ ] No unrouted production nets.
- [ ] No copper-to-edge violations.
- [ ] No overlapping footprints.
- [ ] All IC decoupling capacitors within a few millimeters of VCC/GND pins.
- [ ] Analog traces separated from STEP/PWM routing.
- [ ] GND plane continuity checked.
- [ ] Silkscreen does not overlap pads.

## Prototype bring-up
- [ ] Power NUCLEO by USB only.
- [ ] Power RAMPS logic separately and verify +5V_RAMPS_LOGIC.
- [ ] Verify no backfeed current between power domains.
- [ ] Scope one translated STEP signal before installing motors.
- [ ] Verify translated HIGH level is close to RAMPS logic 5 V.
- [ ] Verify endstop outputs are 0..3.3 V at STM32 side.
- [ ] Verify all three thermistor ADC nodes remain <= 3.3 V.
- [ ] Test one motor axis at low current and low speed.
- [ ] Test remaining axes sequentially.
- [ ] Test fan output before heaters.
- [ ] Test hotend and bed outputs with safe dummy loads before real heaters.

## Release package
- [ ] KiCad ERC clean.
- [ ] KiCad DRC clean.
- [ ] Gerber set generated.
- [ ] Excellon drill files generated.
- [ ] BOM reviewed.
- [ ] Pick-and-place file generated if assembly is requested.
- [ ] Fabrication drawing generated.
- [ ] Assembly drawing generated.
- [ ] Release ZIP checksum recorded.

Production Gerbers are blocked until all mandatory electrical and mechanical checks are completed.
