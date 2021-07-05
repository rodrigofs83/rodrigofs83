#-*- coding: utf-8 -*-
import time
import re
import csv
from qualis import Qualis
from  no import Node
from  arvore import Arvore
class nenu_exception(Exception):
        def __init__(self,msg):
                super().__init__(msg)
        
class AbsentKeyException(Exception):
        def __init__(self,msg):
                super().__init__(msg)
class ChainingHashTable :
        def __init__(self,size=11):
                self._chaves=0
                self._size=size
                self._table=list(Arvore() for i in range(size))
        @property
        def chaves(self):
                return self._chaves
        def hash(self, key):
                ''' Função de transformação hash (hash modular). Retorna o índice    Correspondente ao slot mapeado para a chave “key” '''
                k=int(key)
                return k%self._size
        def put(self, key, data):
                ''' Insere na tabela hash a chave key e seu dado correspondente (data) '''
                slot = self.hash(key)
                print(f'key {key} mapeada ao slot {slot}')
                if self._table[slot].busca(data)!=None:#verifica duplicidade não ta funcionado
                        self._table[slot].modifica(data)
                self._table[slot].add_raiz(data)
                self._chaves+= 1
        def get(self,key,data):
                ''' Recupera da tabela hash o dado correspondente à chave “key” '''
                slot = self.hash(key)
                if self._table[slot].busca(data)!=None:
                        return self._table[slot].busca(data)
                        
                else:
                        None

        def remove(self, key,valor):
                '''Remove da tabela hash a chave “key” e retorna seu dado    correspondente '''
                try:
                        if( self.esta_vazia() ):
                                raise tabela_vazia(f'Não é possível Excluir periódico a tabela esta  vazia')
                        else:
                                slot = self.hash(key)
                                print(slot)
                                if self._table[slot].busca(valor)!=None:
                                        self._table[slot].rmv(valor)
                                        self._chaves-=1
                                else:
                                        return None
                except:
                        raise
        def esta_vazia(self):
                #verifica se a tabela esta vazia'''
                cont=0
                for i in range(len(self._table)):
                        if self._table[i].raiz==None:
                                cont+=1
                if cont==len(self._table):
                        return True
                else:
                        return False
        def esvazia(self):
                '''apaga todos os dados da tabela'''
                if self.esta_vazia() is True:
                        return (f'tabela esta vazia ')
                else:
                        for i in range(len(self._table)):
                                self._table[i].rmv_Arvore()
                                self._chaves=0
                        return (f'tabela foi formatada com susesso')
        def duplicidade(self,key,valor):
                '''verifica duplicidade'''
                slot = self.hash(key)
                print(slot)
                if self._table[slot].busca(valor)!=None:
                        print( self._table[slot].busca(valor))
                        return True
                else:
                        return False
                
        def colisao(self,table):
                '''contado de colisões'''
                contado=0
                for i in range(len(self._table)):
                        if self._table[i]!=None:
                                if self._table[i].cont() >1:
                                        contado += self._table[i].cont() -1
                                
                return contado
        def imprime_dados(self):
                '''imprime todos dados '''
                lis = []
                for i in range(len(self._table)):
                        if self._table[i]!=None:
                                lis.append(self._table[i].imprime())
                        print(lis)
        def __str__(self):
                ''' Representação interna da tabela hash sob a forma chave/valor, da    seguinte forma:    { chave: valor ; chave: valor; ...; chave: valor }'''
                return   '%s'  %(self._table[0].get_raiz())
