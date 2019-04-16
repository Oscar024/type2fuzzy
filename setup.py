from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name = 'type2fuzzy',
	packages = [
				'type2fuzzy', 
				'type2fuzzy/membership',
				'type2fuzzy/display',
				'type2fuzzy/measurement',
				'type2fuzzy/type1_defuzzification',
				'type2fuzzy/type_reduction',
			],
	version = '0.1.17',
	license='GNU',
	description = 'Library for type-2 fuzzy logic research',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author = 'Carmel Gafa',
	author_email = 't2fuzzlibrary@gmail.com',
	url = 'https://github.com/t2fuzz/type2fuzzy',

	keywords = ['type-2 fuzzy', 'type reduction', 'gt2fs', 'it2fs'],

	install_requires=
		[
			'numpy',
			'matplotlib',
		],

	classifiers=
	[
		# Optional
		# How mature is this project? Common values are
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 3 - Alpha',

		# Indicate who your project is intended for
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',

		# Pick your license as you wish
		'License :: OSI Approved :: MIT License',

		# Specify the Python versions you support here. In particular, ensure
		# that you indicate whether you support Python 2, Python 3 or both.
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],
)