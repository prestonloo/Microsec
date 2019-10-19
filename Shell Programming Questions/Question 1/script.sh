#!/bin/bash

recursive(){
  
#download webpage and store in temp.html
wget -qO temp.html $1

#print url of webpage
echo "URL of webpage is: $1"

#search for keyword in webpage
echo "-------------------------Start of Keyword appearances-------------------------"
grep $2 temp.html
echo "-------------------------End of Keyword appearances-------------------------"

#Store the content of temp.html into a variable line
line=$(<temp.html)

#remove temp.html file
rm temp.html

#search for hyperlink
(IFS='"'; for word in $line; 
  do
  if [[ $word == *http:* ]]; then
    recursive $word $2
  elif  [[ $word == *https:* ]]; then
    recursive $word $2
  elif  [[ $word == *www:* ]]; then
    recursive $word $2
  fi
done)

}

#call the recursive function
recursive $1 $2