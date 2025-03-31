from __future__ import annotations


class DNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        self.adenine = 'A'
        self.cythosine = 'C'
        self.guanine = 'G'
        self.thymine = 'T'
   
    def __len__(self) -> int:
        return len(self.sequence)
        
    def __str__(self) -> str:
        return f'{self.sequence}'

    def adenines(self) -> int:
        num_adenines = self.sequence.count(self.adenine)
        return num_adenines

    def guanines(self) -> int:
        num_guanines = self.sequence.count(self.guanine)
        return num_guanines
    
    def cytosines(self) -> int:
        num_cythosines = self.sequence.count(self.cythosine)
        return num_cythosines
    
    def thymines(self) -> int:
        num_thymines = self.sequence.count(self.thymine)
        return num_thymines
    
    def __add__(self, other: DNA) -> DNA:
        for dna1, dna2 in zip(self.sequence, other.sequence):
            dna = ''
            lenght_dna1 = len(dna1)
            lenght_dna2 = len(dna2)
            if lenght_dna1 < lenght_dna2:
                dna = dna2 + dna1
            else:
                dna = dna1 + dna2
        return dna

    def stats(self) -> dict[str,float]:
        pass
    def __mul__(self, other: DNA) -> DNA:
        pass
    def build_from_file(cls, path: str) -> DNA:
        pass
    def dump_from_file(self, path: str) -> None:
        pass
    def __getitem__(self, index: int) -> str:
        pass
    def __setitem__(self,index: int, base: str) -> None:
        pass