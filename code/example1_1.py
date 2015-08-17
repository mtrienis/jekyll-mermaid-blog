def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')


print "list1 = %s" % list1 # list1 = [10, 'a']
print "list2 = %s" % list2 # list2 = [123]
print "list3 = %s" % list3 # list3 = [10, 'a']


def extendListUpdated(val, list=None):
    # if no list is provided initialize an empty list
    if list is None:
        list = []
    list.append(val)
    return list


list1 = extendListUpdated(10)
list2 = extendListUpdated(123,[])
list3 = extendListUpdated('a')

print "list1 = %s" % list1 # [10]
print "list2 = %s" % list2 # [123]
print "list3 = %s" % list3 # ['a']
