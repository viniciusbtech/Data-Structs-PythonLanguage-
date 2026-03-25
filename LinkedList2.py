class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None 
    
    def imprimir(self):
        atual = self.head
        while atual:
            print(atual.data, end=" -> ")
            atual = atual.next
        print("None")

    
    def inserir_final(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
    
        aux=self.head 
        while(aux.next):
            aux=aux.next
        aux.next=new_node

    def invertert(self):
        if self.head is None:
            return
        
        aux=self.head
        aux2=None
        while(aux):
            aux2=aux.next
            aux2.next=aux
            












            

        
 #teste
lista = Linked_list()

lista.inserir_final(10)
lista.inserir_final(20)
lista.inserir_final(30)
lista.inserir_final(40)
lista.inserir_final(50)
lista.inserir_final(60)
lista.inserir_final(70)
lista.inserir_final(80)
lista.inserir_final(90)
lista.inserir_final(100)

lista.imprimir()


