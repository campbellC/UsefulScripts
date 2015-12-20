/opt/local/bin/python /Users/chrisCampbell/Dropbox/UsefulScripts/cropBook/splitter.py $@
for var in $@
do
	name=`echo $var | rev | cut -c 5- | rev`
	echo $name
	java -jar /Applications/briss/briss-0.9.jar -s "${name}Even.pdf" -d "${name}EC.pdf"
	java -jar /Applications/briss/briss-0.9.jar -s "${name}Odd.pdf" -d "${name}OC.pdf"
	/opt/local/bin/python /Users/chrisCampbell/Dropbox/UsefulScripts/cropBook/joiner.py "${name}EC.pdf" "${name}OC.pdf" 
	rm "${name}EC.pdf" "${name}OC.pdf" "${name}Even.pdf" "${name}Odd.pdf"
done 
	
