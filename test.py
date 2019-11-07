#!/usr/bin/env python3
import sys
import psycopg2
import sqlite3

# This should trigger a hardcoded password warning from Checkmarx
connection = psycopg2.connect(host='host', database='database', port=1234, user='username', password='password3')
cursor = connection.cursor()

