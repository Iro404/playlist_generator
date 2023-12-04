"""
def controlador():
    op = True
    print('Bem vindo ao Generic Playlist Generator! Por favor, escreva qual operação você quer realizar:')
    while op:
        op = int(input('1: Criar Playlist\n2: Imprimir lista deReprodução\n3: Adicionar Música\n4: Remover Música\n5: Adicionar Música no Início\n6: Remover música no início\n7: Adicionar Música na posição escolhida\n8: Remover música na posição escolhida\n9: Remover música por nome\n'))
        if op == 1:
            lista = Playlist()
            print('Playlist Criada!\n\n')
            
        elif op == 2:
            lista.queue()
            op = int(input('Você deseja continuar usando o programa?(S/N)\n'))
            if op
            
        elif op == 3:
            pass
        
        elif op == 4:
            pass
        
        elif op == 5:
            pass
        
        elif op == 6:
            pass
        
        elif op == 7:
            pass
        
        elif op == 8:
            pass
        
        elif op == 9:
            pass
"""

class Noh:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        self.ant = None

#####################################################
class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_end(self, data):
        novo_noh = Noh(data)
        if self.head:
            print(f'Adicionando {novo_noh.valor.name} ao fim da playlist...')
            self.tail.prox = novo_noh
            novo_noh.ant = self.tail
            self.tail = novo_noh
        else:
            self.head = novo_noh
            self.tail = novo_noh
            return
        
    def del_end(self):
        if self.head: #Se existir músicas na playlist
            if self.head.prox: #Se houver uma próxima música depois da primeira
                print(f'Removendo "{self.tail.valor.name}" - {self.tail.valor.artists} da Playlist...\n')
                self.tail.ant.prox = None
                self.tail = self.tail.ant
            else:
                self.head = None
                self.tail = None
        else:
            print('Não existem músicas na fila de reprodução!')
            
    def add_in(self, data):
        novo_noh = Noh(data)
        print(f'Adicionando "{novo_noh.valor.name}" no início...\n')
        novo_noh.prox = self.head
        if self.head:
            self.head.ant = novo_noh
        else:
            self.tail = novo_noh
        self.head = novo_noh
        
    def del_in(self):
        if self.head:
            if self.head.prox:
                self.head.prox.ant = None
            else:
                self.tail = None
            print(f'Removendo "{self.head.valor.name}" - {self.head.valor.artists} da playlist...\n')
            self.head = self.head.prox
        else:
            print('Não existem músicas na fila de reprodução!')
            
    def add_mid(self, position, data):
        if position == 0:
            self.add_in(data)
            return
        novo_noh = Noh(data)
        atual = self.head
        for i in range(position - 1):
            if atual is None:
                print('Valor inválido! Por favor, indique uma posição diferente!')
                return
            atual = atual.prox
        print(f'Adicionando "{novo_noh.valor.name}" depois de "{atual.valor.name}"...\n')
        novo_noh.prox = atual.prox
        novo_noh.ant = atual
        if atual.prox:
            atual.prox.ant = novo_noh
        else:
            self.tail = novo_noh
        atual.prox = novo_noh
        
    def del_mid(self, position):
        if position == 0:
            self.del_in()
            return
        else:
            atual = self.head
            for i in range(position - 1):
                if atual is None:
                    print('Valor inválido! Por favor, indique uma posição diferente!\n')
                    return
                atual = atual.prox
            print(f'Deletando "{atual.valor.name}" - {atual.valor.artists}\n')
            if atual.ant:
                atual.ant.prox = atual.prox
            if atual.prox:
                atual.prox.ant = atual.ant
            else:
                self.tail = atual.ant
              
    def del_mus(self, music):  
        if self.head:
            if self.head.valor.name == music:
                self.del_in()
                return
            atual = self.head
            achou = False
            while not achou:
                if music == atual.valor.name:
                    achou = True
                    print(f'Deletando "{atual.valor.name}" - {atual.valor.artists}\n')
                    if atual.ant:
                        atual.ant.prox = atual.prox
                    if atual.prox:
                        atual.prox.ant = atual.ant
                    else:
                        self.tail = atual.ant
                else:
                    if atual.prox:
                        atual = atual.prox
                    else:
                        print('Música não encontrada na playlist!')
                        break
        else:
            print('Não existem músicas a serem deletadas!')

    def queue(self):
        if self.head:
            print('Lista de músicas:')
            atual = self.head
            while atual:
                print(f'"{atual.valor.name}" - {atual.valor.artists}')
                atual = atual.prox
        else:
            print('Não existem músicas na fila de reprodução!\n')
               
