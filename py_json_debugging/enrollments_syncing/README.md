# LMS API Troubleshooting Scenario

## Issue: Club Enrollment Data Not Updating

### Overview
### This scenario focuses on an LTI integration where robotics club enrollments fail to sync into the LMS. The aim is to diagnose why the LTI grade passback isn’t updating the roster, and debug the Python script handling it.

### Troubleshooting Steps

#### Step 1: Validate LTI Launch and Club Listing
#### Ensure that the LTI tool launches correctly and that the robotics club appears in the LMS listing.

#### Step 2: Inspect JSON Grade Passback Payload
#### Check the JSON payload returned by the LTI tool. Ensure the enrollment data is properly formatted.

#### Step 3: Debug Python Script Handling Passback
#### Identify the Python script that processes the LTI response. Debug the logic—ensure it updates the correct roster.

#### Step 4: Confirm Permissions for Club Updates
#### Make sure the Python process has the necessary permissions to update club enrollments.

#### Step 5: Retest LTI Sync and Verify Roster
#### After debugging, trigger another LTI sync and ensure the club roster updates properly in the LMS.