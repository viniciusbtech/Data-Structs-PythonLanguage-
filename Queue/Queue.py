class Fila:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens)==0
    
    def enqueue(self,valor):
        self.itens.append(valor)  #sempre coloca no final da lista 

    def dequeue(self):
        if self.is_empty():
            print("fila vazia")
            return None
        return self.itens.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None 
        return self.itens[0]
    
    def print_Queue(self):
        print(self.itens)
    



# Teste
f = Fila()
f.print_Queue()
f.enqueue(10)
f.print_Queue()
f.enqueue(20)
f.print_Queue()
f.enqueue(30)
f.print_Queue()
f.enqueue(40)
f.print_Queue()

print(f.dequeue()) 
f.print_Queue()
print(f.dequeue()) 
f.print_Queue()