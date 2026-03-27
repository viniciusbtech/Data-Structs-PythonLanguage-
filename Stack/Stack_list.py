class Stack:
    def __init__(self):
        self.itens = []
    
    def push(self,valor):
        self.itens.append(valor)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        else:
            print("Pilha vazia")
    
    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
    
    def is_empty(self):
        return len(self.itens)  == 0
    
    def print_stack(self):
        print(self.itens)

p=Stack()
p.print_stack()

p.push(10)
p.print_stack()

p.push(20)
p.print_stack()

p.push(30)
p.print_stack()

p.push(40)
p.print_stack()

p.push(50)
p.print_stack()

p.push(60)


p.print_stack()

print("Topo:",p.peek())
print("Removido:",p.pop())
p.print_stack()
#LIFO LAST IN FIRST OUT 

print("Removido:",p.pop())
p.print_stack()

print("Removido:",p.pop())
p.print_stack()

print("Removido:",p.pop())
p.print_stack()


p.print_stack()

print("Removido:",p.pop())
p.print_stack()

print("Removido:",p.pop())
p.print_stack()

print("Esta vazio:",p.is_empty())
p.print_stack()
