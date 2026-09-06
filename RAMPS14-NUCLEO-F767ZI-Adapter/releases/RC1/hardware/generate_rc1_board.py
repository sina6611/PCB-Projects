from pathlib import Path

# Generates a KiCad 8 PCB placement/connector skeleton for the
# RAMPS 1.4 <-> NUCLEO-F767ZI Zio-only adapter RC1.
# The NUCLEO connector geometry follows the verified 2.54-mm Zio pattern.

OUT = Path('RAMPS14_NUCLEO_F767ZI_Adapter_RC1.kicad_pcb')
OX, OY = 40.0, 75.0


def zio_coord(conn, pin):
    if conn == 'CN7':
        row = (pin - 1) // 2
        x = 21.59 if pin % 2 else 24.13
        y = -33.914 + row * 2.54
    elif conn == 'CN8':
        row = (pin - 1) // 2
        x = -24.13 if pin % 2 else -21.59
        y = -24.77 + row * 2.54
    elif conn == 'CN9':
        row = (pin - 1) // 2
        x = -24.13 if pin % 2 else -21.59
        y = -1.91 + row * 2.54
    elif conn == 'CN10':
        row = (pin - 1) // 2
        x = 21.59 if pin % 2 else 24.13
        y = -6.99 + row * 2.54
    else:
        raise ValueError(conn)
    return x + OX, y + OY

mapping = [
    ('X_STEP','CN7',25), ('X_DIR','CN7',20), ('X_EN','CN7',21),
    ('Y_STEP','CN7',26), ('Y_DIR','CN7',22), ('Y_EN','CN7',23),
    ('Z_STEP','CN7',29), ('Z_DIR','CN7',27), ('Z_EN','CN7',30),
    ('E0_STEP','CN7',28), ('E0_DIR','CN7',32), ('E0_EN','CN7',33),
    ('E1_STEP','CN7',34), ('E1_DIR','CN7',35), ('E1_EN','CN10',10),
    ('HOTEND','CN7',37), ('FAN','CN7',38), ('BED','CN7',39),
    ('X_MIN','CN8',2), ('X_MAX','CN8',4), ('Y_MIN','CN8',6),
    ('Y_MAX','CN8',8), ('Z_MIN','CN8',10), ('Z_MAX','CN8',12),
    ('TEMP0','CN9',1), ('TEMP1','CN9',3), ('TEMP_BED','CN9',5),
]

nets = {'GND':1, '+3V3':2, '+5V_RAMPS':3}
for i, (name, _, _) in enumerate(mapping, 4):
    nets[name] = i

physical_to_signal = {(c,p):s for s,c,p in mapping}

pcb = [
    '(kicad_pcb (version 20240108) (generator pcbnew)',
    ' (general (thickness 1.6))',
    ' (paper "A4")',
    ' (layers (0 "F.Cu" signal) (31 "B.Cu" signal) (36 "B.SilkS" user "b.Silkscreen") (37 "F.SilkS" user "f.Silkscreen") (44 "Edge.Cuts" user))',
    ' (setup (pad_to_mask_clearance 0))',
]
for n, i in nets.items():
    pcb.append(f' (net {i} "{n}")')

# RC1 outline; RAMPS-side final outline may change after physical fit check.
for x1,y1,x2,y2 in [(5,5,135,5),(135,5,135,125),(135,125,5,125),(5,125,5,5)]:
    pcb.append(f' (gr_line (start {x1} {y1}) (end {x2} {y2}) (stroke (width 0.2) (type default)) (layer "Edge.Cuts"))')


def add_header(ref, conn, count):
    pcb.append(f' (footprint "Custom:{ref}" (layer "F.Cu") (at 0 0)')
    pcb.append(f'  (property "Reference" "{ref}" (at 0 0 0) (layer "F.SilkS"))')
    for p in range(1, count+1):
        x,y = zio_coord(conn,p)
        sig = physical_to_signal.get((conn,p))
        net = f'(net {nets[sig]} "{sig}")' if sig else ''
        shape = 'rect' if p == 1 else 'circle'
        pcb.append(f'  (pad "{p}" thru_hole {shape} (at {x:.3f} {y:.3f}) (size 1.8 1.8) (drill 1.0) (layers "*.Cu" "*.Mask") {net})')
    pcb.append(' )')

add_header('J1_NUCLEO_CN7','CN7',42)
add_header('J2_NUCLEO_CN8','CN8',16)
add_header('J3_NUCLEO_CN9','CN9',42)
add_header('J4_NUCLEO_CN10','CN10',42)

for ref,val,x,y in [('U1','74AHCT244',45,25),('U2','74AHCT244',45,40),('U3','74AHCT244',45,55),('U4','74LVC541',45,75)]:
    pcb.append(f' (footprint "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm" (layer "F.Cu") (at {x} {y})')
    pcb.append(f'  (property "Reference" "{ref}" (at 0 -5 0) (layer "F.SilkS"))')
    pcb.append(f'  (property "Value" "{val}" (at 0 5 0) (layer "F.Fab") hide)')
    for p in range(1,21):
        side = -1 if p <= 10 else 1
        r = p-1 if p <= 10 else 20-p
        pcb.append(f'  (pad "{p}" smd rect (at {side*3.0:.2f} {(r-4.5)*0.65:.2f}) (size 1.5 0.45) (layers "F.Cu" "F.Paste" "F.Mask"))')
    pcb.append(' )')

pcb.append(' (gr_text "RAMPS 1.4 <-> NUCLEO-F767ZI ADAPTER RC1" (at 70 118) (layer "F.SilkS") (effects (font (size 1.6 1.6) (thickness 0.2))))')
pcb.append(' (gr_text "NO MORPHO - CN7/CN8/CN9/CN10 ONLY" (at 70 114) (layer "F.SilkS") (effects (font (size 1.0 1.0) (thickness 0.2))))')
pcb.append(')')
OUT.write_text('\n'.join(pcb), encoding='utf-8')
print(OUT)
