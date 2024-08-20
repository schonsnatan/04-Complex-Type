from typing import Dict, Tuple

CONSTANTE_BONUS = 1000

def validate_name(name: str) -> None:
    if len(name) == 0:
        raise ValueError("Please provide a name")
    elif any(char.isdigit() for char in name):
        raise ValueError("Your name must have only letters")
    elif name.isspace():
        raise ValueError("Please type something")

def validate_salary(sal: float) -> None:
    if sal <= 0:
        raise ValueError("Inform a positive and non-zero value")

def validate_bonus(bonus: float) -> None:
    if bonus < 0:
        raise ValueError("Inform a positive bonus.")

def request_data() -> Dict[str, float]:
    data = {}
    
    while True:
        try:
            # Solicita o nome do usuário
            name = input("Please enter your name: ")
            validate_name(name)
            data['name'] = name
            break
        except ValueError as e:
            print(f"Error: {e}. Please take a look into the instructions.")
    
    while True:
        try:
            # Solicita o salário do usuário
            sal = float(input("Please enter your salary: "))
            validate_salary(sal)
            data['salary'] = sal
            break
        except ValueError as e:
            print(f"Error: {e}. Please take a look into the instructions.")
    
    while True:
        try:
            # Solicita o valor do bônus do usuário
            bonus = float(input("Please enter your bonus percentage (e.g., 0.05 for 5%): "))
            validate_bonus(bonus)
            data['bonus'] = bonus
            break
        except ValueError as e:
            print(f"Error: {e}. Please take a look into the instructions.")
    
    return data

def process_data(data: Dict[str, float]) -> Tuple[float, float]:
    sal = data['salary']
    bonus = data['bonus']
    
    final_bonus = CONSTANTE_BONUS + sal * bonus
    kpi = (sal + final_bonus) / 1000
    
    return kpi, final_bonus

def print_summary(name: str, sal: float, final_bonus: float, kpi: float) -> None:
    print(f"Your KPI is: {kpi:.2f}")
    print(f"{name}, your salary is ${sal:.2f} and your final bonus is ${final_bonus:.2f}")

def main() -> None:
    data = request_data()
    kpi, final_bonus = process_data(data)
    print_summary(data['name'], data['salary'], final_bonus, kpi)

# Executa a função principal
main()
