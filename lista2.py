'''
Exercícios sobre os comandos de condição em python
'''

def exemploSe():
    idade = 18
    if idade == 18:  # Se idade for igual a 18
        print('Possui 18 anos')

def exemploSeSenao():
    idade = 60
    if idade >= 18 and idade < 60:   # Se idade for maior ou igual a 18 e menor que 60
        print('Maior de idade')
    elif idade >= 60: # Senão se a idade for maior ou igual a 60
        print('Melhor idade')
    else:             # Senão
        print('Menor de idade')

def exemploSeSenao():
    idade = 60
    if idade >=60:   # Se idade for maior ou igual a 60 
        print('Melhor idade')
    elif idade >= 18: # Senão se a idade for maior ou igual a 18
        print('Maior de idade')
    else:             # Senão
        print('Menor de idade')

def exemploCaso():      # serve apenas para valores conhecidos (poucos) e exatos.
    estado_civil = 's'
    match(estado_civil):
        case 's':
            print('Solteiro')
        case 'c':
            print('Casado')
        case _:
            print('Valor padrão ou desconhecido!')

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q1():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    soma = num1 + num2
    if soma > 10:
    print("Resultado da soma:" soma )
    
#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q2():
    a = int(input("Digite o primeiro valor"))
    b = int(input("Digite o segundo valor"))
    soma = a + b 
    if soma > 20 
    resultado = soma + 8
    else:
        resultado = soma - 5 
        print (resultado:"; resultado")     

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q03():
    numero = int(input("Digite um número: "))
if numero % 3 == 0:
    print("É múltiplo de 3")
else:
    print("Não é múltiplo de 3")

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q04():
    numero = int(input("Digite um número: "))
if numero % 5 == 0:
    print("É divisível por 5")
else:
    print("Não é divisível por 5")

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q05():
    numero = int(input("Digite um número: "))
if numero % 3 == 0 and numero % 7 == 0:
    print("É divisível por 3 e por 7")
else:
    print("Não é divisível por 3 e por 7")

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def q06():
    salario = float(input("Digite o salário bruto: "))
prestacao = float(input("Digite o valor da prestação: "))
limite = salario * 0.30
if prestacao <= limite:
    print("Empréstimo pode ser concedido")
else:
    print("Empréstimo não pode ser concedido")

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q07():
    numero = float(input("Digite um número: "))
if 20 <= numero <= 50:
    print("O número está entre 20 e 50")
else:
    print("O número não está entre 20 e 50")

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q08():
    numero = float(input("Digite um número: "))
if numero > 20:
    print("Maior do que 20")
elif numero == 20:
    print("Igual a 20")
else:
    print("Menor do que 20")

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def q09():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
if ano_nascimento > ano_atual:
    print("Ano de nascimento inválido")
elif ano_nascimento <= 0:
    print("Ano de nascimento inválido")
else:
    idade = ano_atual - ano_nascimento
    print("Idade:", idade)

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():
    a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
numeros = [a, b, c]
numeros.sort()
print("Números em ordem crescente:", numeros)

#11. Faça um programa que leia 3 números e imprima o maior deles.
def q11():
    n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
maior = n1
if n2 > maior:
    maior = n2

if n3 > maior:
    maior = n3
print("O maior número é:", maior)

#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos
def q12():
    idade = int(input("Digite a idade: "))
if idade >= 65:
    print("Maior de 65 anos")
elif idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).
def q13():
    def q13():
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a nota da prova 1: "))
    n2 = float(input("Digite a nota da prova 2: "))
    media = (n1 + n2) / 2
    print("Nome:", nome)
    print("Nota 1:", n1)
    print("Nota 2:", n2)
    print("Média:", media)
    if media >= 7:
        print("Aprovado")
    elif media < 3:
        print("Reprovado")
    else:
        print("Em Prova Final")

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%
def q14():
    salario = float(input("Digite o salário: "))
if salario <= 600:
    desconto = 0
elif salario <= 1200:
    desconto = salario * 0.20
elif salario <= 2000:
    desconto = salario * 0.25
else:
    desconto = salario * 0.30
print("Salário:", salario)
print("Desconto do INSS:", desconto)
print("Salário com desconto:", salario - desconto)

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.
def q15():
valor = float(input("Digite o valor do produto: "))
if valor < 20:
    venda = valor * 1.45
