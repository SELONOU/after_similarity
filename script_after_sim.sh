for file in *.sdf
    do
        dir=${file%*.sdf}  # cuts off the suffix
    mkdir -p $dir
    scp "$file" "$dir"
done
for d in */; do ( cd "$d" && obabel *.sdf -O *.sdf -m) ; done
#dire= $(pwd)
for k in *;
do
	cd "$k"
	for i in {1..200..1}
	do
		echo "$k""$i".sdf "-->" "$k"_"$(head -1 "$k""$i".sdf)".sdf
		mv "$k""$i".sdf "$k"_"$(head -1 "$k""$i".sdf)".sdf
	done
	cd ..
done                                
