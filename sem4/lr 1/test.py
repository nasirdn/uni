import unittest
from tree import gen_bin_tree, gen_bin_tree_nonrec

class TestBinaryTreeGeneration(unittest.TestCase):

    # Тесты для рекурсивной функции
    def test_gen_bin_tree(self):
        self.assertEqual(gen_bin_tree(height=0, root=5), {'5': []})
        self.assertEqual(gen_bin_tree(height=1, root=5), {'5': [{'25': []}, {'3': []}]})

        self.assertEqual(gen_bin_tree(height=2, root=5), {'5': [{'25': [{'625': [   ]},
                                                                        {'23': [   ]}]},
                                                                {'3': [{'9': [   ]},
                                                                        {'1': [   ]}]}]})


    # Тесты для нерекурсивной функции
    def test_gen_bin_tree_nonrec(self):
        self.assertEqual(gen_bin_tree_nonrec(0, 5), {'5': []})
        self.assertEqual(gen_bin_tree_nonrec(1, 5), {'5': [{'25': []}, {'3': []}]})
        self.assertEqual(gen_bin_tree_nonrec(2, 5), {'5': [{'25': [{'625': []}, {'23': []}]}, {'3': [{'9': []}, {'1': []}]}]})

if __name__ == '__main__':
    unittest.main()
