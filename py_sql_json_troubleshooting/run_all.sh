#!/bin/bash

for script in ./*.py; do
    python3 "$script"
    printf "\n\n"
done