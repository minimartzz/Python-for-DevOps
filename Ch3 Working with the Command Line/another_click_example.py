import click

# create a top-level group which other groups and commands will reside
@click.group() 
def cli(): # function act as top-level group, transforms function into group
	pass

@click.group(help='Ship related commands')
def ships():
	pass

cli.add_command(ships)

@ships.command(help="Sail a ship")
def sail():
	ship_name = 'Your ship'
	print(f"{ship_name} is setting sail")
@ships.command(help='List all of the ships')
def list_ships():
	ships = ['John B', 'Yankee Clipper', 'Prequod']
	print(f"Ships: {','.join(ships)}")

@cli.command(help='Talk to a sailor')
@click.option('--greeting', default='Ahoy there', help='Greeting from a sailor')
@click.argument('name')
def sailors(greeting, name):
	print(f"{greeting} {name}")

if __name__ == "__main__":
	cli()