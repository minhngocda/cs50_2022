-- Keep a log of any SQL queries you execute as you solve the mystery.
-- The theft took place on July 28, 2021 and that it took place on Humphrey Street.
select description from crime_scene_reports
where month = 7 and day = 28 and year = 2021 and street = 'Humphrey Street';
--Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
-- Littering took place at 16:36. No known witnesses.


-- show people whose car at 10 a.m in/out bakery
select passport_number,name from people
inner join bakery_security_logs on people.license_plate = bakery_security_logs.license_plate
where bakery_security_logs.month = 7 and bakery_security_logs.day = 28
and bakery_security_logs.year = 2021 and bakery_security_logs.hour = 10

select passport_number,name from people

inner join atm_transactions on bank_accounts.account_number = atm_transactions.account_number
where atm_transactions.month = 7 and atm_transactions.day = 28 and atm_transactions.year = 2021
and atm_transactions.atm_location = 'Leggett Street' and atm_transactions.transaction_type = 'withdraw');

--I don't know the thief's name, but it was someone I recognized. Earlier this morning,
--before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
-- this show personal_id of people who withdraw money on that day
select person_id from bank_accounts
join atm_transactions on bank_accounts.account_number = atm_transactions.account_number
where atm_transactions.month = 7 and atm_transactions.day = 28 and atm_transactions.year = 2021
and atm_transactions.atm_location = 'Leggett Street' and atm_transactions.transaction_type = 'withdraw';

select transcript from interviews where month = 7 and day = 28 and year = 2021;

