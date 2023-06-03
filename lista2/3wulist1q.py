
arquivo = open("frase.txt", "w")

frase = "chove chuva"
arquivo.write(frase)

arquivo.close()

arquivo = open("frase.txt", "r")
frase_lida = arquivo.read()
print(frase_lida)

arquivo.close()
