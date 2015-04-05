'''Question How can create subclasses that hold additional (and different)
attributes from my original Gene object? How can I add attributes like
color coding, assigning a gene to a biological process, determining if
it is cancerous, and if the gene is one that plays a vital part in the human
genome?'''


class Gene(object):

    '''This class the basic information on a gene. Its arguments are it
    needs to have a name and start and stop coordinate'''
    start_coordinate = 35204
    stop_coordinate = 35235
    name = "APOA1"

    def __init__(self, start_coordinate, stop_coordinate, name):
        # everything attached to self is in the instance namespace
        self.start_coordinate = start_coordinate
        self.stop_coordinate = stop_coordinate
        self.name = name
        # additional attributes
        self.biological_process = "interferon response"
        self.color = "gray"
        self.is_this_gene_cancerous = True
        self.is_important_to_human_genome = False


class ColorCode(Gene):
    '''Question: Can we color code are genes to rank their importance?
    This class uses Gene and adds a new attribute that color codes
    the gene Gene Object. Arguments: Gene Object'''
    color = "red"


class BioProcess(Gene):
    '''Question: Can we assign our gene to known biological process?
    This class uses Gene and adds a new attribute that adds a known
    biological process to the gene. Arguments: Gene Object'''
    biological_process = "infectious disease"


class Cancerous(Gene):
    '''Question: Can we track the gene known to be associated with
    cancer? This class uses Gene and adds a new attribute that qualifies
    if the gene is known to be related in cancer Arguments: Gene Object'''
    is_this_gene_cancerous = False


class Important2HumanGenome(Gene):
    '''Question: Is this gene vital to the human genome? or is it not
    that important? This class uses Gene and adds a new attribute that
    qualifies if the gene plays a vital role in basic human genomic function.
    Arguments: Gene Object'''
    is_important_to_human_genome = True


if __name__ == "__main__":

    # We have created 4 sub classes now lets create 4 methods to override them!
    # We start with a new method that operates off the attributes that
    # are already a part of the Gene Class

    def update_annotation(self):
        new_annotation_start = self.start_coordinate + 10
        new_annotation_stop = self.start_coordinate - 25
        return (new_annotation_start, new_annotation_stop)

    def gene_color(self, x):
        self.color = x
        print self.name
        return self.color

    def bio_process(self, x):
        self.biological_process = x
        return self.biological_process

    def is_cancerous(self, x):
        self.is_this_gene_cancerous = x
        return self.is_this_gene_cancerous

    def important_to_genome(self, x):
        self.is_important_to_human_genome = x
        return self.is_important_to_human_genome

    new_gene = Gene(25000, 25005, "ABC")

    print update_annotation(new_gene)
    print gene_color(new_gene, "blue")
    print bio_process(new_gene, "innate immune signaling")
    print is_cancerous(new_gene, False)
    print important_to_genome(new_gene, True)
