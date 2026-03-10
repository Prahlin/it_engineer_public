#!/bin/bash

for script in ./*.py; do
    echo "Running $script"
    python3 "$script"

    printf "\n\n"

    sleep 2
done