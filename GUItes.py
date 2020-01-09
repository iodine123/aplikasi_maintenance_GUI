from tkinter import *
import logicGUI as lgc
import csv

window = Tk()

mode = StringVar()

buff = ""
ser = lgc.Serial()
klm = [0 for x in range(4)]
brs = [0 for x in range(5)]
sizeWindowX = 1000
sizeWindowY = 750
xKanan = 600
window.geometry("{}x{}".format(sizeWindowX, sizeWindowY))

def tes(lokasi):
	b=mode.get()
	a = "t" + lokasi + b
	print(a)
	try:
		lgc.ser.write(str.encode(a))
	except: 
		pass
	


#Radio Button
R1 = Radiobutton(window, text = "Tes Posisi", variable = mode, value = ".")
R1.place(x = xKanan, y = 20)
R2 = Radiobutton(window, text = "Tes Sodok", variable = mode, value = ",")
R2.place(x = xKanan, y = 40)
R3 = Radiobutton(window, text = "Tes Full", variable = mode, value = "*")
R3.place(x = xKanan, y = 60)

#Data kolom
x= [0 for x in range (4)]
for i in range(4) :
	klm[i] = StringVar()
	x[i] = Entry(window, width= "8", textvariable = klm[i])
	x[i].place(y = 10 , x = (i+1)*120)
	
#Data Baris
baris = [0 for x in range(5)]
for i in range(5):
	brs[i] = StringVar()
	baris[i] = Entry(window, width = 8, textvariable = brs[i])
	baris[i].place(x = 30, y = (i+0.6)* 115)
	
def UploadEE():
	t="u%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,."%(klm[0].get(),klm[1].get(),klm[2].get(),klm[3].get(),baris[0].get(),brs[1].get(),brs[2].get(),brs[3].get(),brs[4].get(),"0",offsetX.get(), offsetY.get())
	print(t)
	t2 = "U%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,."%(rakSodok[0][0].get(),rakSodok[0][1].get(),rakSodok[0][2].get(),rakSodok[0][3].get(),rakSodok[1][0].get(),rakSodok[1][1].get(),rakSodok[1][2].get(),rakSodok[1][3].get(),rakSodok[2][0].get(),rakSodok[2][1].get(),rakSodok[2][2].get(),rakSodok[2][3].get(),rakSodok[3][0].get(),rakSodok[3][1].get(),rakSodok[3][2].get(),rakSodok[3][3].get(),rakSodok[4][0].get(),rakSodok[4][1].get(),rakSodok[4][2].get(),rakSodok[4][3].get(),initSodok.get())
	print(t2)
	lgc.ser.write(str.encode(t))
	lgc.ser.write(str.encode(t2))

def LoadEE():
	a = "l"
	lgc.ser.write(str.encode(a))
	print(a)
	


def tick():
	global buff
	global ser
	while True:
		c = lgc.ser.read()	
				
		if len(c)==0  :
			break
		d= ord(c)
		if d==13:
			buff=buff
		elif d == 10:
			print(buff)
			parsing(buff)
			buff=""
		else:
			buff= buff + "%c"%d
			
	window.after(100,tick)

#parsing
def parsing(d):
	nilai = 0
	nilai = d.split(',')
	if(nilai[0] == 's'):
		for i in range(4):
			klm[i].set (nilai[i+1])
		for j in range(5):
			brs[j].set(nilai[j+5])
		offsetX.set(nilai[11])
		offsetY.set(nilai[12])
	if(nilai[0] == 'S'):
		print(nilai)
		initSodok.set(nilai[21])
		for i in range(20):
			j = i%4
			k = int(i/4)
			rakSodok[k][j].set(nilai[i+1])
				
#CSV
def UploadBackup():	
	print("oke")
	with open('EEsetting.csv', 'w') as csvFile:
		writer = csv.writer(csvFile)
		for i in range(4):
			row=['kolom%d'%i,klm[i].get()]
			writer.writerow(row)
		for j in range(6):
			row=['baris%d'%j,brs[j].get()]
			writer.writerow(row)
		for i in range(4):
			for j in range(5):
				x = i*3 + j
				row=['sodok %d'%x, rakSodok[j][k]]
				writer.writerow(row)
	csvFile.close()

