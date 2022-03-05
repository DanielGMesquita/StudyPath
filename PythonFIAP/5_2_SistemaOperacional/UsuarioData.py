import getpass
from datetime import datetime

print('Usuário: ', getpass.getuser())
print('Data completa: ', datetime.now())
print('Dia: ', datetime.now().day)
print('Mês: ', datetime.now().month)
print('Ano: ', datetime.now().year)
# hour, minute and second