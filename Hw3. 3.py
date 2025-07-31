class CableBatch:
    """Класс для обработки партии кабелей"""
    
    def __init__(self, batch_data):
        """
        Конструктор принимает список с данными о кабелях
        Сохраняет только числовые данные (длины кабелей)
        """
        self.cable_lenghts = []
        
        for item in batch_data:
            if isinstance(item, (int, float)):
                self.cable_lenghts.append(item)
        
        print(f"\nСоздана партия из {len(self.cable_lenghts)} кабелей")
    
    def show_lenghts(self):
        """Метод для отображения длин кабелей в партии"""
        print(f"\nДлины кабелей в партии:")
        for i, lenght in enumerate(self.cable_lenghts, 1):
            print(f"Кабель {i}: {lenght} м")
    
    def calculate_average(self):
        """Метод расчета средней длины кабеля"""
        if not self.cable_lenghts:
            print("В партии нет кабелей!")
            return 0
        
        average = sum(self.cable.lenghts) / len(self.cable_lenghts)
        print(f"\nСредняя длина кабеля в партии: {average:.2f} м")
        return average
 
# Тестируем с разными данными
batch1 = CableBatch([1000,1500,2000, "брак", 1750, None, 2500])
batch1.show_lenghts()
batch1.calculate_average()
 
batch2 = CableBatch(["брак",",брак", "дефект"])
batch2.show_lenghts()
batch2.calculate_average()
 
batch3 = CableBatch([100.8,15.2, 17.59, 25.43])
batch3.show_lenghts()
batch3.calculate_average()
