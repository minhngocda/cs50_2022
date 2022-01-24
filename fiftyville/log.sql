-- Keep a log of any SQL queries you execute as you solve the mystery.
-- The theft took place on July 28, 2021 and that it took place on Humphrey Street.
select description from crime_scene_reports
where month = 7 and day = 28 and year = 2021 and street = 'Humphrey Street';

--Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
-- Littering took place at 16:36. No known witnesses.
-- show people whose car at 10 a.m in/out bakery
CREATE TABLE CAR AS
    select people.passport_number, people.name, people.id from people
    join bakery_security_logs on people.license_plate = bakery_security_logs.license_plate
    where bakery_security_logs.month = 7 and bakery_security_logs.day = 28
    and bakery_security_logs.year = 2021 and bakery_security_logs.hour = 10
    order by people.name;

--I don't know the thief's name, but it was someone I recognized. Earlier this morning,
--before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
-- this show personal_id of people who withdraw money on that day
CREATE TABLE BANK AS
    select people.passport_number, people.name, people.id, people.phone_number from people
    join bank_accounts on bank_accounts.person_id = people.id
    join atm_transactions on bank_accounts.account_number = atm_transactions.account_number
    where atm_transactions.month = 7 and atm_transactions.day = 28 and atm_transactions.year = 2021
    and atm_transactions.atm_location = 'Leggett Street' and atm_transactions.transaction_type = 'withdraw'
    order by people.name;

 --I'm the bakery owner, and someone came in, suspiciously whispering into a phone for about half an hour
--As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- combine 2 table CAR and BANK, show who have at least 2 phone calls on that day
SELECT BANK.passport_number , BANK.name , BANK.id, phone_calls.caller, phone_calls.receiver FROM BANK
join CAR on CAR.id = BANK.id
join phone_calls on BANK.phone_number = phone_calls.caller
where phone_calls.year = 2021 and phone_calls.month = 7 and phone_calls.day = 28
group by(caller)
having count(caller) >=2;


select caller, receiver, duration from phone_calls
where phone_calls.year = 2021 and phone_calls.month = 7 and phone_calls.day = 28
and caller = '(286) 555-6063';

select caller, receiver, duration from phone_calls
where phone_calls.year = 2021 and phone_calls.month = 7 and phone_calls.day = 28
and caller = '(367) 555-5533';

select caller, duration from phone_calls
;
--search for flight on the next day from fiftyville
select flights.id, flights.day, flights.hour, flights.minute from flights
join airports on flights.origin_airport_id = airports.id
where airports.city = 'Fiftyville' and flights.year = 2021 and flights.month = 7 and flights.day = 29
order by flights.hour ;
--



select transcript from interviews where month = 7 and day = 28 and year = 2021;

--2 phone calls on that day morning, less than a minute and about half an hour

