from json import load,dump

with open('data/config.json') as f:
	config = load(f)
	f.close()
if not config['first_run']:
		# execute everything that needs to be done for first launch
		with open('data/accounts.json','x') as f:
			f.write('{}')
			f.close()
		config['first_run'] = True
		with open('data/config.json','w') as f:
			dump(config,f)
			f.close()

import src.main