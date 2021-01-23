print("DOS-Betaを初期化します")
import os
open("store.ini","w")
s = open("config.ini","w")
s.write("""[Defalt]
application = True
Unsignedapplication = false
nostoreapp = 
appcmd = None""")



