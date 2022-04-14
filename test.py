import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


database_url = 'https://test-project-ceef3-default-rtdb.firebaseio.com/'

cred = credentials.Certificate("dbkey.json")
firebase_admin.initialize_app(
    cred,
    {'databaseURL': database_url}
)

"""
Добавление в базу

ref = db.reference("/")
ref.set(
    {
	"Test": 0
    }
)
"""
"""
Удаление из базы
ref = db.reference("/")
ref.child("Test").set({})
"""

"""
Редактирование
ref = db.reference("/Books/Best_Sellers/")
best_sellers = ref.get()
print(best_sellers)
for key, value in best_sellers.items():
	if(value["Author"] == "J.R.R. Tolkien"):
		value["Price"] = 90
		ref.child(key).update({"Price":80})
"""

"""
ref = db.reference("/")
ref.set({
    "countries": ['Russia', 'United States']
})
"""

ref = db.reference("/countries/")
countries = ref.get()
print(countries)
countries.append('Great Britain')
ref = db.reference("/")
ref.update({"countries":countries})
