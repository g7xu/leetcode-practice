# doubly linked-list
# hashtable

# Node for double linked list
class Node(object):
    def __init__(self, key, val, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.current_size = 0
        self.cache_dict = dict() # dict storing the node
        
        # double link list with dummy node
        front_dummy = Node(-1, -1)
        end_dummy = Node(-1, -1)
        front_dummy.next = end_dummy
        end_dummy.pre = front_dummy
        self.cache_recent_begin = front_dummy
        self.cache_recent_end = end_dummy
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache_dict:
            # update the recent by moving the node to the front
            target_node = self.cache_dict[key]

            # remove current node
            target_node.pre.next = target_node.next
            target_node.next.pre = target_node.pre

            # move to the front
            target_node.pre = self.cache_recent_begin
            target_node.next = self.cache_recent_begin.next

            self.cache_recent_begin.next.pre = target_node
            self.cache_recent_begin.next = target_node
            

            return target_node.val

        return -1
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache_dict:
            self.get(key)
            self.cache_dict[key].val = value
            return

        
        if self.current_size + 1 <= self.capacity:
            target_node = Node(key, value)
            self.current_size += 1

            self.cache_dict[key] = target_node

            # move to the front
            target_node.pre = self.cache_recent_begin
            target_node.next = self.cache_recent_begin.next

            self.cache_recent_begin.next.pre = target_node
            self.cache_recent_begin.next = target_node
        else:
            target_node = Node(key, value)

            # remove from double linkedlist
            to_remove_node = self.cache_recent_end.pre
            to_remove_node.pre.next = to_remove_node.next
            to_remove_node.next.pre = to_remove_node.pre
            to_remove_node.next = None
            to_remove_node.pre = None
            
            # remove from dict
            del self.cache_dict[to_remove_node.key]

            # update dict
            self.cache_dict[key] = target_node
            
            # move this add node to the font
            target_node.pre = self.cache_recent_begin
            target_node.next = self.cache_recent_begin.next

            self.cache_recent_begin.next.pre = target_node
            self.cache_recent_begin.next = target_node




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)