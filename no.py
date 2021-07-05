from qualis import Qualis

class Node:
    def __init__(self,dado=None,filho_es=None,filho_dir=None):
        self._dado = dado
        self._filho_es = filho_es
        self._filho_dir = filho_dir
    @property
    def dado(self):
        return self._dado
    @dado.setter
    def dado(self,novo_dado):
        self._dado=novo_dado
    @property
    def filho_es(self):
        return self._filho_es
    @filho_es.setter
    def filho_es(self,novo_dado):
        if self._filho_es==None:
            self._filho_es=novo_dado
    @property     
    def filho_dir(self):
        return self._filho_dir        
    @filho_dir.setter
    def filho_dir(self,novo_dado):
        if self._filho_dir==None:
            self._filho_dir = novo_dado
    def __str__(self):
        return '%s' %(self._dado)





