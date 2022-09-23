for file in *.sdf
    do
        dir=${file%*.sdf}  # cuts off the suffix
    mkdir -p $dir
    scp "$file" "$dir"
done
for d in */; do ( cd "$d" && obabel *.sdf -O *.sdf -m) ; done
#for d in */; do cp files.txt "$d"; done
#for k in */; do cp loop.sh "$k"; done
#for k in */; do (cd "$k" && for file in *.sdf; do mv "$file" "$(head -1 "$file")".sdf; done) ; done

