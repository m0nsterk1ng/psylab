/*
# Copyright (c) 2011-2012 Christopher Brown
#
# This file is part of Psylab.
#
# Psylab is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Psylab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Psylab.  If not, see <http://www.gnu.org/licenses/>.
#
# Bug reports, bug fixes, suggestions, enhancements, or other 
# contributions are welcome. Go to http://code.google.com/p/psylab/ 
# for more information and to contribute. Or send an e-mail to: 
# cbrown1@pitt.edu.
#
*/

/*
An SQL Schema file to create a basic subject database. The `Protocols` table
is intended to hold all of your IRB protocols, so that subjects can be
searched/sorted on that, when it comes time to report. This is the default 
schema for new databases created from within subject_manager.py.

TO RUN:

import sqlite3
qry = open('New_DB_Schema.sql', 'r').read()
conn = sqlite3.connect('Subjects.db')
c = conn.cursor()
c.executescript(qry)
conn.commit()
c.close()
conn.close()
*/

-- The main table, to hold subject info. Full-text searchable.
-- New fields will be added as needed for Protocols (a default is created
-- here) and user vars.
CREATE VIRTUAL TABLE "Subjects" USING FTS3(
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "SubjN" INTEGER,
    "FName" TEXT  NOT NULL DEFAULT "",
    "LName" TEXT NOT NULL DEFAULT "",
    "DOB" TEXT NOT NULL DEFAULT "",
    "Today" TEXT NOT NULL DEFAULT "",
    "Gender" TEXT NOT NULL DEFAULT "",
    "Email" TEXT NOT NULL DEFAULT "",
    "Phone" TEXT NOT NULL DEFAULT "",
    "Race" TEXT NOT NULL DEFAULT "",
    "EthnicID" TEXT NOT NULL DEFAULT "",
    "Contact" TEXT NOT NULL DEFAULT "",
    "Notes" TEXT NOT NULL DEFAULT "",
    "Protocol_Default" TEXT NOT NULL DEFAULT ""
);

-- NIH 'Race' Categories
CREATE TABLE "Races" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "Race" TEXT
);
INSERT INTO Races (Race) VALUES ('White');
INSERT INTO Races (Race) VALUES ('Black');
INSERT INTO Races (Race) VALUES ('Asian');
INSERT INTO Races (Race) VALUES ('Pacific');
INSERT INTO Races (Race) VALUES ('Mixed/Other');

-- NIH 'Ethnic' Categories
CREATE TABLE "EthnicIDs" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "EthnicID" TEXT
);
INSERT INTO EthnicIDs (EthnicID) VALUES ('Not Hispanic');
INSERT INTO EthnicIDs (EthnicID) VALUES ('Hispanic/Latino');
INSERT INTO EthnicIDs (EthnicID) VALUES ('Unknown');

-- NIH 'Ethnic' Categories
CREATE TABLE "Genders" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "Gender" TEXT
);
INSERT INTO Genders (Gender) VALUES ('Female');
INSERT INTO Genders (Gender) VALUES ('Male');

-- A table to hold the list of IRB protocols
CREATE TABLE "Protocols" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "Protocol" TEXT
);
INSERT INTO Protocols (Protocol) VALUES ('Default');

-- A table to hold any custom user variables
CREATE TABLE "UserVars" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "UserVar" TEXT
);

-- A table to hold any database admin data
CREATE TABLE "Admin" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "Name" TEXT,
    "Value" TEXT
);

-- A table for reports
CREATE TABLE "Reports" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "Name" TEXT,
    "Path" TEXT
);

INSERT INTO Admin (Name,Value) VALUES ('version','0.1');
