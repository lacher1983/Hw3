class OpticalCable:
    """Класс для оптисания оптического кабеля"""
    
    def __init__(self, lenght, diameter):
        """Конструктор класса - вызывается при создании нового объекта
        lenght - длина кабеля в метрах
        diameter - диаметр кабеля в мм
        """
        self.lenght = lenght # Создаем поле length и сохраняем переданное значение
        self.diameter = diameter # Создаем поле diameter и сохраняем переданное значение
    
    def show_spec(self):
        """Метод для отображения характеристик кабеля"""
        print(f"Характеристики кабеля")
        print(f"- Длина: {self.lenght} метров")
        print(f"- Диаметр: {self.diameter} мм")
 
# Создаем несколько объектов (разных кабелей)
cable1 = OpticalCable(1000, 5.7) #Кабель длиной 1000м и диаметром 5,7мм
cable2 = OpticalCable(4000, 6.8) #Кабель длиной 4000м и диаметром 6,8мм
 
# Выводим характеристики кабелей
cable1.show_spec()
print("---")
cable2.show_spec()
