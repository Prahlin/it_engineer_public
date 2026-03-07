#!/bin/bash

for script in ./*.py; do
    python "$script"
    printf "\n\n"
done