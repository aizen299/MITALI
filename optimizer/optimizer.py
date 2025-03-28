from .fsa import FSA


class CodeOptimizer:
    def __init__(self):
        self.dead_code_fsa = FSA.dead_code_fsa()
        self.constant_folding_fsa = FSA.constant_folding_fsa()

    def optimize_dead_code(self, code):
        # Remove unused variables
        return self.dead_code_fsa.sub("", code)

    def optimize_constant_folding(self, code):
        # Simplify constant expressions
        def fold_constants(match):
            a, op, b = match.groups()
            result = eval(f"{a}{op}{b}")
            return str(result)

        return self.constant_folding_fsa.sub(fold_constants, code)

    def optimize(self, code):
        optimized_code = self.optimize_dead_code(code)
        optimized_code = self.optimize_constant_folding(optimized_code)
        return optimized_code
