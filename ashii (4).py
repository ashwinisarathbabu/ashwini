id = input("Enter employee ID:")
name = input("Enter name:")
salary = float(input("Enter basic salary:"))


allowance = salary * 0.30
deducation = salary * 0.10
net_salary = salary + allowance - deducation


print("\nEnployee details")
print("ID:",id)
print("Name:",name)
print("Basic salary:",salary)
print("allowance:",allowance)
print("deducation:",deducation)
print("Net salary:",net_salary)


