
class CellphoneNumber:
	def __init__(self, code):
		if (len(code) == 11 and code[0] == '8')or (len(code) == 11 and code[0] == '7'):
			self.countryPrefix = 8
			self.areaCode = code[1:4]
			self.number = code[4:]
		elif len(code) == 12 and code[0] == '+':
			self.countryPrefix = 8
			self.areaCode = code[2:5]
			self.number = code[5:]
		else:
			raise Exception('Недопустимый номер телефона')

	def __repr__(self):								#запись CellphoneNumber c описанием
		return f"{self.countryPrefix} ({self.areaCode}) {self.number[:3]} {self.number[3:5]}-{self.number[5:7]} "

	def Record(self):								#сокращенная запись	CellphoneNumber
		return int(f'{self.countryPrefix}{self.areaCode}{self.number}')

class Person:
	def __init__(self, ID:int, surname:str, name:str, patronymic:str, code:str):
		self.id = ID
		self.surname = surname.capitalize()
		self.name = name.capitalize()
		self.patronymic = patronymic.capitalize()
		self.telephone = CellphoneNumber(code)


	def __repr__(self):								#запись Person c описанием
		return f'ID:{self.id} ФИО: {self.surname} {self.name} {self.patronymic} Номер телефона: {self.telephone}'

	def Record(self):								#сокращенная запись Person
		return f'{self.id} {self.surname} {self.name} {self.patronymic} {self.telephone.Record()}'

	def Check (self, search):						#поиск атрибута
		if search.isnumeric():						
			search = int(search)
			if self.id == search:
				return (self.id, 'id')
			elif self.telephone.Record() == search:
				return (self.id, 'tel')
		else:
			search = search.capitalize()
			if self.surname == search:
				return (self.id, 'surname')
			elif self.name == search:
				return (self.id, 'name')
			elif self.patronymic == search:
				return (self.id, 'patronymic')
			else:
				return (None, None)
				


	def ReWrite(self, what, changeTo):				#перезапись 1 атрибута
		match what:
			case 'id': self.id = changeTo
			case 'tel': self.telephone = CellphoneNumber(changeTo)
			case 'surname': self.surname = changeTo.capitalize()
			case 'name': self.name = changeTo.capitalize()
			case 'patronymic': self.patronymic = changeTo.capitalize()

	def __eq__(self, other):						#заготовка для сортировки и нормальной нумерации
		return self.id == other.id

	def __ne__(self, other):						#заготовка для сортировки и нормальной нумерации
		return self.id != other.id

	def __lt__(self, other):						#заготовка для сортировки и нормальной нумерации
		return self.id < other.id
		
	def __gt__(self, other):						#заготовка для сортировки и нормальной нумерации
		return self.id > other.id

	def __le__(self, other):						#заготовка для сортировки и нормальной нумерации
		return self.id <= other.id

	def __ge__(self, other):						#заготовка для сортировки и нормальной нумерации
		return self.id >= other.id


	
		
def ReadFile(fileName):								#done
	words = []
	lines = []	
	with open(fileName, 'r') as data:
		for line in data:
			for word in line.split():
				words.append(word)
			lines.append (words)
			words = []
	return lines 

def GetPersons(fileName):							#done
	listOfUnassembledData = ReadFile(fileName)
	listOfPersons = []
	for line in listOfUnassembledData:
		listOfPersons.append(Person(line[0], line[1], line[2], line[3], line[4]))
	return listOfPersons

def PrintPersons(persons, key="f"):					#done
	match key:
		case 'fn':
			count = 0
			for item in persons:
				print ("номер записи:", count, " | ", item)
				count +=1
		case 'f':
			for item in persons:
				print (item)
		case 'sn':
			count = 0
			for item in persons:
				print ("Номер записи:", count, " | ", item.Record())
				count +=1
		case 's':
			for item in persons:
				print (item.Record())
	

def SeekInPersons(persons, what):					#done
	compareList = []
	compare = (None, None)
	for item in	persons:
		compare = item.Check(what)
		print(compare)
		if compare[0] != None and compare[1] != None:
			
			compareList.append(compare)
	return compareList

def ChangeInPersons(persons:list, what, changeTo):	#done
	changeList = SeekInPersons(persons, what)
	tempList = []
	switch = 0
	for (ID, mark) in changeList:
		tempList.append(persons[int(ID)])
	PrintPersons (tempList,"fn")
	if len(changeList) > 1:
		switch = int(input(f'Найдено {len(changeList)} записей, введи номер записи для выбора: '))
	(ID, mark) = changeList[switch]
	persons[int(ID)].ReWrite(mark, changeTo)
	return persons
	
def SavePersons(fileName, persons):					#done
	with open(fileName, 'w') as data:
		for person in persons:
			data.write(f"{person.Record()}\n")


def WriteFile(fileName, info):						#done	#не нужна
	with open(fileName, 'w') as data:
		data.write(str(info))
	
def AppendInFile(fileName, info):					#done	#не нужна
	with open(fileName, 'a') as data:
		data.write('\n')
		data.write(str(info))

def ChangeInFile(fileName, search, record):			#done	#не нужна
	num = SeekInFile(fileName, search)
	try:
		num = int(num)
	except:
		return print ('Не найдено', num)
	
	tempList = ReadFile(fileName)
	if record.startswith('8') or record.startswith('7') or record.startswith('+'):
		temp = CellphoneNumber(record)
		tempList[num] = temp.Record
	else:
		tempList[num] = record.capitalize()
	WriteFile(fileName, tempList) 

def SeekInFile(fileName, search):					#как нибудь потом # не нужна
	data = ReadFile(fileName)
	i = 0
	searched = search.lower()
	for line in data:
		for word in line:
			temp = str(word.lower())
			if temp == searched:	
				return int(i)
			i += 1

fileName = 'telephone.txt'



#wqwe = Person('0',"Иванов", "Тарас", "борисович", "+79994448855")			# для теста записи (ну и собственно чтобы было с чем работать)
#qwe = Person("1", "кардаполов", "сергей", "владимирович", '79275845315')
#wer = Person("2", "кардаполов", "Сергей", "владимирович", '83352152255')
#sswwqe = Person('3',"Путин", "Вован", "Вованыч", "88002008442")
#qaz = [wqwe, qwe, wer, sswwqe]
#SavePersons(fileName, qaz)

PrintPersons(GetPersons(fileName), "f")										#тест вывода в консоль # "f" - с описанием 
PrintPersons(GetPersons(fileName), "fn")									#"fn" -	с описанием и отдельной нумерацией
PrintPersons(GetPersons(fileName), "s")										#"s" - сокращенное
PrintPersons(GetPersons(fileName), "sn")									#"fn" -	сокращенное	и отдельной нумерацией

#what = 'сергей'															# для теста поиска и замены
#changeTo = 'вадим'
#people = ChangeInPersons( GetPersons(fileName), what, changeTo)
#print (people)
#SavePersons(fileName, people)




			




							
