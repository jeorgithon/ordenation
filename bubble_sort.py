class Bubble:
    @staticmethod
    def bubble_sort(vector: list) -> list:
        for i in range(1, len(vector)):
            for j in range(len(vector)-i):
                if vector[j] > vector[j+1]:
                    aux = vector[j]
                    vector[j] = vector[j+1]
                    vector[j+1] = aux
        return vector