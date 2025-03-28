import re


class Lexer:
    def __init__(self):
        self.tokens = []

    def tokenize(self, code):
        # Define regex patterns for tokens
        token_specification = [
            ("NUMBER", r"\b\d+\b"),  # Numbers
            ("IDENTIFIER", r"\b[a-zA-Z_]\w*\b"),  # Variable names
            ("OPERATOR", r"[+\-*/=]"),  # Operators
            ("SEPARATOR", r"[;{}()]"),  # Separators
            ("WHITESPACE", r"\s+"),  # Whitespace (ignored)
            ("COMMENT", r"//.*"),  # Comments (ignored)
        ]
        combined_regex = "|".join(
            f"(?P<{pair[0]}>{pair[1]})" for pair in token_specification
        )
        for match in re.finditer(combined_regex, code):
            kind = match.lastgroup
            value = match.group()
            if kind != "WHITESPACE" and kind != "COMMENT":
                self.tokens.append((kind, value))
        return self.tokens
