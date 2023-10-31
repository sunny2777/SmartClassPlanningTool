class Node:
    def __init__(self,number,name,offered,pre):
        self.number=number
        self.name=name
        self.offered=offered
        self.pre=pre

    def get_number(self):
        return self.number

    def get_name(self):
        return self.name

    def get_offer(self):
        return self.offered
    def get_pre(self):
        return self.pre