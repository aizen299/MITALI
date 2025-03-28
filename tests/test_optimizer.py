import unittest
from optimizer.optimizer import CodeOptimizer

class TestCodeOptimizer(unittest.TestCase):
    def setUp(self):
        self.optimizer = CodeOptimizer()

    def test_dead_code_elimination(self):
        code = """
        int unused_var = 20;
        int a = 5;
        int b = a + 10;
        """
        optimized_code = self.optimizer.optimize_dead_code(code)
        self.assertNotIn("unused_var", optimized_code)  # unused_var should be removed
        self.assertIn("int a = 5;", optimized_code)     # a should remain

    def test_constant_folding(self):
        code = "int a = 5 + 3;\n"
        optimized_code = self.optimizer.optimize_constant_folding(code)
        self.assertIn("int a = 8;", optimized_code)

if __name__ == "__main__":
    unittest.main()