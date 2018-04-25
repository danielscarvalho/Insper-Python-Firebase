from firebase import firebase

firebase = firebase.FirebaseApplication('https://advfb-7e80b.firebaseio.com/', None)

#Rules do Firebase SEM segurança para escrita... leitura livre...
#{
#  "rules": {
#    ".read":  true,
#    ".write": true
#  }
#}

#Rules do Firebase com segurança para escrita... leitura livre...
#{
#  "rules": {
#    ".read":  true,
#    ".write": "auth != null"
#  }
#}

#people = {"people":{{"user":"John Silver","value":100},
#                                         {"user":"Mary Cris"  ,"value":200}}}

#result = firebase.post('/users',   {'1': 'John Doe', '2': 'Jane Doe'}) # com rashcode
result = firebase.put('/users', "1",   {'1': 'John Doe'}) # sem rashcode
result = firebase.put('/users', "2",   {'2': 'Jane Doe'}) # sem rashcode, 
print (result)


