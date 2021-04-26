__author__ = "Ololade Waliu Jimoh, @drjimoh"
__copyright__ = "Copyright 2021, ITSmart Digital Skillz"

__email__ = "waliu.jimoh@yahoo.com"


class Sequencing:
    def __init__(self, sequence):
        self.sequence = sequence


    def validate_dna(self):
        # checking sequence to make sure it is dna sequence
        "this method checks if dna sequence is valid. Returns true if sequence is valid"
        dna_sequence_upper = self.sequence.upper()
        total_valid = (dna_sequence_upper.count("A") + dna_sequence_upper.count("C")
                        + dna_sequence_upper.count("G") + dna_sequence_upper.count("T"))
        if total_valid == len(dna_sequence_upper):
            return True
        else:
            return False
    def validate_rna(self):
        # checking sequence to make sure it is dna sequence
        "this method checks if rna sequence is valid. Returns true if sequence is valid"
        rna_sequence_upper = self.sequence.upper()
        total_valid = (rna_sequence_upper.count("A") + rna_sequence_upper.count("C")
                        + rna_sequence_upper.count("G") + rna_sequence_upper.count("U"))
        if total_valid == len(rna_sequence_upper):
            return True
        else:
            return False

    def frequency(self):
        """ Calculates the frequency of each symbol in the sequence.
            Returns a dictionary. """
        dic = {}
        for s in self.sequence.upper():
            if s in dic:
                dic[s] += 1
            else : dic[s] = 1
        return dic

    def gc_count(self):
        "calculate the number of GC content in sequence"
        gc_ct = self.sequence.upper().count("G") + self.sequence.upper().count("C")
        gc_percent = (gc_ct/len(self.sequence))*100
        return f"gc count is {gc_ct} and percent gc content is {gc_percent}"

if __name__ == '__main__':
    obj = Sequencing("ACCCCCCCTGGUGGGGxdfss")
    print(obj.validate_dna())
    print(obj.validate_rna())
    print(obj.frequency())
    print(obj.gc_count())
