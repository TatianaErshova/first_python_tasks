#!/usr/bin/env python3
import sys
import subprocess
from linked_list_ping import LinkedList

if len(sys.argv)>1:
    print(sys.argv[1])
    try:
        ping_result = subprocess.run(['ping', '-c',sys.argv[2],sys.argv[1]],text=True, capture_output=True, check=True)
    except subprocess.CalledProcessError:
        print("packet loss :(")
        exit(1)
    print(ping_result.stdout)
    print(ping_result.stderr)
    ping_result_split = ping_result.stdout.split("\n")
    #print(ping_result_split[1])
def createlinkedlist(ping_result_split):
    el = LinkedList()
    for i in range(len(ping_result_split)-1,-1,-1):
        el.add(ping_result_split[i])
        a = el.head
        print("-------------------")
        while a!= None:
            print(a.data)
            a = a.next
    return(el)
el1 = createlinkedlist(["line1","line2","line3","line4"])
#el1.addtosecond('222222')
#b = el1.head
#print("11111111111111111111111111")
#while b != None:
 #   print(b.data)
 #   b = b.next

el1.deletefirst()

el1.add("newline")
b = el1.head
print("11111111111111111111111111")
while b != None:
    print(b.data)
    b = b.next