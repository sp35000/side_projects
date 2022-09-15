#!/usr/bin/python
import sys
trancePath="/home/yzmu/myCloud/ckrops/intra/trance/"
outputPath="/home/yzmu/tranceout/"
yearFile=(sys.argv[1])
nomeArqEntrada = trancePath+yearFile+".html"
arqEntrada = open(nomeArqEntrada,'r')
nameCurrentWriteFile="";
for line in arqEntrada:
#0....+....1....+....2....+....3....+....4....+....5....+....6....+....
#---------------------------------------------------------- dd/mm/yyyy
	verifLine=line[0:10]
	if (verifLine == "----------" and yearFile[1:3] == line[67:69]):
		flagNewText=True
		if (nameCurrentWriteFile <> ""):
			arqSaida.close()
		nameCurrentWriteFile=outputPath+yearFile+"-"+line[65:69]+line[62:64]+line[59:61]+".html"
		arqSaida = open(nameCurrentWriteFile,'w')
		arqSaida.write(line)
		print(flagNewText,nameCurrentWriteFile)
	else:
		flagNewText=False
		if (nameCurrentWriteFile <> ""):
			arqSaida.write(line)
arqEntrada.close()
