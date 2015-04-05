'''Question: How can I use OOP to record sets of genes I need to use for
studies? Using OOP How can the genes that are part of my study?'''


class Gene(object):
    '''This class the basic information on a gene. Its arguments are it
    needs to have a name and start and stop coordinate'''
    start_coordinate = 35204
    stop_coordinate = 35235
    name = "APOA1"
    study = {}

    def __init__(self, start_coordinate, stop_coordinate, name):
        # everything attached to self is in the instance namespace
        # capture the start and stop coordinates of a gene
        self.start_coordinate = start_coordinate
        self.stop_coordinate = stop_coordinate
        self.name = name

    def range(self):
        '''This method determines the genes length of
        coverage but looking at the difference between the start and
        stop coordinates. Arguments: Gene Object '''
        self.coverage = self.stop_coordinate - self.start_coordinate
        return self.coverage

    def gene_study(self, name, start_coordinate, stop_coordinate):
            '''This method creates a dicionary to hold all the genes
            (and their information) as part of a study.'''

            if name not in self.study:
                self.study[name] = [start_coordinate, stop_coordinate]
                print name + "Your gene has been added."
            else:
                print name + "Your gene is already part of the study."

    def gene_lookup(self, x):
            '''This method uses the gene object and performs a lookup
            by gene name and informs the user if the gene is part of
            a study. Arguments: Gene Object and Gene name'''

            for k, v in self.study.iteritems():
                if x == v:
                    print "Genes that are part of your study:"
                    print '%s: %s' % (k, v)
                else:
                    print "No Genes in that study"

    def study_summary(self):
            '''This method uses the gene object to display the contents of
            a study. Arguments: Gene Object '''
            print "Gene, Start: Stop Coordinates:"
            print self.study.items()

if __name__ == "__main__":

    experiment1 = Gene(25000, 25005, "ABC")
    experiment1 = Gene(25005, 25015, "ABC1")
    experiment1 = Gene(25015, 25025, "ABC2")
    experiment1 = Gene(25025, 25055, "ABC3")

    # I want to add this experiment/and its genes to part of my study

    experiment1.gene_study("ABC ", 25000, 25005)
    experiment1.gene_study("ABC1 ", 25005, 25015)
    experiment1.gene_study("ABC2 ", 25015, 25025)
    experiment1.gene_study("ABC3 ", 25025, 25055)

    # I want to see the contents of my study

    print(experiment1.study_summary())
