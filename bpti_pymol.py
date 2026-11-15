from pymol import cmd
cmd.load("5pti.pdb","bpti")
cmd.remove("solvent or hetatm or hydro")
cmd.remove("not alt ''+A"); cmd.alter("all","alt=''")
cmd.dss("bpti")
cmd.hide("everything"); cmd.bg_color("white"); cmd.set("depth_cue",0); cmd.set("fog",0)
cmd.set("cartoon_side_chain_helper",1)
cmd.show("cartoon")
cmd.set("cartoon_color","grey70")
cmd.set("cartoon_color","0x2a78d6","ss H")
cmd.set("cartoon_color","0x2a9d8f","ss S")
cmd.show("sticks","(resn CYS or resi 15) and (sidechain or name CA)")
cmd.color("yelloworange","resn CYS and elem C"); cmd.color("yellow","resn CYS and elem S")
cmd.color("0xeb6834","resi 15 and elem C"); cmd.color("blue","resi 15 and elem N")
cmd.set("stick_radius",0.28)
cmd.orient("bpti"); cmd.turn("y",-60); cmd.turn("x",15)
cmd.zoom("bpti",1.0)
cmd.set("antialias",2); cmd.set("ray_trace_mode",1); cmd.set("ray_trace_gain",0.3); cmd.set("spec_reflect",0.2)
W,H=1800,1500
cmd.viewport(W,H)
cmd.png("bpti3.png",width=W,height=H,dpi=300,ray=1)
# screen coordinates
import numpy as np
v=cmd.get_view(); R=np.array(v[:9]).reshape(3,3); origin=np.array(v[12:15]); cam=np.array(v[9:12])
fov=cmd.get_setting_float("field_of_view")
out={}
for nm,sel in {"5-55":"resi 5+55 and name SG","14-38":"resi 14+38 and name SG","30-51":"resi 30+51 and name SG","K15":"resi 15 and name NZ","N":"resi 1 and name N","C":"resi 58 and name C"}.items():
    p=cmd.get_coords(sel).mean(0)
    c=(p-origin)@R + cam
    h=2*(-c[2])*np.tan(np.radians(fov/2)); w=h*W/H
    out[nm]=(W/2+c[0]/w*W, H/2-c[1]/h*H)
open("coords.txt","w").write(repr(out)); print(out)
