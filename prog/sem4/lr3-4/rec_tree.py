#Вариант рекурсивной функции.

def gen_bin_tree(height: int, root: int):

  left_func = lambda root: root**2
  right_func = lambda root: root - 2

  tree = {str(root): []}

  if height == 0:
    return tree
  else:
    l_r = left_func(root)
    r_r = right_func(root)
    a = gen_bin_tree(root=l_r, height=height - 1)
    tree[str(root)].append(a)
    b = gen_bin_tree(root=r_r, height=height - 1)
    tree[str(root)].append(b)
    return tree