#Data Lokasi
rak = [[0 for x in range(4)] for x in range(5)]
offsetSodok = [[0 for x in range(4)] for x in range(5)]
rakSodok = [[0 for x in range(4)] for x in range(5)]
for j in range(5):
	for k in range(4):
		rakSodok[j][k] = StringVar()
		rak[j][k] = Button(window, text = "%c%c"%(j+65,k+49), width = 5 , height = 3)
		rak[j][k].value = "%c%c"%(j+65,k+49)
		mod = mode.get()
		rak[j][k].config(command = lambda a=rak[j][k].value: tes(a))
		rak[j][k].place(x = (k+1)*120, y = (j+0.5)*110)
		offsetSodok[j][k] = Entry(window, width = 8, textvariable = rakSodok[j][k])
		offsetSodok[j][k].place(x = (k+1)*120, y = ((j+0.5)*110)+65)

#Tombol
tombolLoadEE = Button(window, text = "Load EE", width = 15, height= 2, command = LoadEE)
tombolLoadEE.place(x = xKanan+10, y = 100)

tombolUploadEE = Button(window, text = "Upload EE", width = 15, height= 2, command = UploadEE)
tombolUploadEE.place(x = xKanan+180, y = 100)

tombolUploadEEBackup = Button(window, text = "Load Backup EE", width = 15, height= 2)
tombolUploadEEBackup.place(x = xKanan+10, y = 175)

tombolUploadEEBackup = Button(window, text = "Simpan Backup EE", width = 15, height= 2, command = UploadBackup)
tombolUploadEEBackup.place(x = xKanan+180, y = 175)

tombolMotorHome = Button(window, text = "Motor Home", width = 15, height= 2, command = lgc.motorHome)
tombolMotorHome.place(x = xKanan+10, y = 250)

tombolMotorSleep = Button(window, text = "Motor Sleep", width = 15, height= 2, command = lgc.motorSleep)
tombolMotorSleep.place(x = xKanan+180, y = 250)

tombolMotorWake = Button(window, text = "Motor Wake", width = 15, height= 2, command = lgc.motorWake)
tombolMotorWake.place(x = xKanan+10, y = 325)

tombolMotorWake = Button(window, text = "Cek Sensor", width = 15, height= 2, command = lgc.cekSensor)
tombolMotorWake.place(x = xKanan+180, y = 325)

def koneksi():
	lgc.connectSerial()
	window.after(100,tick)

tombolConnect = Button(window, text = "Connect", width = 15, height= 2, command = koneksi)
tombolConnect.place(x = 30, y = sizeWindowY-120)

tombolEnterMode = Button(window, text = "Enter Mode", width = 15, height= 2, command = lgc.enterMode)
tombolEnterMode.place(x = 250, y = sizeWindowY-120)

tombolExitMode = Button(window, text = "Exit Mode", width = 15, height= 2, command = lgc.exitMode)
tombolExitMode.place(x = 400, y = sizeWindowY-120)

sodokManual = StringVar() 
def sodokMaju():
	a = "p%sa"%(sodokManual.get())
	print(a)
	lgc.ser.write(str.encode(a))
	

def sodokMundur():
	a = "pb"
	print(a)
	lgc.ser.write(str.encode(a))
	

#offset & initsodok
offsetX = StringVar()
offsetY = StringVar()
tombolOffsetX = Entry(window, width = "8", textvariable = offsetX )
tombolOffsetX.place(x = xKanan+10, y = 400)
tombolOffsetY = Entry(window, width = "8", textvariable = offsetY )
tombolOffsetY.place(x = xKanan+90, y = 400)

initSodok = StringVar()
tombolInitSodok = Entry(window, width = "8", textvariable = initSodok )
tombolInitSodok.place(x = xKanan+10, y = 450)
entrySodok = Entry(window, width = "18", textvariable = sodokManual )
entrySodok.place(x = xKanan+100, y = sizeWindowY-190)
tombolSodok = Button(window, text = "Sodok maju", width = 15, height= 2, command = sodokMaju)
tombolSodok.place(x = xKanan+10, y = sizeWindowY-120)
tombolSodok = Button(window, text = "Sodok mundur", width = 15, height= 2, command = sodokMundur)
tombolSodok.place(x = xKanan+200, y = sizeWindowY-120)

window.mainloop()
