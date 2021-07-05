import re
class Qualis:
      def __init__(self):
            self._issn=None
            self._titulo=None
            self._estrato=None
      @property
      def issn(self):
            return self._issn
      @issn.setter
      def issn(self,novo_issn):
            self._issn=novo_issn 
      @property
      def titulo(self):
            return self._titulo
      @titulo.setter
      def titulo(self,novo_titulo):
            self._titulo=novo_titulo
      @property
      def estrato(self):
            return self._estrato
      @estrato.setter
      def estrato(self,novo_estrato):
            self._estrato=novo_estrato
      def __gt__(self,outro): 
            if isinstance (outro, Qualis): 
                  return outro.issn > self.issn
      else: 
            return False 
      def __lt__(self,outro): 
            if isinstance (outro, Qualis): 
                  return outro.issn < self.issn
            else: 
                  return False
      def __eq__(self, outro): 
            if isinstance (outro,Qualis):
                  return outro.issn == self._issn
            else: 
            return False
      def __str__(self):
            return '%s ; %s ;%s' %(self._issn,self._titulo,self._estrato)



