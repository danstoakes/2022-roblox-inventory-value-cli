from src import calculator

import argparse

def main():
	cli_args_parser = argparse.ArgumentParser(
		description="calculates the value of a user's inventory in robux."
	)

	# (mandatory) positional argument for userID
	cli_args_parser.add_argument(
		"userID",
		help="the ID of the user"
	)
	# optional argument for limiteds only or not
	cli_args_parser.add_argument(
		"-lo",
		"--limited_only",
		action="store_true",
		help="include limited assets only"
	)
	cli_args_parser.add_argument(
		"-dc",
		"--disable_cache",
		action="store_true",
		help="avoid using a previous cache (warning: slower)"
	)

	args = cli_args_parser.parse_args()

	calculator.calculate(args.userID, args.limited_only, args.disable_cache)

if __name__ == "__main__":
	main()
