def chk():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1mYour ID : "+id)
  try:
    httpCaht = requests.get("").text
    if id in httpCaht:
      print("\033[92mYOUR ID IS ACTIVE.........")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else:
      print("\x1b[91mBarezm Id kat active nya Tkaya bo Active krdn nama bnera bo telegram @S0_KI.......")
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == 'main':
     print(logo)
     chk()
   
chk()

print("HELLO WORLD")