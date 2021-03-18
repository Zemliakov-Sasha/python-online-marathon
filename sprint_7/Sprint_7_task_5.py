from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    def __init__(self):
        self.name = None

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def showDetails(self) -> str:
        pass


class LeafElement(Component, ABC):

    def __init__(self, args):
        """Takes the first positional argument and assigns to member variable "position"."""
        self.name = args

    def showDetails(self):
        """Prints the position of the child element."""
        print(f"\\t\\t{self.name}")


class CompositeElement(Component, ABC):

    def __init__(self, args):
        """Takes the first positional argument and assigns to member
         variable "position". Initializes a list of children elements."""
        self.name = args
        self._children: List[Component] = []


    def add(self, component: Component):
        """Adds the supplied child element to the list of children
         elements "children"."""
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component):
        """Removes the supplied child element from the list of
        children elements "children"."""
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def showDetails(self):
        """Prints the details of the component element first. Then,
        iterates over each of its children, prints their details by
        calling their showDetails() method."""
        results = []
        print(self.name)
        for child in self._children:
            if child.parent and child.name[:3] != "\\t\\t":
                child.name = "\\t" + child.name
            results.append(child.showDetails())


topLevelMenu = CompositeElement("GeneralManager")
subMenuItem1 = CompositeElement("Manager1")
subMenuItem2 = CompositeElement("Manager2")
subMenuItem11 = LeafElement("Developer11")
subMenuItem12 = LeafElement("Developer12")
subMenuItem21 = LeafElement("Developer21")
subMenuItem22 = LeafElement("Developer22")
subMenuItem1.add(subMenuItem11)
subMenuItem1.add(subMenuItem12)
subMenuItem2.add(subMenuItem22)
subMenuItem2.add(subMenuItem22)
topLevelMenu.add(subMenuItem1)
topLevelMenu.add(subMenuItem2)
topLevelMenu.showDetails()
