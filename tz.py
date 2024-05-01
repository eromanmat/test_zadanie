

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
        # Преобразуем операнды в целые числа
        num1 = float(operand1)
        num2 = float(operand2)

        # Проверяем, что числа от 1 до 10
        if not (1 <= num1 <= 10 and 1 <= num2 <= 10):
            return "Invalid numbers: Must be between 1 and 10"

        # Выполняем арифметическую операцию в зависимости от оператора
        if operator == '+':
            result = int(num1 + num2)
        elif operator == '-':
            result = int(num1 - num2)
        elif operator == '*':
            result = int(num1 * num2)
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero"
            result = int(num1 / num2)  # целочисленное деление
        else:
            return "Invalid operator"

        # Возвращаем результат в виде строки
        return str(result)

    except ValueError:
        return "Invalid operands"

# Пример использования
expression = "7.5 / 3"
result = main(expression)
print("Output:", result)  # Output: "3"

