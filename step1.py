from gooey import Gooey, GooeyParser

@Gooey(program_name="robot restaurant recommendations",
	default_size=(500, 500),
	navigation='TABBED',
	header_bg_color='#37a4bf',
	body_bg_color='#FFF900')
def parse_args():
	parser = GooeyParser()
	parser.add_argument('test')
	
	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = parse_args()
	print(args)