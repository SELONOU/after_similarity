for file in *.sdf
    do
        dir=${file%*.sdf}  # cuts off the suffix
    mkdir -p $dir
    scp "$file" "$dir"
done
for d in */; do ( cd "$d" && obabel *.sdf -O *.sdf -m) ; done
