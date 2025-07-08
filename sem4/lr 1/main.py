#Вариант 5.
import pprint as pp
from tree import gen_bin_tree, gen_bin_tree_nonrec

if __name__ == '__main__':

  print('Рекурсивный вариант.')
  pp.pprint(gen_bin_tree(height=2, root=5), indent=4, depth=2, width=6)

  print('Не рекурсивный вариант.')
  pp.pprint(gen_bin_tree_nonrec(height=4, root=5), indent=4, depth=2, width=6)
