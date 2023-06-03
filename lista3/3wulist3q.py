
arquivo = open("frase.txt", "a+")
novo_texto = "\nchove chuva, chove sem parar, chove chove..."
arquivo.write(novo_texto)
arquivo.seek(0)
novo_conteudo = arquivo.read()
print("Novo conteúdo:")
print(novo_conteudo)
arquivo.close()
