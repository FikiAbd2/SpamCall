import os


os.system('clear')

os.system('termux-open-url https://youtube.com/channel/UC-6Ce1GVQ8nlnUEJ8PUEF-A')
dat = {"method": "CALL","countryCode": "id",}

for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" [•] Status ~+> ",(send.json()["message"]))