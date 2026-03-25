class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None 
    
    def inserir_inicio(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    
    def numb_node(self):
        aux=0
        atual=self.head 
        while(atual):
            aux+=1
            atual=atual.next
        print(f"numbers of Node is {aux}")

    def in_list(self,X):
        aux=-1
        aux2=self.head 
        while(aux2):
            if(aux2.data==X):
                aux=1
                break
            aux2=aux2.next
        if(aux==1):
            print("encontrado")
        else:
            print("não encontrado")
                
        



 #teste
lista = Linked_list()

lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_inicio(30)
lista.inserir_inicio(40)
lista.inserir_inicio(50)
lista.inserir_inicio(60)
lista.inserir_inicio(70)
lista.inserir_inicio(80)
lista.inserir_inicio(90)
lista.inserir_inicio(100)
lista.inserir_inicio(110)
lista.inserir_inicio(120)

lista.in_list(25)
lista.in_list(55)
lista.in_list(88)

lista.in_list(20)
lista.in_list(50)
lista.in_list(80)