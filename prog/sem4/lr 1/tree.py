#Вариант рекурсивной функции.


def gen_bin_tree(height: int, root: int):

  if height < 0 or type(height) != int or type(root) != int:
    raise ValueError('Root and/or height values invalid')

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


#Вариант не рекурсивной функции.


def gen_bin_tree_nonrec(height: int, root: int):

  if height < 0 or type(height) != int or type(root) != int:
    raise ValueError('Root and/or height values invalid')

  left_func = lambda root: root**2
  right_func = lambda root: root - 2

  tree = {str(root): []}

  if height == 0:
    return tree

  queue = [(root, height, tree)]

  while queue:
    current_root, current_height, current_tree = queue.pop(0)

    if current_height > 0:
      l_r = left_func(current_root)
      r_r = right_func(current_root)
      left_node = {str(l_r): []}
      right_node = {str(r_r): []}
      current_tree[str(current_root)].extend([left_node, right_node])
      queue.append((l_r, current_height - 1, left_node))
      queue.append((r_r, current_height - 1, right_node))

  return tree
