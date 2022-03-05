seg = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = seg // 86400
rest_dia = seg % 86400
horas = rest_dia // 3600
seg_rest = rest_dia % 3600
minutos = seg_rest//60
seg_rest_final = seg_rest%60
print(dias,"dias,",horas,"horas,",minutos, "minutos e",seg_rest_final,"segundos.")