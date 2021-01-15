import sys
sys.path.append('.')

from DNA_RNA_Protein_Module import DNA, RNA, Protein, loadFile, findProteinsequences

def test_1():
    dnaString = loadFile("DATA\\DNA\\DNA_seq_altered.txt")
    dna = DNA(dnaString)
    rna = dna.createRNA()
    dna1 = rna.createDNA()
    if (dna.getSequence() == dna1.getSequence()):
        print("TEST 1: SUCCESS")
        return True
    return False

def test_2():
    dnaString_1 = loadFile("DATA\\DNA\\DNA_seq_altered.txt")
    dna = DNA(dnaString_1)
    dna.writeToFile("DATA\\DNA\\DNA_test_2.txt")
    dnaString_2 = loadFile("DATA\\DNA\\DNA_test_2.txt")
    if (dnaString_1 == dnaString_2):
        print("TEST 2: SUCCESS")
        return True
    return False

def test_3():
    dnaString = loadFile("DATA\\DNA\\DNA_seq_altered.txt")
    dna = DNA(dnaString)
    rna = dna.createRNA()
    rna.writeToFile("DATA\\RNA\\RNA_test_3.txt")
    rnaString = loadFile("DATA\\RNA\\RNA_test_3.txt")
    if ( (rna.getSequence() == rnaString) and (dna.getSequence() == dnaString) ):
        print("TEST 3: SUCCESS")
        return True
    return False

def test_4():
    dnaString = loadFile("DATA\\DNA\\DNA_test_2.txt")
    dna = DNA(dnaString)
    rnaString = loadFile("DATA\\RNA\\RNA_test_3.txt")
    rna = RNA(rnaString)
    rna_beginPositions = rna.findBeginSequence()
    rna_endPositions = rna.findEndSequence()
    dna_beginPositions = dna.findBeginSequence()
    dna_endPositions = dna.findEndSequence()
    if ((rna_beginPositions == dna_beginPositions) and (rna_endPositions == dna_endPositions)):
        valid_sequences = findProteinsequences(rna_beginPositions,rna_endPositions)
        firstInterval = valid_sequences[0]
        rna_subsection = rna.getSubSection(firstInterval)
        protein = rna_subsection.createProtein()
        protein.writeToFile("DATA\\PROTEIN\\Protein_test4.txt")
        builded_protein = loadFile("DATA\\PROTEIN\\Protein_test4.txt")
        valid_protein = loadFile("DATA\\PROTEIN\\amino_acid_sequence_original.txt")
        if ((protein.getSequence() == valid_protein) and (builded_protein == valid_protein)):
            print("TEST 4: SUCCESS")
            return True
    return False

def testProcess():
    """
    """
    try:
        if (test_1()):
            if (test_2()):
                if (test_3()):
                    if test_4():
                        print("TESTS SUCCESSFULL PASSED")
                        return True
        return False
    except Exception as exc:
        print(f'ERROR: {exc}')
        return False

if __name__ == "__main__":

   print(testProcess())

"""
#FIND Functions
def findBeginSequenceOnRNA(rnaSequence):
    return findInString('AUG', rnaSequence)

def findBeginSequenceOnDNA(dnaSequence):
    return findInString('ATG', dnaSequence)

def findEndSequenceOnRNA(rnaSequence):
    return sorted(findInString('UAA', rnaSequence) + findInString('UAG', rnaSequence) + findInString('UGA', rnaSequence))

def findEndSequenceOnDNA(dnaSequence):
    return sorted(findInString('TAA', dnaSequence) + findInString('TAG', dnaSequence) + findInString('TGA', dnaSequence))
"""



"""
def isSequenceDNA(seq):
    return genericSequenceController(seq, ["A","T","C","G"])

def isSequenceRNA(seq):
    return genericSequenceController(seq, ["A","U","C","G"])

def isSequenceProtein(seq):
    return genericSequenceController(seq, ["I","M","T","N","K","S","R","L","P","H","Q","V","A","D","E","G","F","Y","C","W"])
"""
"""
def createRNAbyDNA(dnaSequence):
    return dnaSequence.replace("T","U")

def createDNAbyRNA(rnaSequence):
    return rnaSequence.replace("U","T")

def translateARNtoProtein(seq):
    table = { 
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T', 
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R', 
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P', 
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R', 
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A', 
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G', 
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S', 
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L', 
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_', 
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
    } 
    protein ="" 

    for i in range(0, len(seq), 3): 
        codon = seq[i:i + 3] 
        try:
            protein+= table[codon]
        except :
            pass
    return protein 
"""