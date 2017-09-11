import datetime

class Call(object):
    def __init__(self,idn,caller,phone,time,reason):
        self.idn = idn
        self.caller = caller
        self.phone = phone
        self.time = time
        self.reason = reason

    def display(self):
        print(self.idn)
        print(self.caller)
        print(self.phone)
        print(self.time)
        print(self.reason)

class CallCenter(object):
    def __init__(self,call_q,q_size):
        self.call_q = call_q
        self.q_size = q_size

    def add(self,new_call):
        self.call_q.append(new_call)

    def remove(self):
        self.call_q.remove(self.call_q[0])

    def remove_specific(self,phone_num):
        for call in self.call_q:
            if call.phone == phone_num:
                self.call_q.remove(call)
    
    def sort_me(self):
        for call in self.call_q:
            self.call_q = sorted(self.call_q,key = lambda call:call.phone)

    def info(self):
        position = 1
        for ppl in self.call_q:
            printout = ""
            printout += str(position)
            printout += ": "
            printout += ppl.caller
            printout += " "
            printout += ppl.phone
            printout += str(self.q_size)
            position += 1
            print printout    

sadie = Call(1,"sadie","(555)555-5555","1:00","dumb")
brownie = Call(2,"brownie","(222)222-2222","3:30","also dumb")
unsub = Call(3,"unsub","(666)666-6666","6:60","MURDER")
reid = Call(4,"reid","(314)159-2653","3:14","nerd")

my_calls = [sadie,brownie,unsub]

penelope = CallCenter(my_calls,len(my_calls))
