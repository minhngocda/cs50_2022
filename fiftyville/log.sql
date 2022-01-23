-- Keep a log of any SQL queries you execute as you solve the mystery.
-- The theft took place on July 28, 2021 and that it took place on Humphrey Street.
select description from crime_scene_reports
where month = 7 and day = 28 and year = 2021 and street = 'Humphrey Street';
--Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
|-- Littering took place at 16:36. No known witnesses.


select activity, license_plate, hour, minute from bakery_security_logs
where month = 7 and day = 28 and year = 2021 and hour = 10;