else:
    venda = valor * 1.30
print("Valor de compra:", valor)
print("Valor de venda:", venda)

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos
def q16():
    idade = int(input("Digite a idade do nadador: "))
if 5 <= idade <= 7:
    print("Categoria: Infantil A")
elif 8 <= idade <= 10:
    print("Categoria: Infantil B")
elif 11 <= idade <= 13:
    print("Categoria: Juvenil A")
elif 14 <= idade <= 17:
    print("Categoria: Juvenil B")
elif idade >= 18:
    print("Categoria: Sênior")
else:
    print("Idade fora das categorias (menor que 5 anos)")

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00
def q17():
    nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
if idade <= 10:
    valor = 30.00
elif idade <= 29:
    valor = 60.00
elif idade <= 45:
    valor = 120.00
elif idade <= 59:
    valor = 150.00
elif idade <= 65:
    valor = 250.00
else:
    valor = 400.00
print(f"Nome: {nome}")
print(f"Valor a pagar: R${valor:.2f}")

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.
def q18():
    numero = int(input("Digite um número de 1 a 12: "))
if numero == 1:
    mes = "Janeiro"
elif numero == 2:
    mes = "Fevereiro"
elif numero == 3:
    mes = "Março"
elif numero == 4:
    mes = "Abril"
elif numero == 5:
    mes = "Maio"
elif numero == 6:
    mes = "Junho"
elif numero == 7:
    mes = "Julho"
elif numero == 8:
    mes = "Agosto"
elif numero == 9:
    mes = "Setembro"
elif numero == 10:
    mes = "Outubro"
elif numero == 11:
    mes = "Novembro"
elif numero == 12:
    mes = "Dezembro"
else:
    mes = None

if mes:
    print(f"Mês: {mes}")
else:
    print("Não existe mês com esse número.")

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".
def q19():
    # Leitura dos pontos
p1 = int(input("Digite os pontos do jogador 1: "))
p2 = int(input("Digite os pontos do jogador 2: "))
p3 = int(input("Digite os pontos do jogador 3: "))

pontos = [p1, p2, p3]

pontos.sort(reverse=True)
print("Pontuações em ordem decrescente:", pontos)
soma = sum(pontos)
if soma > 100:
    media = soma / 3
    print(f"Média da equipe: {media:.2f}")
else:
    print("Equipe desclassificada")

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio
def q20():
    saldo_medio = float(input("Digite o saldo médio do cliente: "))
if 0 <= saldo_medio <= 500:
    credito = 0
elif saldo_medio <= 1000:
    credito = saldo_medio * 0.30
elif saldo_medio <= 3000:
    credito = saldo_medio * 0.40
else:
    credito = saldo_medio * 0.50
print(f"Saldo médio: R${saldo_medio:.2f}")
print(f"Valor do crédito: R${credito:.2f}")

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:
def q21():
    livro = input("Digite o nome do livro: ")
tipo = input("Digite o tipo de usuário (professor/aluno): ").lower()

if tipo == "professor":
    dias = 10
elif tipo == "aluno":
    dias = 3
else:
    dias = 0
print("\n--- Recibo ---")
print(f"Nome do livro: {livro}")
print(f"Tipo de usuário: {tipo}")
if dias > 0:
    print(f"Total de dias: {dias}")
else:
    print("Tipo de usuário inválido")

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.
def q22():
    km = float(input("Digite o percurso em km: "))
tipo = input("Digite o tipo do carro (A, B ou C): ").upper()
if tipo == "A":
    consumo = km / 12
elif tipo == "B":
    consumo = km / 9
elif tipo == "C":
    consumo = km / 8
else:
    consumo = None
if consumo is not None:
    print(f"Consumo estimado: {consumo:.2f} litros")
else:
    print("Tipo de carro inválido")

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos

try:
    opcao = int(input('Digite o número da questão: '))
    if opcao < 1 or opcao > 25:
        raise Exception('Questão inválida, valores devem estar entre 1 e 25')
    eval(f'q{opcao}()')
except ValueError:
    print('O número da questão deve ser numérico (inteiro)!')
except Exception as e:
    print(e)