def ImportCsV(texto,tabela):
        
        
        try:
                arq = open(texto,encoding='utf-8')
                texto = csv.reader(arq,delimiter=';')
                issn_invalidos  = []
                tempo=0
                inicio = time.time()
                for linha in texto:
                        qualis=Qualis()
                        qualis.issn = linha[0]
                        qualis.titulo = linha[1]
                        qualis.estrato = linha[2]
                        if Valida_issn(qualis.issn):
                                chave = Converte_int(qualis.issn) 
                                tabela.put(chave,qualis)
                                print(qualis)
                        else:
                                issn_invalidos.append(linha)
        
                fim = time.time()
                tempo = fim-inicio
                print(f'''
        ---------------- Estatísticas -------------------
                        qualis invalido = {len(issn_invalidos)}
                        chaves adicionadas  = {tabela.chaves}
                        colisões = {tabela.colisao(tabela)}
                        tempo = {tempo:.2f}seconds
        -------------------------------------------------''')
                arq.close()
        except FileNotFoundError:
                print( 'Esse arquivo ou diretorio não existe')      
        
                
        
def Converte_int(issn):
        chave = int(re.sub(r'-','',str(issn)))
        return chave
def Valida_issn(inss):
        #regex=^[0-9]{4}[-][0-9]{4}$
        if re.match(r'^[0-9]{4}[-][0-9]{4}$',str(inss)):
                return True
        else:
                return False        

def menu():
        while True:
                try:
                
                        tam = int(input('Digite tamanho da tabela de dispenção'))
                        assert tam >0 
                        tabela = ChainingHashTable(tam)
                        break

                except ValueError :
                        print(f'Digite um numero inteiro ')
                except AssertionError:
                        print(f'tamnho da tabela de dispenção não pode ser numero negativo ou 0 (zero )')
        entre=True
        while(entre):
                print('''
        --------Digite  Opçao-------------------
        [1] Importar arquivo Qualis CSV               
        [2] Adicionar manualmente um periódico 
        [3] Consultar um periódico                        
        [4] Excluir periódico                  
        [5] Eliminar todos os periódicos
        [6] Listar dados
        [7] colisões
        [0]  Sair                              
        ----------------------------------------
        ''')
                op=input('Digite a Opção :')
                if op=='1':
                        
                        ImportCsV('qualis-cc.csv',tabela)     
                elif op=='2':
                        issn = input('Digite ISSN ex(xxxx-xxxx): ')
                        valor=True
                        while valor:
                                if Valida_issn(issn):
                                        chave = Converte_int(issn)
                                        titulo = input('Digite TITULO')
                                        estrato = input('Digite ESTRATO')
                                        qualis=Qualis()
                                        qualis.issn = issn
                                        qualis.titulo = titulo
                                        qualis.estrato = estrato
                                        print(qualis)
                                        tabela.put(chave,qualis)
                                        arq=open('copia.csv','+a',newline='',encoding='utf-8')
                                        for linha in arq:
                                                texto=linha 
                                        texto = csv.writer(arq,delimiter=';')
                                        escrita = [qualis.issn,qualis.titulo,qualis.estrato]
                                        texto.writerow(escrita)
                                        arq.close()

                                        valor = False
                                        
                                else:
                                        issn = input('Digite ISSN Valido ex(xxxx-xxxx): ')
                        
                elif op=='3':
                        valor=True
                        issn=input('Digite o issn Ex(0000-0000): ')
                        
                        while valor:
                                if Valida_issn(issn):
                                        chave = Converte_int(issn)
                                        print(tabela.get(chave,issn))
                                        valor = False
                                else:
                                        issn = input('Digite ISSN Valido ex(xxxx-xxxx): ')
                                        
                        
                elif op=='4':
                        valor = True
                        issn = input('Digite ISSN ex(xxxx-xxxx): ')
                        while valor:
                                if Valida_issn(issn):
                                        chave = Converte_int(issn)
                                        tabela.remove(chave,issn)
                                        valor = False
                                else:
                                        issn = input('Digite ISSN Valido ex(xxxx-xxxx)')
                elif op=='5':
                        print(tabela.esvazia())
                elif op=='6':
                        tabela.imprime_dados()
                elif op=='7':
                        print('colisões = ',tabela.colisao(tabela))
                elif op=='0':
                        print('''
        --------------------Fim--------------------'
        ''')
                        entre=False
                else:
                        print('Digite uma Opção valida')
                        
                        
menu()
