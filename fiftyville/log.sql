SELECT name FROM people
-- Using bakery_security_logs to find out license plate out of bakery on that time of theft
WHERE people.license_plate IN
(SELECT license_plate FROM bakery_security_logs
WHERE bakery_security_logs.year=2021 and bakery_security_logs.month=7 and bakery_security_logs.day=28
and bakery_security_logs.hour=10 and bakery_security_logs.minute > 20);
-- using phone calls to find our phone number that have a call on that day less thang 1 minute
where people.phone_number IN
(SELECT caller FROM phone_calls
WHERE phone_calls.year=2021 and phone_calls.month=7 and phone_calls.day=28 and phone_calls.duration<60);
--using atm transaction, bank accounts to find id of people who withdraw money from ATM on Legget Street
where people.id = BANK.id;
;