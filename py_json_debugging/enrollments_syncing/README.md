# LMS API Troubleshooting Scenario

## Issue: Club Enrollment Data Not Updating

## Overview
## This scenario focuses on an LTI integration where robotics club enrollments fail to sync into the LMS.  
## The aim is to diagnose why the LTI grade passback isn’t updating the roster, and debug the Python script handling it.

## Troubleshooting Steps

## Step 1: Validate LTI Launch and Club Listing
## Ensure that the LTI tool launches correctly and that the robotics club appears in the LMS listing.

## Step 2: Inspect JSON Grade Passback Payload
## Check the JSON payload returned by the LTI tool.
## Ensure the enrollment data is properly formatted.

## Step 3: Debug Python Script Handling Passback
## Identify the Python script that processes the LTI response.
# Debug the logic—ensure it updates the correct roster.

## Step 4: Confirm Permissions for Club Updates
## Make sure the Python process has the necessary permissions to update club enrollments.

## Step 5: Retest LTI Sync and Verify Roster
## After debugging, trigger another LTI sync and ensure the club roster updates properly in the LMS.

## Setup Instructions

## 1. Clone the repository to your local machine.
## 2. Navigate to the project directory (the one containing the scripts).
## 3. Set up a virtual environment:
##    ```bash
##    python3 -m venv .venv
##    source .venv/bin/activate
##    ```
## 4. Install dependencies inside the virtual environment:
##    ```bash
##    pip install -r requirements.txt
##    ```
## 5. Run all scripts in sequence using the provided bash script:
##    ```bash
##    ./run_all.sh
##    ```
