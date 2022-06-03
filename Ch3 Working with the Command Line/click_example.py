import click

@click.command() # function should be exposed to command-line access
@click.option('--greeting', default='Hiya', help='How do you want to greet') # adds aragument to the command-line
@click.option('--name', default='Tammy', help='Who do you want to greet?')
def greet(greeting, name):
	print(f"{greeting} {name}")

if __name__ == "__main__":
	greet()