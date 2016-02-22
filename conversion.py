#! /bin/python
# -*- coding: utf-8 -*-

import struct

def convertirBin_Dec(numero):
	return numero

def convertirDec_Bin(numero):
	numConv=[]
	if numero > 0:
		numConv.append("0") 
	else:
		numConv.append("1")
	signo = numero.split("-")
	if len(signo) > 1:#tiene signo
		num = signo[1].split(".")
	else:
		num = signo[0].split(".")
	numeroBinario = bin(int(num[0]))
	numeroBinario = numeroBinario[2:]
	decimal = num[1]
	print decimal
	print numeroBinario
	return numConv
	
def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))

def main():
	x = True
	while x:
		print("Selecciona una opción: ")
		opcion = raw_input("1. Decimal a binario \n2. Binario a Decimal"+
			"\nPresione otra tecla para salir.\n")
		if opcion == "1":
			try:
				numflot = float(raw_input("Escribe el numero: "))
			except :
				print "Error"
				break
			print convertirDec_Bin(str(numflot))
		elif opcion == "2":
			try:
				numBin = raw_input("Escribe el numero binario: ")
			except:
				print "Error"
				break
			print convertirBin_Dec(numBin)
		else:
			x = False

main()