######################################################################
class Music: #talvez, pra ser mais rápido adicionar as músicas, eu deva criar um arquivo com várias músicas 
    def __init__(self, name, artists, genre, album, order):
        self.name = name
        self.artists = artists
        self.genre = genre
        self.album = album
        self.order = order
###############################################################################

kendrickl_blood = Music('BLOOD.','Kendrick Lamar', 'Rap', 'DAMN.',1)
kendrickl_dna = Music('DNA.','Kendrick Lamar','Rap','DAMN.', 2)
kendrickl_yah = Music('YAH.','Kendrick Lamar','Rap','DAMN.', 3)
kendrickl_element = Music('ELEMENT.','Kendrick Lamar','Rap','DAMN.', 4)
kendrickl_feel = Music('FEEL.','Kendrick Lamar','Rap','DAMN.', 5)
kendrickl_loyalty = Music('LOYALTY. FEAT. RIHANNA.','Kendrick Lamar, Rihanna','Rap','DAMN.', 6)
kendrickl_pride = Music('PRIDE.','Kendrick Lamar','Rap','DAMN.', 7)
kendrickl_humble = Music('HUMBLE.','Kendrick Lamar','Rap','DAMN.',8)
kendrickl_lust = Music('LUST.','Kendrick Lamar','Rap','DAMN.', 9)
kendrickl_love = Music('LOVE. FEAT. ZACARI.','Kendrick Lamar, Zacari','Rap','DAMN.', 10)
kendrickl_xxx = Music('XXX. FEAT. U2.','Kendrick Lamar, U2','Rap','DAMN.', 11)
kendrickl_fear = Music('FEAR.','Kendrick Lamar','Rap','DAMN.', 12)
kendrickl_god = Music('GOD.','Kendrick Lamar','Rap','DAMN.', 13)
kendrickl_duckworth = Music('DUCKWORTH.','Kendrick Lamar','Rap','DAMN.', 14)

"""
musics = Playlist()
musics.add_end(kendrickl_humble)
musics.add_end(kendrickl_blood)
musics.add_end(kendrickl_fear)
musics.add_end(kendrickl_god)
musics.add_end(kendrickl_duckworth)
print('##PLAYLIST INICIAL##')
musics.queue()
print('\n\n##REMOVENDO MÚSICA NO FIM##')
musics.del_end()
musics.queue()
print('\n\n##ADICIONANDO MÚSICA NO FIM##')
musics.add_end(kendrickl_pride)
musics.queue()
print('\n\n##ADICIONANDO NO INÍCIO##')
musics.add_in(kendrickl_blood)
musics.queue()
print('\n\n##REMOVENDO MÚSICA NO INÍCIO##')
musics.del_in()
musics.queue()
print('\n\n##ADICIONANDO NO MEIO##')
musics.add_mid(3, kendrickl_feel)
musics.queue()
print('\n\n##FORÇANDO ERRO DE VALOR INVÁLIDO##')
musics.add_mid(10, kendrickl_xxx)
print('\n\n##DELETANDO NO MEIO##')
musics.del_mid(4)
musics.queue()
print('\n\n##REMOVENDO MÚSICA ESPECÍFICA##')
musics.del_mus(str(input('Escreva o nome da música que você deseja remover:\n')))
"""
#controlador()
