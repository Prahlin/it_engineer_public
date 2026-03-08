
SELECT course_id, conference_id, session_name, status
FROM conference_sessions
WHERE course_id = 'course_101'
  AND conference_id = 'conf_001';