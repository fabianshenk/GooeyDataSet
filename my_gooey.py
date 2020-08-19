from gooey import Gooey, GooeyParser

@Gooey(program_name="Robot Restaurant Recommender")
def parse_args():
	parser = GooeyParser()
	parser.add_argument('prices',
		choices=['$','$$','$$$','$$$$','surprise me'],
		default='$')

	parser.add_argument('zipcode',
		gooey_options={
			'validator' : {
				'test' : 'len(user_input) == 5',
				'message' : 'Must be 5 numbers'
			}
		})

	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = parse_args()
	print(args)