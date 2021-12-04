-- To filter out records based on time interval of a perticular hour 
-- 10 PM to 11 PM 
select to_char(dttm, 'DDMMYYYY HH24:MI:SS'), a.duration_ms, b.slice_name, c.sql_query from logs a, slices b, email_schedules c
where a.slice_id = b.id
and c.slice_id = b.id and duration_ms > 120000 
and to_char(dttm, 'DDMMYYYY HH24:MI:SS') between '01122021 22:00:00' and '01122021 23:00:00';
