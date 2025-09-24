from enum import Enum


class Note:

  def __init__(self, title, text, creation_date, important):
    self.title = title
    self.text = text
    self.creation_date = creation_date
    self.important = important


class Notebook:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
      cls._instance.notes = []
    return cls._instance

  def add_note(self, note):
    self.notes.append(note)

  def remove_note(self, title):
    for note in self.notes:
      if note.title == title:
        self.notes.remove(note)
        break

  def edit_note(self, title, new_text):
    for note in self.notes:
      if note.title == title:
        note.text = new_text
        break

  def view_notes(self):
    for note in self.notes:
      print(
          f"Title: {note.title}\nText: {note.text}\nCreation Date: {note.creation_date}\nImportant: {note.important}\n"
      )


class Strategy(Enum):
  DATE = 1
  IMPORTANCE = 2


class SortStrategy:

  def __init__(self, strategy):
    self.strategy = strategy

  def sort_notes(self, notes):
    if self.strategy == Strategy.DATE:
      return sorted(notes, key=lambda note: note.creation_date)
    elif self.strategy == Strategy.IMPORTANCE:
      return sorted(notes, key=lambda note: note.important, reverse=True)


class Command:

  def execute(self, notes):
    pass


class FilterImportantCommand(Command):

  def execute(self, notes):
    return [note for note in notes if note.important]


class ChainOfResponsibility:

  def __init__(self):
    self.commands = []

  def add_command(self, command):
    self.commands.append(command)

  def execute_commands(self, notes):
    result = notes
    for command in self.commands:
      result = command.execute(result)
    return result


if __name__ == "__main__":
  notebook = Notebook()

  # Добавление заметок
  note1 = Note("Meeting", "Meeting at 10am", "2022-01-01", True)
  note2 = Note("Groceries", "Buy milk and eggs", "2022-01-02", False)
  notebook.add_note(note1)
  notebook.add_note(note2)

  # Посмотреть все заметки
  print("All Notes:")
  notebook.view_notes()

  # Редактирование заметки
  notebook.edit_note("Meeting", "Meeting at 11am")

  # Посмотреть все заметкипосле редактирования
  print("All Notes after editing:")
  notebook.view_notes()

  # Перенос заметок
  notebook.remove_note("Groceries")

  # Посмотреть заметки после переноса
  print("All Notes after removing:")
  notebook.view_notes()

  # Сортировать заметки по дате
  sort_strategy = SortStrategy(Strategy.DATE)
  sorted_notes = sort_strategy.sort_notes(notebook.notes)
  print("Sorted Notes by Date:")
  for note in sorted_notes:
    print(
        f"Title: {note.title}\nText: {note.text}\nCreation Date: {note.creation_date}\nImportant: {note.important}\n"
    )

  # Фильтрация важных заметок
  filter_important_command = FilterImportantCommand()
  chain_of_responsibility = ChainOfResponsibility()
  chain_of_responsibility.add_command(filter_important_command)
  filtered_notes = chain_of_responsibility.execute_commands(notebook.notes)
  print("Filtered Important Notes:")
  for note in filtered_notes:
    print(
        f"Title: {note.title}\nText: {note.text}\nCreation Date: {note.creation_date}\nImportant: {note.important}\n"
    )
