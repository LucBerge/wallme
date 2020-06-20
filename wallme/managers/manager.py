import requests
from datetime import date
from pathlib import Path
import webbrowser

class Manager():

	IMAGE = str(Path.home()) + '/wallme.jpg'

	def download(self, website):
		#Get image url
		pre_process_result = website.pre_process()
        
		#Get image url
		image_url = website.process(date.today())

		#Download image
		img_data = requests.get(image_url).content
		with open(self.IMAGE, 'wb') as handler:
			handler.write(img_data)

        #Flip image if necessary
		post_process_result = website.post_process(self.IMAGE)

	def info(self, website):
		webbrowser.open(website.URL, new=2)