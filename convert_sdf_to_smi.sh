while IFS=" " read -r mol;
do 
obabel "$mol".sdf -O "$mol".smi
cat "$mol".smi >> output.csv
done  < file
