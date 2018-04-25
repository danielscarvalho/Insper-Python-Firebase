from firebase import firebase

# pip install requests
# pip install python-firebase

firebase = firebase.FirebaseApplication('https://advfb-7e80b.firebaseio.com/', None)
result = firebase.get('peopleData', 0)
print (result)


