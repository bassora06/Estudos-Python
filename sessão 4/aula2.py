from datetime import datetime
from pytz import timezone

agora = datetime.now()
agoraTokyo = datetime.now(timezone('Asia/Tokyo'))

diretiva = '%d / %m / %Y'

print(datetime.strftime(agora, diretiva))
print(agoraTokyo)

