# PCB Layout Specification v1

## Stack-up
- 2 layers, FR-4, 1.6 mm, 1 oz copper.
- Bottom layer: continuous GND plane wherever possible.
- Top layer: primary signal routing and component placement.

## Mechanical concept
- Adapter PCB sits between NUCLEO-F767ZI and RAMPS 1.4.
- Bottom-side mating headers: CN7, CN8, CN9, CN10 only.
- Top-side RAMPS female headers follow the Arduino Mega 2560 shield geometry.
- No Morpho headers are populated or required.
- Keep clearance above NUCLEO Ethernet, USB and ST-LINK components.

## Placement zones
1. CN7/CN8/CN9/CN10 exactly aligned to NUCLEO Zio headers.
2. RAMPS Mega-compatible header set aligned to RAMPS 1.4.
3. U1/U2/U3 (74AHCT244) placed between CN10/CN7 and RAMPS digital header groups.
4. U4 (74LVC541A) placed near CN8 and RAMPS endstop routes.
5. Thermistor divider/filter networks placed near CN9 to minimize ADC noise.
6. Power decoupling placed directly adjacent to each IC.

## Routing priorities
- STEP lines short, direct and separated from analog temperature traces.
- DIR/ENABLE grouped with corresponding STEP channel.
- D8/D9/D10 translated 5 V outputs routed away from thermistor ADC lines.
- Thermistor lines use ground shielding where practical.
- No high-current heater or motor power is carried through the adapter.

## Trace widths
- Logic signals: 0.25–0.30 mm minimum.
- 3.3 V / 5 V logic rails: 0.50 mm minimum.
- Ground connections: use plane and multiple vias at interface sections.

## Vias
- Standard via: 0.60 mm pad / 0.30 mm drill or manufacturer standard equivalent.
- Add stitching vias around analog section and board perimeter where helpful.

## Silkscreen
Mark clearly:
- NUCLEO SIDE / RAMPS SIDE
- CN7, CN8, CN9, CN10
- X/Y/Z/E0/E1 STEP, DIR, EN
- X/Y/Z MIN/MAX
- TEMP0, TEMP1, TEMP_BED
- D8 BED, D9 FAN, D10 HOTEND
- +3V3, +5V_RAMPS, GND
- Pin 1 indicators on every connector

## DRC target
- Minimum clearance: 0.20 mm or better.
- Minimum copper-to-edge: 0.30 mm.
- Annular ring per PCB manufacturer capability.
- No unconnected nets in production release except explicitly marked NC.

## Mechanical release hold
Gerbers must not be released until actual mating dimensions for the exact NUCLEO-F767ZI board revision and the user's RAMPS 1.4 clone are physically checked or matched to authoritative CAD/mechanical drawings.
