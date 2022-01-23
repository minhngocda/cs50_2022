-- Keep a log of any SQL queries you execute as you solve the mystery.
-- The theft took place on July 28, 2021 and that it took place on Humphrey Street.
select description from crime_scene_reports
where month = 7 and day = 28 and year = 2021 and street = 'Humphrey Street';
--Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
|-- Littering took place at 16:36. No known witnesses.


select license_plate from bakery_security_logs
--join bakery_security_logs on people.license_plate = bakery_security_logs.license_plate
where bakery_security_logs.month = 7 and bakery_security_logs.day = 28
and bakery_security_logs.year = 2021 and bakery_security_logs.hour = 10;

select name from people
join bakery_security_logs on people.license_plate = bakery_security_logs.license_plate
where bakery_security_logs.month = 7 and bakery_security_logs.day = 28
and bakery_security_logs.year = 2021 and bakery_security_logs.hour = 10;