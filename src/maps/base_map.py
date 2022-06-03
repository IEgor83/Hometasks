from abc import ABC, abstractmethod

from typing import Iterable, Tuple, List

from os import path


class BaseMap(ABC):
  @abstractmethod
  def __setitem__(self, key: str, value: int) -> None:
    ...

  @abstractmethod
  def __getitem__(self, key: str) -> int:
    ...

  @abstractmethod
  def __delitem__(self, key: str) -> None:
    ...

  @abstractmethod
  def __iter__(self) -> Iterable[Tuple[str, int]]:
    ...

  def __contains__(self, key: str) -> bool:
    for keys, elems in self:
      if key == keys:
        return True
    return False

  def __eq__(self, other: 'BaseMap') -> bool:
    if len(self) != len(other):
      return False
    for i in self:
      if not i[0] in other:
        return False
      if other[i[0]] != i[1]:
        return False
    return True

  def __bool__(self) -> bool:
    if len(self) == 0:
      return False
    return True

  @abstractmethod
  def __len__(self):
    ...

  def items(self) -> Iterable[Tuple[str, int]]:
    yield from self

  def values(self) -> Iterable[int]:
    return (item[1] for item in self)

  def keys(self) -> Iterable[str]:
    return (item[1] for item in self)

  @classmethod
  def fromkeys(cls, iterable, value=None) -> 'BaseMap':
    my_class = cls()
    for key in iterable:
      my_class[key] = value
    return iterable

  def update(self, other=None) -> None:
    if other is not None:
      for key, value in other:
        self[key] = value


  def get(self, key, default=None):
    if key in self:
      return self[key]
    return default

  def pop(self, key, *args):
    if key in self:
      val = self[key]
      del self[key]
      return val
    else:
      if len(args) > 0:
        return args
      raise KeyError

  def popitem(self):
    if len(self) == 0:
      raise KeyError
    for elem in self:
      last_elem = elem
    del self[last_elem[0]]
    return last_elem

  def setdefault(self, key, default=None):
    if key in self:
      return self[key]
    else:
      self[key] = default
      return default

  def clear(self):
    for item in self:
      del self[item[0]]
    return self

  def write(self, path: str) -> None:
    with open(path, "w+", encoding="utf-8") as file:
      for item in self:
        for j in item:
          file.write(f"{j.key}:{j.value}\n")

  @classmethod
  def read(cls, path: str) -> 'BaseMap':
    new_object = cls()
    opened_file = open(path + '/dict.txt', 'r')
    for item in opened_file:
      new_object[item[0]] = item[1]
    return new_object

