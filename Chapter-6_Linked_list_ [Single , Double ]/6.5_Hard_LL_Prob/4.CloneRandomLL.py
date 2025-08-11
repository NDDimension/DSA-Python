"""
"Clone the Linked List having Next & Random Pointers"

=> We will be given with a special kind of linked list where we do have the next pointers
    along with a new random pointer which can point to anywhere.

=> Our task is to clone this particular LL and display it.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


class LinkedList:
    def __init__(self, data_arr=None, random_map=None):
        self.head = None
        self.nodes_by_data = {}

        if data_arr:
            self._create_list(data_arr)
            if random_map:
                self._assign_random(random_map)

    def _create_list(self, arr):
        self.head = Node(arr[0])
        self.nodes_by_data[arr[0]] = self.head
        current = self.head

        for data in arr[1:]:
            newNode = Node(data)
            self.nodes_by_data[data] = newNode
            current.next = newNode
            current = newNode

    def _assign_random(self, random_map):
        for key, val in random_map.items():
            if key in self.nodes_by_data:
                self.nodes_by_data[key].random = self.nodes_by_data.get(val, None)

    def p_LL(self):
        temp = self.head
        idx = 0

        while temp:
            rand_data = temp.random.data if temp.random else "None"
            print(f"[{idx}] Data: {temp.data}, Random: {rand_data}")
            temp = temp.next
            idx += 1


data = [7, 14, 21, 28]
random_map = {7: 21, 14: 7, 21: 28, 28: 14}

l1 = LinkedList(data, random_map)
l1.p_LL()

# Simple Approach
# Time Complexity : O(2n)
# Space Complexity : O(2n)
"""
We will be creating a copy of everynode first , then we are going to iterate and 
assign the next pointer and random pointers to it .
"""


def clone(head):
    if not head:
        return None

    temp = head
    node_map = {}

    # Cloning nodes
    while temp:
        node_map[temp] = Node(temp.data)
        temp = temp.next

    # Assigning Pointers
    temp = head
    while temp:
        clone = node_map[temp]
        clone.next = node_map.get(temp.next)
        clone.random = node_map.get(temp.random)
        temp = temp.next

    return node_map[head]


l1.head = clone(l1.head)
l1.p_LL()

# Optimal Approach
# Time Complexity : O(3n)
# Space Complexity : O(1)
"""
We are going to insert copy nodes in between the nodes .
Next we will be connecting the random pointers
Lastly separating both the Linked Lists and restoring back the original one
along with next pointer connections.
"""


def clone_Optimal(head):
    # Step 1 : Inserting in between
    if not head:
        return None

    temp = head
    while temp:
        copyNode = Node(temp.data)
        copyNode.next = temp.next
        temp.next = copyNode
        temp = temp.next.next

    # Step 2 : Connecting Random Pointers
    temp = head
    while temp:
        copyNode = temp.next
        copyNode.random = temp.random.next
        temp = temp.next.next

    # Step 3 : Connecting Next Pointers
    dNode = Node(-1)
    res = dNode
    temp = head
    while temp:
        res.next = temp.next
        temp.next = temp.next.next

        res = res.next
        temp = temp.next

    return dNode.next


l1.head = clone_Optimal(l1.head)
l1.p_LL()
