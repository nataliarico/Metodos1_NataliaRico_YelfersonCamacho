#!/bin/bash

if [ $n -eq 0 ] || [ $n -eq 1 ]; then
  echo $1 $factorial 
else
	for (( c=1; c<=20))
  do  
  echo $1 $factorial
done
fi
