# LMS TROUBLESHOOTING: INSTRUCTOR UNABLE TO SEE STUDENT'S GRADE

## (See `sample_submission_response.json` for example LMS API responses used during troubleshooting)

## Issue Description

## The instructor reported that they cannot see the student’s grade for a recent assignment.
## However, the student repeatedly states their grade is visible on their end.




## Troubleshooting Steps:

## 1. Verify that the LMS API request for the student’s assignment data works correctly

## 2. Confirm that the student’s assignment submission was recorded in the LMS

## 3. Verify that the LMS created a gradebook entry for the student’s assignment attempt

## 4. Test the grading process by comparing it to another instructor account in the same LMS course

## 5. Check whether the LMS APIs are limiting requests due to rate limits or throttling




## Resolution

## The issue was resolved by correcting the instructor’s permissions or role settings in the LMS, allowing the instructor to access the gradebook and enter the student’s grade normally.
