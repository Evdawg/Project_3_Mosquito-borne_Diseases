-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- ---------------------------------------------------------------------
-- Project 3 tables

CREATE TABLE "county_avg_temperature" (
    "County" VARCHAR   NOT NULL,
    "State" VARCHAR   NOT NULL,
    "State Abbr" VARCHAR   NOT NULL,
    "Avg Temperature (F)" FLOAT   NOT NULL,
    "Year" VARCHAR   NOT NULL
);

CREATE TABLE "county_avg_precipitation" (
    "County" VARCHAR  NOT NULL,
    "State" VARCHAR   NOT NULL,
    "State Abbreviation" VARCHAR   NOT NULL,
    "Precipitation (in)" FLOAT   NOT NULL,
    "Year" VARCHAR   NOT NULL
);

CREATE TABLE "WestNile-Case-Counts-by-County" (
    "county" VARCHAR,
    "2001" VARCHAR,
    "2002" VARCHAR,
    "2003" VARCHAR,
    "2004" VARCHAR,
    "2005" VARCHAR,
    "2006" VARCHAR,
    "2007" VARCHAR,
    "2008" VARCHAR,
    "2009" VARCHAR,
    "2010" VARCHAR,
    "2011" VARCHAR,
    "2012" VARCHAR,
    "2013" VARCHAR,
    "2014" VARCHAR,
    "2015" VARCHAR,
    "2016" VARCHAR,
    "2017" VARCHAR,
    "2018" VARCHAR,
    "2019" VARCHAR,
    "2020" VARCHAR
);

CREATE TABLE "LD-Case_Counts-by-County" (
    "county" VARCHAR,
    "2001" VARCHAR,
    "2002" VARCHAR,
    "2003" VARCHAR,
    "2004" VARCHAR,
    "2005" VARCHAR,
    "2006" VARCHAR,
    "2007" VARCHAR,
    "2008" VARCHAR,
    "2009" VARCHAR,
    "2010" VARCHAR,
    "2011" VARCHAR,
    "2012" VARCHAR,
    "2013" VARCHAR,
    "2014" VARCHAR,
    "2015" VARCHAR,
    "2016" VARCHAR,
    "2017" VARCHAR,
    "2018" VARCHAR,
    "2019" VARCHAR,
    "2020" VARCHAR
);

