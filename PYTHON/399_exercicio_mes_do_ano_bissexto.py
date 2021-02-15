def ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def dias_no_mes(ano, mes):
    dias_do_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes > 12 or mes < 1:
        return "Você deve escolher entre o mês 1 até o mês 12."
    mes_selecionado = mes - 1
    ano_bissexto_resultado = ano_bissexto(ano)
    if ano_bissexto_resultado:
        dias_do_mes[1] = 29
        return dias_do_mes[mes_selecionado]
    else:
        return dias_do_mes[mes_selecionado]


ano = int(input("Digite um ano: "))
mes = int(input("Digite um mês: "))
dias = dias_no_mes(ano, mes)
print(dias)


########################################################
###### OUTRA MANEIRA DE ESCREVER O MESMO CÓDIGO ########

# def is_leap(year):
#       if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#         return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if month > 12 or month < 1:
#     return "Invalid month entered."
#   if month == 2 and is_leap(year):
#     return 29
#   return month_days[month - 1]


# #Do NOT change any of the code below 👇
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
