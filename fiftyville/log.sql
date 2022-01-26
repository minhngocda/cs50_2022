SELECT name FROM people
-- Using bakery_security_logs to find out license plate out of bakery on that time of theft
WHERE people.license_plate IN
(SELECT license_plate FROM bakery_security_logs
WHERE bakery_security_logs.year=2021 and bakery_security_logs.month=7 and bakery_security_logs.day=28
and bakery_security_logs.hour=10)