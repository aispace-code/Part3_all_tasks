# # Попросить пользователя ввести текст. В результате вывести процент букв в верхнем
# # регистре (заглавные) и в нижнем регистре (прописные).

name = (input("Enter any word ")).replace(' ', '')
lower_letter = 0
upper_letter = 0
length = len(name)

for i in name:
      if(i.islower()):
            lower_letter = lower_letter+1
      elif(i.isupper()):
            upper_letter = upper_letter+1

letters = lower_letter + upper_letter

per_lower = lower_letter / letters * 100
per_upper = upper_letter / letters * 100
print("Lower: %.2f%%" % per_lower)
print("Upper: %.2f%%" % per_upper)

