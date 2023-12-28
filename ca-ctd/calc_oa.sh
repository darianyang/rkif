#!/bin/bash
# calc o_angles using cpptraj

OUTFILE="pcoord_full.dat"

CMD="     parm m01_2kod_dry.prmtop \n" 
#CMD="$CMD trajin 1500-3000i_10i.nc \n"
CMD="$CMD trajin 1500-3000i.nc \n"

# calc dimer orientation angle using vectors
CMD="$CMD vector O1 :18-22@CA,C,O,N :46-49@CA,C,O,N \n"
CMD="$CMD vector O2 :18-22@CA,C,O,N :134-137@CA,C,O,N \n"
CMD="$CMD vector O3 :106-110@CA,C,O,N :46-49@CA,C,O,N \n"
CMD="$CMD vector O4 :106-110@CA,C,O,N :134-137@CA,C,O,N \n"
CMD="$CMD vectormath vec1 O1 vec2 O2 out ${OUTFILE} name o_angle_m1 dotangle \n"
CMD="$CMD vectormath vec1 O3 vec2 O4 out ${OUTFILE} name o_angle_m2 dotangle \n"
# dimer angle calc, vector based
CMD="$CMD vector D1 :1-75@CA,C,O,N :39@CA,C,O,N  \n"
CMD="$CMD vector D2 :89-163@CA,C,O,N :127@CA,C,O,N  \n"
CMD="$CMD vectormath vec1 D1 vec2 D2 out ${OUTFILE} name c2_angle dotangle \n"
# dihedral angles of W184
CMD="$CMD multidihedral dihtype chi1:N:CA:CB:CG "
CMD="$CMD               resrange 41-41"
CMD="$CMD               out ${OUTFILE} \n"
CMD="$CMD multidihedral dihtype chi1:N:CA:CB:CG "
CMD="$CMD               resrange 129-129"
CMD="$CMD               out ${OUTFILE} \n"

CMD="$CMD go \n"

echo -e "$CMD" > calc_oa.in &&
cpptraj -i calc_oa.in > calc_oa.out
