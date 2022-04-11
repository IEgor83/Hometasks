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


  def __bool__(self) -> bool:


  @abstractmethod
  def __len__(self):
    ...

  def items(self) -> Iterable[Tuple[str, int]]:


  def values(self) -> Iterable[int]:


  def keys(self) -> Iterable[str]:


  @classmethod
  def fromkeys(cls, iterable, value=None) -> 'BaseMap':


  def update(self, other=None) -> None:


  def get(self, key, default=None):


  def pop(self, key, *args):


  def popitem(self):


  def setdefault(self, key, default=None):


  def clear(self):


  def write(self, path: str) -> None:


  @classmethod
  def read(cls, path: str) -> 'BaseMap':
    


class NodeTree:
  def __init__(self, key: str = None, value=None, left=None, right=None):
    self.key = key
    self.value = value
    self.left = left
    self.right = right


class HashTree(BaseMap):
  def __init__(self):
    self.head = None
    self.length = 0

  @classmethod
  def add(cls, a, key, value):
    if key > a.key:
      if a.right is None:
        a.right = NodeTree(key, value)
      else:
        cls.add(a.right, key, value)
    elif key < a.key:
      if a.left is None:
        a.left = NodeTree(key, value)
      else:
        cls.add(a.left, key, value)
    else:
      a.value = value

  def __setitem__(self, key, value):
    if self.head is None:
      self.head = NodeTree(key, value)
      self.length += 1
    else:
      a = self.head
      self.add(a, key, value)
      self.length += 1

  def __getitem__(self, key):
    a = self.head
    while a:
      if a.key == key:
        return a.value
      else:
        if key > a.key:
          a = a.right
        else:
          a = a.left
    raise KeyError

  def __delitem__(self, key):
    def del_elem(elem, key):
      if not elem:
        raise KeyError
      if elem.key > key:
        elem.left = del_elem(elem.left, key)
        return elem
      elif elem.key < key:
        elem.right = del_elem(elem.right, key)
        return elem
      else:
        if elem.left and elem.right:
          a = elem.left
          while a.right:
            a = a.right
          elem.key = a.key
          elem.value = a.value
          elem.left = del_elem(elem.left, elem.key)
          return elem
        elif elem.left:
          return elem.left
        else:
          return elem.right

    self.head = del_elem(self.head, key)
    self.length -= 1

  def __len__(self):
    return  self.length

  def __iter__(self):
    self.a = self
    return self

  def __next__(self):
    if self.length > 0:
      b = self.a.head
      while b.left:
        b = b.left
      del self.a[b.key]
      return b.key, b.value
    print(self.a)
    raise StopIteration


