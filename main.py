from optimizer.lexer import Lexer
from optimizer.optimizer import CodeOptimizer
from optimizer.utils import read_file, write_file


def main():
    # Load code sample
    file_path = "examples/sample_code.c"
    code = read_file(file_path)

    print("Original Code:")
    print(code)

    # Tokenize code
    lexer = Lexer()
    tokens = lexer.tokenize(code)
    print("\nTokens:")
    print(tokens)

    # Optimize code
    optimizer = CodeOptimizer()
    optimized_code = optimizer.optimize(code)

    print("\nOptimized Code:")
    print(optimized_code)

    # Save optimized code
    output_path = "examples/optimized_code.c"
    write_file(output_path, optimized_code)
    print(f"\nOptimized code saved to {output_path}")


if __name__ == "__main__":
    main()
