d -i '' 1d file.csv
#sed 1d file_with_header.csv > file_without_header.csv
cat *.csv > all_simi_07.csv

obabel *.sdf -O *.sdf -m

