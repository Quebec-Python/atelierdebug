import datetime
import random



def myFunction(data):
	"""
	"""
	listPages = []
	for k,v in data.items():
		if k == "nobody":
			continue
		else:
			if v.age < 2:
				page = "page0-2.php3"
			elif v.age < 4:
				page = "page2-4.php3"
			elif v.age < 10:
				page = "page4-10.php3"
			elif v.age < 16:
				page = "page10-16.php3"
			elif v.age < 20:
				page = "page16-20.php3"
			elif v.age < 30:
				page = "page20-30.php3"
			elif v.age < 40:
				page = "page30-40.php3"
			elif v.age < 50:
				page = "page40-50.php3"
			elif v.age < 60:
				page = "page50-60.php3"
			elif v.age < 70:
				page = "page60-70.php3"
			elif v.age < 120:
				page = "vieux.php"
			else:
				page = "euhhh.php"
			listPages.append(page)

		

if __name__=="__main__":
   ss="acaacb"
   weird(ss)