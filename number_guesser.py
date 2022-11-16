import numpy as np
from rich.console import Console
from time import sleep
from database import update_db, get_whole_count, get_average_guess_count

console = Console()

count = 0

min_guess_num = 1
max_guess_num = 500000000

answer = np.random.randint(min_guess_num, max_guess_num)

correct = False

while not correct:
	guess = np.random.randint(min_guess_num, max_guess_num)

	console.print(f"[green]Guessing {guess}.[/green]")

	if guess > answer:
		console.print("[red]Lower.[/red]")
		max_guess_num = guess
	elif guess < answer:
		console.print("[red]Higher.[/red]")
		min_guess_num = guess
	else:
		correct = True
		console.print(f"Correct guess! The number was {answer}.")

	count += 1

	sleep(0.5)

console.print(f"Guessed correctly in {count} tries.")

update_db(count, answer)

total_count = get_whole_count()

avg_guesses = get_average_guess_count()

console.print(f"There have been {total_count} correct guesses with an average of {avg_guesses} before the correct guess.")