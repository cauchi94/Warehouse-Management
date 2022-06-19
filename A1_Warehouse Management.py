#class Stock(object):
#    def __init__(self, units):
#        self.units = units
#        self.type = None
#    def get_units(self):
#        return self.units
#    def get_type(self):
#        return self.type
#    def set_units(self, newunits):
#        self.units = newunits
#    def set_type(self, newtype=''):
#        self.type = newname
#    def __str__(self):
#        return 'Stock type: '+str(self.type)+' has '+str(self.units)+' units.'

#class Stock(object):
#    def __init__(self, warehouse):
#        self.warehouse = warehouse
#        self.type = None
#    def get_warehouse(self):
#        return self.warehouse
#    def get_type(self):
#        return self.type
#    def set_warehouse(self, newwarehouse):
#        self.warehouse = newwarehouse
#    def set_type(self, newtype=''):
#        self.type = newtype
#    def __str__(self):
#        return 'Stock type: '+str(self.type)+' is located in warehouse '+str(self.warehouse)

#s = Stock()
#print(s)

class Type(Object):
    def __init__(self, type, units):
        Stock.__init__(self, units) #call Stock constructor to prevent from rewriting the code again
        self.set_type(type) #call Stock's method to set the type of stock
        self.units = 0 #add current units attribute and assign it to 0 units
    def get_units(self):
        return self.units #get amount of units for stock type
    def add_units(self, num):
        self.units += self.units + num #add the number of units to current units
    def remove_units(self, num):
        self.units += self.units - num #substract the number of units from current units
    def __str__(self):
        return 'Stock Type '+str(self.type)+' has '+str(self.units)+' units.'

    #def get_stockID(self):
    #    return self.stockID
    #def set_units(self, newunits):
    #    self.units = newunits
    #def set_stockID(self, newstockID = ''):
    #    self.stockID = newstockID

t1 = Type(4,1)
t2 = Type(6,2)
t3 = Type(8,3)
print(t1)
print(t2)
print(t3)

#t1.add_units(4)