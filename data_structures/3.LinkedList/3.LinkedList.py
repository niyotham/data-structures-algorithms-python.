class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def  insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head= node

    def print(self):
        if self.head is None:
            print("Link list is empty")
            return
        itr= self.head

        llstr=""
        while itr:
            llstr += str(itr.data) + '---->' # if itr.next else str(itr.data)
            itr = itr.next

        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr.next
        return count

    def  insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr= self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_at(self):
        pass

    def remove_at(self, index):
        pass

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(70)
    ll.print()

    ll.insert_values(["banana","mango","grapes","orange"])

    ll.print()