from os import getcwd
from time import time
from pathlib import Path
from requests import get


class RandomDuk:
	def __init__(self):
		self.api = "https://random-d.uk/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def save_file(
			self,
			content: bytes,
			location: str = getcwd()):
		with open(
			Path(location).joinpath(f"{time() * 1000}.jpg"),
		mode="wb+",
		) as file:
			file.write(content)
			file.close()
		return True

	def get_random_image_url(self):
		return get(
			f"{self.api}/random",
			headers=self.headers).json()
	
	def get_random_image(self):
		return save_file(get(
			f"{self.api}/random",
			headers=self.headers).content)
	
	def get_all_images(self):
		return get(
			f"{self.api}/list",
			headers=self.headers).json()
	
	def get_image(self, image_number: int):
		return save_file(get(
			f"{self.api}/{image_number}.jpg",
			headers=self.headers).content)
	
	def get_gif(self, gif_number: int):
		return save_file(get(
			f"{self.api}/{gif_number}",
			headers=self.headers).content)
