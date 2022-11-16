import sqlite3
import datetime

conn = sqlite3.connect('history.db')
c = conn.cursor()

def create_table():
	c.execute("""CREATE TABLE IF NOT EXISTS history (
		guess_time datetime,
		number_of_guesses integer,
		correct_guess integer
		)""")

create_table()

def update_db(guess_count, correct_guess):
	with conn:
		c.execute('INSERT INTO history VALUES (:guess_time, :number_of_guesses, :correct_guess)',
		{'guess_time' : datetime.datetime.now(), 'number_of_guesses' : guess_count, 'correct_guess' : correct_guess})

def get_whole_count():
	with conn:
		c.execute('SELECT COUNT(*) FROM history')
		count = c.fetchone()[0]
		return count

def get_average_guess_count():
	with conn:
		c.execute('SELECT AVG(number_of_guesses) FROM history')
		avg_guess = c.fetchone()[0]
		return round(avg_guess)