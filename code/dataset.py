from dataset import DataSetItem, DataSetInterface

class DataSet(DataSetInterface):
    """
    Diese Klasse implementiert das Interface DataSetInterface.
    """

    def __init__(self):
        """
        Initialisiert ein leeres DataSet.
        """
        super().__init__()
        self.items = {}

    def __setitem__(self, name: str, id_content: tuple[int, any]):
        """
        Hinzufügen oder Aktualisieren eines DataSetItems im DataSet.
        """
        self.items[name] = DataSetItem(name, id_content[0], id_content[1])

    def __iadd__(self, item: DataSetItem):
        """
        Hinzufügen eines DataSetItems.
        """
        self.items[item.name] = item
        return self

    def __delitem__(self, name: str):
        """
        Löscht ein DataSetItem anhand seines Namens.
        """
        if name in self.items:
            del self.items[name]

    def __contains__(self, name: str) -> bool:
        """
        Überprüfen, ob ein DataSetItem im DataSet enthalten ist.
        """
        return name in self.items

    def __getitem__(self, name: str) -> DataSetItem:
        """
        Abrufen eines DataSetItems anhand seines Namens.
        """
        if name in self.items:
            return self.items[name]
        raise KeyError(f"Item with name '{name}' not found.")

    def __and__(self, dataset: DataSetInterface) -> DataSetInterface:
        """
        Gibt ein neues DataSet zurück, das die Schnittmenge von zwei DataSets darstellt.
        """
        result = DataSet()
        for name, item in self.items.items():
            if name in dataset:
                result += item
        return result

    def __or__(self, dataset: DataSetInterface) -> DataSetInterface:
        """
        Gibt ein neues DataSet zurück, das die Vereinigung von zwei DataSets darstellt.
        """
        result = DataSet()
        result.items.update(self.items)
        for name, item in dataset.items():
            if name not in result:
                result += item
        return result

    def __iter__(self):
        """
        Ermöglicht die Iteration über das DataSet.
        """
        sorted_items = sorted(
            self.items.values(),
            key=lambda x: getattr(x, self.iterate_key),
            reverse=self.iterate_reversed
        ) if self.iterate_sorted else self.items.values()
        return iter(sorted_items)

    def filtered_iterate(self, filter_func):
        """
        Gefilterte Iteration über das DataSet.
        """
        for item in self:
            if filter_func(item.name, item.id):
                yield item

    def __len__(self) -> int:
        """
        Gibt die Anzahl der DataSetItems im DataSet zurück.
        """
        return len(self.items)
