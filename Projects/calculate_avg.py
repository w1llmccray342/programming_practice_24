class  Assignment:

    def __init__(self, name, weight):
        .__weight = weight
        .__name = name

    def __str__(self):
        return "{.__name} holds {.__weight}"
    
    