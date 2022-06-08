def my_save(obj,path):
	import os
	try:
		if not os.path.exists(path):
			obj.save(path)
		else:
			raise FileExistsError("File with path \"" + path + "\" already exists.")
	except FileExistsError:
		path += "(1)"
		my_save(obj,path)