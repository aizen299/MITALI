import re


class FSA:
    @staticmethod
    def dead_code_fsa():
        # Matches unused variables
        return re.compile(r"(int|float|char|double)\s+\w+\s*=\s*.*?;\n(?!.*\b\w+\b)")

    @staticmethod
    def constant_folding_fsa():
        # Matches expressions with constant values
        return re.compile(r"(\d+)\s*([\+\-\*\/])\s*(\d+)")
