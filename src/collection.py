import uuid
from recept import Recept

class Collection:
    """
    Object that represents a collection of objects of a particular class.
    Acts as a dictionary with predefined type of value.
    :params: _type      type the value should belong to, type
    :params: _content   dictionary itself
    """
    def __init__(self, t=Recept) -> None:
        self._type = t
        self._content = {}

    def add(self, el:Recept, label)-> None:
        """
        Function that adds given object to the collection.
        :params: obj        object to add, Recept or another class object, same as collection's type
        :params: label      dictionary key, in this case deepsort detection label, int
        returns: None
        """
        assert isinstance(el, self._type), "element does not belong to the correct collection class {}".format(self._type)
        
        self._content[label] = el

    def remove(self, label)-> None:
        """
        Function that removes a record from the collection by label
        :params: label      dictionary key, in this case deepsort detection label, int
        returns: None
        """
        if label in self._content:
            del self._content[label]
        
    def get_id(self, label)-> uuid.UUID:
        """
        Function that gets the id of the element by its label.
        :params: label      dictionary key, in this case deepsort detection label, int
        returns: id         id of the element with the given label or None if the label is not
                            in the collection, UUID
        """
        if label in self._content:
            return self._content[label].id 

    @property
    def length(self) -> int:
        """
        Function that counts the length of the collection.
        returns: length         number of elements in the collection, int
        """
        return len(self._content)

    @property
    def ids(self) -> list:
        """
        Function that returns objects' ids.
        returns: ids            ids of elements in the collection, list of UUID
        """
        return [el.id for el in self._content.values()]

    
    def contains(self, label) -> bool:
        """
        Function that checks whether an element with such label exists in 
        the collection.
        :params: label      dictionary key, in this case deepsort detection label, int
        returns: check      result, whether an object exists in the collection, bool
        """
        return label in self._content