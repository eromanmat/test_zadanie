

def main(input_str):
    # Разделяем строку на части, чтобы получить операнды и оператор
    parts = input_str.split()
    
    # Убеждаемся, что строка содержит три части (число, оператор, число)
    if len(parts) != 3:
        return "Invalid input"

    # Извлекаем операнды и оператор
    operand1 = parts[0]
    operator = parts[1]
    operand2 = parts[2]

    try:
        # Преобразуем операнды в числа (float для работы с десятичными)
        num1 = float(operand1)
        num2 = float(operand2)

        # Выполняем арифметическую операцию в зависимости от оператора
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero"
            result = num1 / num2
        else:
            return "Invalid operator"

        # Возвращаем результат в виде строки
        return str(result)

    except ValueError:
        return "Invalid operands"

# Пример использования
expression = "12 / 4"
result = main(expression)
print(result)  
