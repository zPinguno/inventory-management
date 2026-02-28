from enum import Enum


class ItemState(Enum):
    USED = "Gebraucht"
    FIXING = "In Reparatur"
    ORDERED = "Bestellt"
    RETIRED = "Ausgemustert"
    BORROWED = "Verliehen"
    DELIVERED = "Geliefert"
    PROJECTED = "Geplant"
    REQUESTED = "Angefordert"


def normalizeText(text: str) -> ItemState:
    if isinstance(text, ItemState):
        return text

    for state in ItemState:
        if state.value.lower() == str(text).lower():
            return state

    return ItemState.USED


def normalizeItems(items: list) -> list:
    for item in items:
        if not isinstance(item.state, ItemState):
            item.state = normalizeText(item.state)
    return items

def getAllStates():
    states = list()
    for state in ItemState:
        states.append(state)
    return states
def getAllStatesAsText():
    states = list()
    for state in ItemState:
        states.append(state.value)
    return states