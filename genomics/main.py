__author__ = "Ololade Waliu Jimoh, @drjimoh"
__copyright__ = "Copyright 2021, ITSmart Digital Skillz"

__email__ = "waliu.jimoh@yahoo.com"



def read_fasta(path):
    my_file = open(path)
    content = my_file.read()
    print(content)


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


    def gc_content_subseq(self, k):
        """ Returns GC content of non−overlapping sub−sequences of size k
                . The result is a list. """
        res = []
        for i in range(0, len(self.sequence)-k+1, k):
            subseq = self.sequence[i:i+k]
            gc = self.gc_count()
            res.append(gc)
        return res 

    def transcription(self):
        "function that computes the RNA corresponding to the DNA sequence provided"

        assert self.validate_dna(), "Invalid DNA sequence"
        return self.sequence.upper().replace("T", "U")

    def reverse_complement(self):
        assert self.validate_dna(), "Invalid DNA sequence"
        comp = ""
        for c in self.sequence.upper():
            if c=="A":
                comp= "T"+comp
            elif c=="T":
                comp = "A"+comp
            elif c=="G":
                comp = "C"+comp
            elif c=="C":
                comp = "G"+comp

        return comp
if __name__ == '__main__':
    obj = Sequencing("ATTGCGCGATACCGCG")
    print(obj.validate_dna())
    print(obj.validate_rna())
    print(obj.frequency())
    print(obj.gc_count())
    print(obj.gc_content_subseq(3))
    print(obj.transcription())
    print(obj.reverse_complement())
