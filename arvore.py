 #-*- coding: utf-8 -*-
import re
from qualis import Qualis
from  no import Node
class Arvore_exception(Exception):
        def __init__(self,msg):
                super().__init__(msg)
class Arvore:
    def __init__(self,raiz = None):
        self._raiz = raiz
    @property
    def raiz(self):
        return self._raiz
    def esta_vasia(self):
        if self._raiz==None:
            return self._raiz
    def add_raiz(self,dado):
    #arvore vasia
        if self._raiz==None: 
            self._raiz = Node(dado)
        else:
            return self._add_raiz(dado,self._raiz)
    def _add_raiz(self,dado,node):
            # dado e menor que o dado da raiz e tem filho esquedo
            
            if dado.issn < node.dado.issn:
                if node.filho_es!=None:
                    return self._add_raiz(dado,node.filho_es)
                else:
                    no=Node(dado)
                    node.filho_es=no
            else:
                #dado e maior que dado da  raiz e tem filho dir
                if node.filho_dir!=None:
                    return self._add_raiz(dado,node.filho_dir)
                else:
                    no=Node(dado)
                    node.filho_dir=no
            
                
                
    def busca(self,chave):
        if self._raiz!=None:
            return self._busca_chave(chave,self._raiz)
        else:
            return None

    def _busca_chave(self,chave,node):
        if chave == node.dado.issn:
            return node
        elif chave < node.dado.issn and node.filho_es!=None:
            return self._busca_chave(chave,node.filho_es)
        elif chave > node.dado.issn and node.filho_dir!=None:
            return self._busca_chave(chave,node.filho_dir)
        
        else:
            return  None
        
    def modifica(self,node):
        #modifica dados do nó se chave for a mesma  
        if self.busca(node.issn)!=None:
            aux = self.busca(node.issn)
            aux.dado.titulo = node.titulo
            aux.dado.estrato = node.estrato
        return aux
    def menor(self):
        if self._raiz == None:
            return None
        else:
            return self._menor(self._raiz)
    def _menor(self,node):
        aux=node
        
        while aux.filho_es!=None:
            aux=aux.filho_es
        return aux
    def rmv_Arvore(self):
        self._raiz = None
        
    def rmv(self,chave):
        return self._rmv(chave,self._raiz)
    def _rmv(self,chave,node):
        if node is None:
            # Se desceu até um ramo nulo, não há nada a fazer
            return node
        
        if chave < node.dado.issn:
            # Se o valor for menor, desce à esquerda
            node._filho_es = self._rmv(chave,node.filho_es)
    
        elif chave > node.dado.issn:
            # Se o valor for maior, desce à direita
            node._filho_dir = self._rmv(chave,node.filho_dir)
    
        else:
            # Se não for nem menor, nem maior, encontramos! Vamos remover...
            if node._filho_es is None:
                #filho esquedo == None
                aux = node.filho_dir
                node=None
                return aux
            elif node._filho_dir is None:
                #filho direito  == None
                aux = node.filho_es
                node=None
                return aux
            # Substituto é o sucessor do valor a ser removido
            aux = self._menor(node.filho_dir)
            # Ao invés de trocar a posição dos nós, troca o valor
            node._dado = aux._dado
            # Depois, remove o substituto da subárvore à direita
            node._filho_dir = self._rmv(aux._dado,node._filho_dir)
        return node
    def cont(self):
        return self._cont(self._raiz) 
    def _cont(self,node):
        if node==None:
            return 0
        else:
            return 1+ self._cont(node.filho_es)+self._cont(node.filho_dir)
    def pres_ord(self):
        return self._pres(self._raiz)
    def in_ord(self):
        return self._in(self._raiz)
    def pros_ord(self):
        return self._pros(self._raiz)
    
    def _pres(self,node):
        if node!=None:
            print(node.dado)
            self._pres(node.filho_es)
            self._pres(node.filho_dir)
    def _in(self,node):
        if node!=None:
            self._in(node.filho_es)
            print(node.dado)
            self._in(node.filho_dir)
    def _pros(self,node):
        if node!=None:
            self._pros(node.filho_es)
            self._pros(node.filho_dir)
            print(node.dado)

    def altura(self):
        return self._altura(self._raiz)
    def _altura(self,node):
        if node == None:
            return 0
        else:
            if self._altura(node.filho_es) > self._altura(node.filho_dir):
                return 1 + self._altura(node.filho_es)
            else:
                return 1 + self._altura(node.filho_dir)
    def imprime(self):
        return self._imprime(self._raiz)

    def _imprime(self,node):
        
        if node!=None:
            print(node.dado)
            self._imprime(node.filho_es)
            self._imprime(node.filho_dir)
            
    def __str__(self):
        return '%s' %(self._raiz)
'''
q=Qualis()
q.issn='0000-0001'
q.estrato='A1'
q.titulo='rodrigo'
a=Qualis()
a.issn='0000-0002'
a.estrato='A1'
a.titulo='lukas'
b=Qualis()
b.issn='0000-0003'
b.estrato='A1'
b.titulo='pincel'
c=Arvore()
c.add_raiz(b)
c.add_raiz(a)
c.add_raiz(q)
e=Qualis()
e.issn='0000-0002'
e.estrato='D1'
e.titulo='aux'
c.imprime()
print(c.modifica(e))
c.imprime()
'''
