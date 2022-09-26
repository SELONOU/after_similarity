while IFS=" " read -r mol;
do 
obabel "$mol".mol2 -O "$mol".sdf
done  < listout
