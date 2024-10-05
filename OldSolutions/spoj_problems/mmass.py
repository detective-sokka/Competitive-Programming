# spoj.com Problem code - MMASS (Accepted)

'''
Testcases:
COOH
CH(CO2H)3
((CH)2(OH2H)(C(H))O)3

Answers:
45
148
222
'''


class MoleculeWeight:
    def __init__(self):
        self.total_weight = 0
        self.stack_ = [0]
        self.molecule = []
        self.atomic_weights = {'H': 1, 'C': 12, 'O': 16}

    def inputMolecule(self, molecule):
        self.molecule = list(molecule)

    def calcWeight(self):
        prev = self.molecule[0]
        local_weight = 0
        self.stack_.append(local_weight)

        for curr in self.molecule:
            if curr == '(':
                local_weight = 0
                self.stack_.append(local_weight)

            elif curr in self.atomic_weights:
                self.stack_[-1] += self.atomic_weights[curr]

            elif curr == ')':
                local_weight = self.stack_.pop()
                self.stack_[-1] += local_weight

            elif '2' <= curr <= '9':
                if prev == ')':
                    self.stack_[-1] -= local_weight
                    local_weight *= int(curr)
                    self.stack_[-1] += local_weight
                    local_weight = 0
                else:
                    self.stack_[-1] -= self.atomic_weights[prev]
                    self.stack_[-1] += self.atomic_weights[prev] * int(curr)

            prev = curr
        self.total_weight = self.stack_.pop()

    def returnWeight(self):
        if self.total_weight == 0:
            self.calcWeight()
        return self.total_weight


def main():
    input_molecule = MoleculeWeight()
    input_molecule.inputMolecule(input())
    print(input_molecule.returnWeight())


if __name__ == "__main__":
    main()


