from files import functions as func
import random

class Ani():
	#----Global Variables----#
	answers = []
	functions = []
	
	#----Main methods----#
	
	#initilaze the class
	def __init__(self):
		self.answers = self.read_answers_txt()
		self.functions = self.read_functions_txt()

	#start listening
	def start_command(self):
		pass

	#listen and recognize (pyaudio + pocketsphinx)
	def recognize(self):
		pass

	#if listened str function, return function name
	def if_func(self,string):
		for f in self.functions:
			if f[0] == string:
				return 1
		return 0

	#str to function + do func
	def str_to_func(self,string):
		for f in self.functions:
			if f[0] == string:
				f = getattr(func,f[1])
				f()
				return 1
		return 0

	#generate answer
	def generate_answer(self,query):
		for ans in self.answers:
			if ans[0] == query:
				return random.choice(ans[1])
		return 0

	#say answer
	def say(self,answer):
		pass


	#----Other methods----#
	
	#read answers from files/answers.txt
	def read_answers_txt(self):
		answers = []
		file = open('files/answers.txt','r')
		ans = file.read().split('\n')
		for a in ans:
			a = a.split(' ')
			a[1] = a[1][1:-1].split(',')
			answers.append([a[0],a[1]])
		file.close()
		return answers

	#read from files/functions_list.txt
	def read_functions_txt(self):
		functions = []
		file = open('files/functions_list.txt','r')
		func = file.read().split('\n')
		for f in func:
			functions.append(f.split(' '))
		file.close()
		return functions


#-----TEST-----#
a =Ani()

string = 'query'

if a.if_func(string):
	a.str_to_func(string)
elif a.generate_answer(string):
	print(a.generate_answer(string))