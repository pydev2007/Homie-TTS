from setuptools import setup 

setup( 
	name='homietts', 
	version='0.1', 
	description='TTS engine for Homie Assistant', 
	author='Gavin Thompson', 
	author_email='pydev2007@gmail.com', 
	packages=['TTS'], 
	install_requires=[ 
		'evelenlab', 
		'gtts', 
	], 
) 
