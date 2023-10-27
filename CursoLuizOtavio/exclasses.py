# Criando um sistema de cliente com nome plano e email, tentando assistir um filme e verificando se seu 
# plano é o necessario para assistir um filme
class Cliente:

    def __init__(self, nome, plano, email):
        self.email = email
        self.nome = nome
        self.plano = plano
        self.lista_plano = ['basic', 'premium']
        if plano in self.lista_plano :
            self.plano = plano
        else:
            raise Exception('PLANO INVÁLIDO')
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano
            print('Seu plano foi modificado')
        else:
            print('Digite um plano valido')

    def ver_film(self, filme , plano_filme):
        self.filme = filme
        if self.plano == plano_filme :
            print(f'Acesso liberado para {filme}')
        elif self.plano == 'premium':
            print('Acesso liberado a todos os filmes')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print("Faça um upgrade no seu plano para acessar o filme.")

    def saudacao(self):
        print(f"Olá,{self.nome}! Seja bem-vindo(a).\nPlano: {self.plano}\nRegistrado no email : {self.email} ")

# Criando um objeto da classe Pessoa
pessoa1 = Cliente('mateus', 'basic', 'mateus@email')
pessoa1.saudacao()
pessoa1.ver_film('Harry Potter', 'premium')
#upgrade filme
pessoa1.mudar_plano('premium')
pessoa1.ver_film('Harry Potter', 'premium')



