class Node:
    def __init__(self,song_path):
        self.song_path=song_path
        self.next=None
        self.prev=None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.current=None

    def add_song(self,song_path):
        new_node=Node(song_path)
        if not self.head:
            new_node.prev=new_node
            new_node.next=new_node
            self.head=new_node
        else:
            last=self.head.prev
            last.next=new_node
            new_node.prev = last
            self.head.prev=new_node
            new_node.next=self.head
    
    def display_playlist(self):
        if not self.head:
            print("PlayList is empty")
            return
        last = self.head
        print("Show the playlist")
        while True:
            print(last.song_path)
            last=last.next
            if last==self.head:
                break

    
    def next_song(self):
        if self.current:
            self.current=self.current.next
        return self.current.song_path

    def prev_song(self):
        if self.current:
            self.current=self.current.prev
        return self.current.song_path
