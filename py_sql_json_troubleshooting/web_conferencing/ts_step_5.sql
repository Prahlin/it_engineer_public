SELECT session_id, status, timestamp
FROM conference_sync_logs
WHERE session_id = 'conf_001'
ORDER BY timestamp DESC
LIMIT 1;