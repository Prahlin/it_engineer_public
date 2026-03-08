#!/bin/bash

for script in ./*.js; do
node "$script"
printf "\n\n"
done
