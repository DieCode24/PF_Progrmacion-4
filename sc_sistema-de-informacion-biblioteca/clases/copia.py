class Copia:
    def __init__(self, isbn, id, estado):
        self.isbn = isbn
        self.id = id
        self.estado = estado
    
    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, value):
        self._isbn = value
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
        
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, value):
        self._estado = value
        