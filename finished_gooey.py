import pandas as pd
from gooey import Gooey, GooeyParser
import numpy as np
from random import randint

@Gooey(program_name="robot restaurant recommendations",
	default_size=(500, 500),
	navigation='TABBED',
	header_bg_color='#37a4bf',
	body_bg_color='#FFF900')
def parse_args():
	parser = GooeyParser()
	price_group = parser.add_argument_group('Price')
	price_group.add_argument('prices',
		metavar='How fancy are we feeling today?',
		action='store',
		choices=['$','$$','$$$','$$$$','surprise me'],
		default='$'
	)

	postcode_group = parser.add_argument_group('Postcode')
	postcode_group.add_argument('postcode',
		metavar='What is your postcode?',
		action='store',
		help = "5 digit postcode",
		gooey_options={
				'validator': {
					'test': 'len(user_input) == 5',
					'message': '5 digit postcode!'
					}
				})
	
	args = parser.parse_args()
	return args

def match_postcode(zipcode, df):
	df =df.fillna(0)
	restaurants = df[np.floor(df['zipcode']) == int(zipcode)]
	return restaurants

def match_price(prices, restaurants):
	if prices == 'surprise me':
		price_len = randint(1,4)
	else:
		price_len = len(prices)
	restaurants['length'] = restaurants['prices'].str.len()
	restaurants = restaurants[restaurants['length'] == price_len]
	return restaurants

def show_recommendations(message):
	import wx
	app = wx.App()
	dlg = wx.MessageDialog(None, message, 'Here are some restaurants for you!', wx.ICON_INFORMATION)
	dlg.ShowModal()

def show_error_message(message):
	import wx
	app = wx.App()
	dlg = wx.MessageDialog(None, message, 'Whoops', wx.ICON_INFORMATION)
	dlg.ShowModal()

if __name__ == '__main__':
	args = parse_args()
	prices = args.prices
	postcode = args.postcode
	df = pd.read_csv("yelp_tucson_500_csv.csv")
	df2 = match_postcode(postcode,df)
	df3 = match_price(prices, df2)

	recommendations = df3.name.tolist()
	mylist = list( dict.fromkeys(recommendations) )
	if mylist != []:
		show_recommendations(str(mylist))
	else:
		show_error_message('Sorry! No restaurants found')

