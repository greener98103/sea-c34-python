'''Question How can I define a class in python that captures information
on Genes in my experiment? How can I determine the genomic range of a gene?'''


class Gene(object):
    '''This class holds the basic information on a gene. Its arguments are it
    needs to have a name and start and stop coordinate'''
    start_coordinate = 35204
    stop_coordinate = 35235
    name = "APOA1"

    def __init__(self, start_coordinate, stop_coordinate, name):
        # everything attached to self is in the instance namespace
        self.start_coordinate = start_coordinate
        self.stop_coordinate = stop_coordinate
        self.name = name

    def range(self):
        '''Here is a method that determines the genes length of
        coverage'''
        self.coverage = self.stop_coordinate - self.start_coordinate
        return self.coverage

# create an instance of the class

expression = Gene(35007, 35027, "APOA3")
print(expression.name)
print(expression.start_coordinate)
print(expression.stop_coordinate)
print(expression.range())
