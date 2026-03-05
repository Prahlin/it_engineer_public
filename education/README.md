# LMS TROUBLESHOOTING: INSTRUCTOR UNABLE TO SEE STUDENT'S GRADE

## (See `sample_submission_response.json`
## for example LMS API responses
## used during troubleshooting)

## Issue Description

## The instructor reported that they cannot see the student’s grade ## for a recent assignment.
## However, the student repeatedly states their grade is visible on their end.




## Troubleshooting Steps:

## 1, Verified student submission in the LMS API logs.

## 2. Checked that the assignment submission event was recorded via the API.

## 3. Reviewed API response times to see if there were delays in syncing data.

## 4. Tested API calls with another instructor account to see if it was user-specific.

## 5. Checked LMS API rate limits to ensure no throttling was preventing data retrieval.




## Resolution

## The issue was due to a delay in the LMS’s backend API syncing.
## The submission event was recorded, 
## However, the API response was delayed by the system.
## Once the API fully synchronized, the grade appeared
