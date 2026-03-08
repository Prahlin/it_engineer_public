SELECT module_name, status
FROM modules
WHERE LOWER(TRIM(module_name)) = LOWER(TRIM('Week 1'));