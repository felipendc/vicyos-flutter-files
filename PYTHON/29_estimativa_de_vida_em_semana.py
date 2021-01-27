# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

dias_do_ano = 365
semanas_do_ano = 52
meses_do_ano = 12

dias_totais = (dias_do_ano * 90) - (int(age) * dias_do_ano)
semanas_totais = (semanas_do_ano * 90) - (int(age) * semanas_do_ano)
anos_totais = (meses_do_ano * 90) - (int(age) * meses_do_ano)

print(
    f"You have {dias_totais} days, {semanas_totais} weeks, and {anos_totais} months left.")
