import logging
from exceptions import *

# Настройка логгеров
logger_main = logging.getLogger('main')
logger_main.setLevel(logging.INFO)

logger_gbt = logging.getLogger('gen_bin_tree')
logger_gbt.setLevel(logging.INFO)

# Создаем форматировщик
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# Настройка обработчиков для файлов
handler_main_file = logging.FileHandler("main.log", mode='w')
handler_main_file.setFormatter(formatter)

handler_gbt_file = logging.FileHandler('gen_bin_tree.log', mode='w')
handler_gbt_file.setFormatter(formatter)

# Добавление обработчиков к логгерам
logger_main.addHandler(handler_main_file)
logger_gbt.addHandler(handler_gbt_file)

# рекурсивная версия
def rec_tree(height: int, root):
    '''Функция создаёт двоичное дерево заданной высоты рекурсивным методом'''
    try:
        logger_gbt.info('Вызвана функция rec_bin_tree')
        if type(height) != int:
            logger_gbt.error('Отловлена ошибка типа высоты дерева')
            raise HeightIsNotAnIntegerException(
                "Ошибка, высота дерева должна быть целым значением")

        if height < 0:
            logger_gbt.error('Отловлена ошибка отрицательной высоты дерева')
            raise HeightBelowZeroException(
                "Ошибка, высота дерева не может быть отрицательной")

        if type(root) != int and type(root) != float:
            logger_gbt.error('Отловлена ошибка типа корня дерева')
            raise RootIsNotANumberException(
                "Ошибка, корень дерева должен быть числом")

        elif height == 0:
            return {}
        else:
            return {
                root: {
                    root**2: rec_tree(height - 1, root**2),
                    root - 2: rec_tree(height - 1, root - 2)
                }
            }
    except BinaryTreeException:
        logger_gbt.error('Во время исполнения функции произошла ошибка')
    finally:
        logger_gbt.info('Функция завершена')

# нерекурсивная версия
def nonrec_tree(height: int, root):
    '''Функция создаёт двоичное дерево заданной высоты нерекурсивным методом'''
    try:
        logger_gbt.info('Вызвана функция non_rec_bin_tree')
        if type(height) != int:
            logger_gbt.error('Отловлена ошибка типа высоты дерева')
            raise HeightIsNotAnIntegerException(
                "Ошибка, высота дерева должна быть целым значением")

        if height < 0:
            logger_gbt.error('Отловлена ошибка отрицательной высоты дерева')
            raise HeightBelowZeroException(
                "Ошибка, высота дерева не может быть отрицательной")

        if type(root) != int and type(root) != float:
            logger_gbt.error('Отловлена ошибка типа корня дерева')
            raise RootIsNotANumberException(
                "Ошибка, корень дерева должен быть числом")

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

    except BinaryTreeException:
        logger_gbt.error('Во время исполнения функции произошла ошибка')
    finally:
        logger_gbt.info('Функция завершена')

# вызов функции
def main():
  try:
      logger_main.info('Вызвана функция main')
      nonrec_tree(2, -1)
      nonrec_tree(-1, 1)
      nonrec_tree(0.5, 1)
      nonrec_tree(2, '1')

      rec_tree(2, -1)
      rec_tree(-1, 1)
      rec_tree(0.5, 1)
      rec_tree(2, '1')
      logger_main.info(
          'Все функции выполнены успешно')
  except Exception as e:
      logger_main.error(f'Во время выполнения функции произошла ошибка: {e}')

if __name__ == '__main__':
    try:
        main()
    finally:
        logging.shutdown()