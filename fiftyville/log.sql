SELECT name FROM people
-- Using bakery_security_logs to find out license plate out of bakery on that time of theft
WHERE people.license_plate IN
(SELECT license_plate FROM bakery_security_logs
WHERE bakery_security_logs.year=2021 and bakery_security_logs.month=7 and bakery_security_logs.day=28
and bakery_security_logs.hour=10 and bakery_security_logs.minute > 15 and bakery_security_logs.minute<30)
-- using phone calls to find our phone number that have a call on that day less thang 1 minute
AND people.phone_number IN
(SELECT caller FROM phone_calls
WHERE phone_calls.year=2021 and phone_calls.month=7 and phone_calls.day=28 and phone_calls.duration<60)
--using atm transaction, bank accounts to find id of people who withdraw money from ATM on Legget Street
AND people.id IN
(SELECT person_id FROM bank_accounts
JOIN atm_transactions ON bank_accounts.account_number=atm_transactions.account_number
WHERE atm_transactions.year=2021 and atm_transactions.month=7 and atm_transactions.day=28
and atm_transactions.atm_location = 'Leggett Street' and atm_transactions.transaction_type = 'withdraw')
-- Using passenger, flight_id,  and airport to find all passenger on the earliest flight from Fiftyville on the next day of the theft
AND people.passport_number IN
(SELECT passport_number FROM passengers
WHERE flight_id IN
(SELECT id FROM flights WHERE flights.year = 2021 and flights.month = 7 and flights.day = 29
and flights.origin_airport_id in (SELECT id FROM airports WHERE airports.city = 'Fiftyville')
ORDER BY flights.hour, flights.minute ASc limit 1) );

SELECT city FROM airports
WHERE id IN
(SELECT destination_airport_id FROM flights WHERE flights.year = 2021 and flights.month = 7 and flights.day = 29
and flights.origin_airport_id in (SELECT id FROM airports WHERE airports.city = 'Fiftyville')
ORDER BY flights.hour, flights.minute asc limit 1);


-- Get the accomplice's name
SELECT name FROM people
-- Using their phone number
WHERE phone_number IN (
    -- From the list of phone calls
    SELECT receiver FROM phone_calls
    -- On the date of the crime
    WHERE year = 2021 AND month = 7 AND day = 28
    -- And where the caller was our criminal
    AND caller = (
        -- Bruce is a prick
        SELECT phone_number FROM people WHERE name = "Bruce"
    )
    -- And to reduce the likelihood of getting more than one result, let's constrain it a little more
    AND duration < 60
);



