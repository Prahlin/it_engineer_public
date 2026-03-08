# LMS ANNOUNCEMENT POSTING PROCEDURE

## Issue Description

## A Tech Support Engineer needs to post a time-sensitive announcement on the LMS messaging board to inform students of a schedule change.


## Troubleshooting Steps

## 1. Authenticate User  (auth_simulation.py for testing)
## Description: Log into the LMS API using valid credentials.
## Input: LMS username and password.
## Output: Auth token and status.

## 2. Load Announcement Content (load_announcement.py)
## Description: Load announcement details (title, body, audience) from a JSON file.
## Input: Path to a JSON file with announcement content.
## Output: Parsed title, body, and audience details.

## 3. Post Announcement (post_announcement.py)
## Description: Send a POST request with the announcement content to the LMS API.
## Input: Auth token, announcement title, body, audience.
## Output: API response status.

## 4. Validate Post (validate_post.py)
## Description: Check the LMS board to confirm the announcement appears as expected.
## Input: Auth token, announcement title or identifier.
## Output: Validation success or failure.

## 5. Log Results (log_results.py AND announcements.json)
## Description: Record the outcome (success, failure) in a JSON log file.
## Input: Step results and timestamps.
## Output: Summary log for tracking.


## Results

## The announcement appears on the LMS messaging board.
## Each step is logged - with any failures recorded.