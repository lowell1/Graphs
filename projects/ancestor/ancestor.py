import sys

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    queue = Queue()
    queue.enqueue(starting_node)
     
    last_ancestors = []
    while queue.size() > 0:
        new_parents = []

        while queue.size() > 0:
            cur_node = queue.dequeue()

            #find the parent nodes of the current node
            for item in ancestors:
                if item[1] == cur_node:
                    new_parents.append(item[0])

        if len(new_parents) > 0:
            last_ancestors = new_parents[:]

        for x in new_parents:
            queue.enqueue(x)

    if len(last_ancestors) == 0:
        return -1
    
    if len(last_ancestors) == 1:
        return last_ancestors[0]
    
    if last_ancestors[0] < last_ancestors[1]:
        return last_ancestors[0]

    return last_ancestors[1]