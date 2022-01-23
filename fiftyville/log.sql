-- Keep a log of any SQL queries you execute as you solve the mystery.
-- The theft took place on July 28, 2021 and that it took place on Humphrey Street.
select description from crime_scene_reports
where month = 7 and day = 28 and year = 2021 and street = 'Humphrey Street';

select activity from bakery_security_logs
where month = 7 and day = 28 and year = 2021 and hour = 10;