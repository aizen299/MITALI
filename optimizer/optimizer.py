import re

class CodeOptimizer:
    def __init__(self):
        self.dead_code_fsa = re.compile(r"(int|float|char|double)\s+(\w+)\s*=\s*.*?;")
        self.constant_folding_fsa = re.compile(r"(\d+)\s*([\+\-\*\/])\s*(\d+)")

    def optimize_dead_code(self, code):
        # Find all declared variables
        declared_variables = self.dead_code_fsa.findall(code)

        # Extract variable names
        variable_names = [var[1] for var in declared_variables]

        # Check which variables are actually used
        for var in variable_names:
            if re.search(rf"\b{var}\b", code):
                # Variable is used, skip removal
                continue
            # Remove unused variable declaration
            code = re.sub(rf"(int|float|char|double)\s+{var}\s*=\s*.*?;\n?", "", code)
        return code

    def optimize_constant_folding(self, code):
        def fold_constants(match):
            a, op, b = match.groups()
            result = eval(f"{a}{op}{b}")
            return str(result)

        return self.constant_folding_fsa.sub(fold_constants, code)

    def optimize(self, code):
        code = self.optimize_dead_code(code)
        code = self.optimize_constant_folding(code)
        return code