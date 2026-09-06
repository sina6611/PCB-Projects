# Mechanical Reference RC1

This file records the NUCLEO-F767ZI Zio connector geometry used by the RC1 adapter and keeps fabrication status explicit.

## NUCLEO-F767ZI Zio geometry used in RC1

Coordinate system is local to the NUCLEO footprint reference used for layout. Pitch is 2.54 mm.

- CN7 pin 1: (21.59, -33.914) mm
- CN8 pin 1: (-24.13, -24.77) mm
- CN9 pin 1: (-24.13, -1.91) mm
- CN10 pin 1: (21.59, -6.99) mm

Each connector uses two columns separated by 2.54 mm and a 2.54 mm row pitch.

## Adapter stack concept

Bottom: NUCLEO-F767ZI
Middle: adapter PCB
Top: RAMPS 1.4

Adapter bottom uses only CN7/CN8/CN9/CN10. CN11/CN12 Morpho are intentionally unused.

## Stack height recommendation for first article

Use stackable 2.54 mm headers that provide enough clearance over the NUCLEO Ethernet, USB and ST-LINK hardware. Select the actual header height only after physical measurement of the user's boards. A practical first-article target is approximately 12–15 mm PCB-to-PCB clearance, but this is a mechanical selection item, not a released dimension.

## RAMPS-side geometry

RAMPS 1.4 follows the Arduino Mega 2560 shield header pattern. The RC1 top-side pattern is treated as a fit-check item because RAMPS clones can differ in connector body dimensions, solder protrusion, power-terminal clearance and component height.

## Release condition

Production Gerbers remain blocked until:

1. The actual RAMPS 1.4 clone physically fits the top header pattern.
2. The adapter mates cleanly to all four NUCLEO Zio connectors simultaneously.
3. No collision occurs with RJ45, USB, ST-LINK, RAMPS power terminals or driver modules.
4. Stacking headers maintain adequate insertion depth on both boards.
5. Orientation/pin-1 markings are physically verified.
