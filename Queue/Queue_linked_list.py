class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Fila:
    def __init__(self):
        self.front=None #inicio
        self.rear=None #Ifim
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self,valor):
        new_node=Node(valor)

        if self.rear is None:
            self.front=self.rear=new_node
        else:
            self.rear.next=new_node 
            self.rear=new_node


    def dequeue(self):
        if self.is_empty():
            print("Fila vazia")
            return None 
        
        aux=self.front.data
        self.front=self.front.next

        if self.front is None:
            self.rear=None 

        return aux 
    
    def peek(self):
        if self.is_empty():
            return None
        return self.front.data
        


        
    
f = Fila()

f.enqueue(10)
f.enqueue(20)
f.enqueue(30)

print(f.dequeue())  # 10
print(f.peek())     # 20
print(f.dequeue())  # 20
print(f.dequeue())  # 30
print(f.dequeue())  # fila vazia
    





         
