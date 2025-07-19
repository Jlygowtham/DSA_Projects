class Node:
    def __init__(self,song_path):
        self.song_path=song_path
        self.next=None
        self.prev=None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beg(self,song_path):
        new_node=Node(song_path)
        if not self.head:
            new_node.prev=new_node
            new_node.next=new_node
            self.head=new_node
            print("Added Head node")
        else:
            last=self.head.prev
            new_node.next=self.head 
            self.head.prev=new_node
            new_node.prev=last
            last.next=new_node
            self.head=new_node

    def insert_at_end(self,song_path):
        new_node=Node(song_path)
        if not self.head:
            new_node.prev=new_node
            new_node.next=new_node
            self.head=new_node
            print("Added Head node")
        else:
            last=self.head.prev
            last.next=new_node
            new_node.prev = last
            self.head.prev=new_node
            new_node.next=self.head
            print("Added new node")

    def print_forward(self):
        print("Print the Circular LinkedList is forward")
        if not self.head:
            print("LinkedList is empty")
            return
        result=[]
        last = self.head
        while True:
            result.append(last.song_path)
            last=last.next
            if last==self.head:
                break
        print(result)

    def print_backward(self):
        print("Print the Circular LinkedList is backward")
        if not self.head:
            print("LinkedList is empty")
            return
        result=[]
        last=self.head.prev
        while True:
            result.append(last.song_path)
            last=last.prev
            if last==self.head.prev:
                break
        print(result)


# cl=CircularDoublyLinkedList()
# cl.insert_at_end(5)
# cl.insert_at_end(10)
# cl.insert_at_end(15)
# cl.insert_at_end(20)
# cl.insert_at_end(25)
# print("---------------------")
# cl.print_forward()
# cl.print_backward()