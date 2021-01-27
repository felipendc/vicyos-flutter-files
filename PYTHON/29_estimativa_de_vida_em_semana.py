
idade = input("Qual é a sua idade atual?")


dias_do_ano = 365
semanas_do_ano = 52
meses_do_ano = 12

dias_totais = (dias_do_ano * 90) - (int(idade) * dias_do_ano)
semanas_totais = (semanas_do_ano * 90) - (int(idade) * semanas_do_ano)
anos_totais = (meses_do_ano * 90) - (int(idade) * meses_do_ano)

print(
    f"You have {dias_totais} days, {semanas_totais} weeks, and {anos_totais} months left.")


# Aqui está uma forma muito mais simples:
#     # 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# years = 90 - int(age)
# months = round(years * 12)
# weeks = round(years * 52)
# days = round(years * 365)

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")
