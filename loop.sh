while read -r i;
	do rm "$i";
		done < files.txt
