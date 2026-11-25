def arquivo():
 sequencia = []
 with open("sequence.fasta", "r") as file:
  for linha in file:
   linha = linha.strip()
   if not linha or linha.startswith('>'):
    continue
   sequencia.append(linha)
  return "".join(sequencia)
tabela = str.maketrans("ATCG","TAGC")
lista_r = []
k = 0
inter = ""
while k <= 4:
 k = int(input("Digite o tamanho do pescoço do grampo (Precisa ser um valor maior que 4) : "))
 if k <= 4:
  k = int(input("Digite um valor maior que 4 : "))
def funcao(abc,lista):
 for j in range(len(abc)):
  for i in range(3,k):
   if 12 < 2 * k + i > 20 or  j + (2*k + i)  >= len(abc):
    break
   if abc[j:j+k] == abc[j + k + i : j + (2*k + i)].translate(tabela)[::-1] and (k%2 != 0 or abc[j+k:j+k+i] != abc[j+k:j+k+i].translate(tabela)[::-1]):
    lista.append(abc[j: j + (2 * k + i) ])
 return  lista
abc_dna = arquivo()
lista_r = funcao(abc_dna,lista_r)
print("Lista de Grampos: ")
for i in lista_r:
 if abc_dna.find(i) > abc_dna.find(inter) + len(inter) or inter == "":
  print(i," Posição inicial :",abc_dna.find(i) + 1 , ", Posição final :" , abc_dna.find(i) + len(i), ", Tamanho do Pescoço :" , k )
 inter = i
print("Numero de Grampos: ",len(lista_r))



