class CableOrder:
    """Класс для обработки заказов на кабель"""
    
    def __init__(self, *args):
        """
        Конструктор принимает аргументы впроизвольном порядке
        Возможные варианты:
        - тип кабеля и длина
        - длина и тип кабеля 
        - два числа (длина и диаметр)
        - две строки (тип и цвет)
        """
        # если оба аргумента числа - это длина и диаметр
        if len(args) == 2:
            if all(isinstance(arg, (int, float)) for arg in args):
                self.lenght = args[0]
                self.diameter = args[1]
                self.order_type = "Параметрический заказ"
            
            # если оба аргумента строки - это тип и цвет
            elif all(isinstance(arg, str) for arg in args):
                self.cable_type = args[0]
                self.color = args[1]
                self.order_type = "Стандартный заказ"
                
            # если один аргумент строка, а другой - число
            elif any(isinstance(arg, str) for arg in args) and any(isinstance(arg, (int, float)) for arg in args):
                for arg in args:
                    if isinstance(arg, str):
                        self.cable_type = args
                    else:
                        self.lenght = args
                self.order_type = "Комбинированный заказ"
                
    def show_order(self):
        """Метод для отображения информации о заказе"""
        print("\nИнформация о заказе:")
        print(f"Тип заказа: {self.order_type}")
        
        if hasattr(self, 'lenght'):
            print(f"Длина: {self.lenght} м")
        if hasattr(self, 'diameter'):
            print(f"Диаметр: {self.diameter} мм")
        if hasattr(self, 'cabel_type'):
            print(f"Тип кабеля: {self.cabel_type}")
        if hasattr(self, 'color'):
            print(f"Цвет: {self.color}")
 
# Создаем разные типы заказов
order1 = CableOrder("OM3", "синий") #Стандартный заказ
order2 = CableOrder(2000, 5.5) # Параметрический заказ
order3 = CableOrder("ОМ4", 1000) # Комбинированный заказ
order4 = CableOrder(1500, "красный") # Комбинированный заказ
 
# Выводим информацию о заказах
order1.show_order()
order2.show_order()
order3.show_order()
order4.show_order()
