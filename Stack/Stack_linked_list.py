
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    
    def is_empty(self):
        return self.top is None
    
    def push(self,valor):
        new=Node(valor)
        new.next=self.top
        self.top=new
    
    def pop(self):
        if self.is_empty():
            print("Stack empty")
            return None
        aux=self.top.data
        self.top=self.top.next
        return aux
    
    def peek(self):
        if not self.is_empty():
            return self.top.data
        
    def print_stack(self):
        atual=self.top
        print("Top",end=" -> ")
        while atual:
            print(atual.data, end=" ->")
            atual=atual.next
        print("None")

    

# Teste


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


  


      
    
