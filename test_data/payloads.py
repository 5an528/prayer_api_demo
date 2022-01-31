import json


time = json.dumps({
    "city": "dhaka"
})
create = json.dumps({
    "name": "morpheus",
    "job": "leader"
})

user_to_register = json.dumps({
    "email": "eve.holt@reqres.in",
    "password": "pistol"
})

only_email = json.dumps({
    "email": "eve.holt@reqres.in"
})

only_password = json.dumps({
    "password": "34534kjl53k45#"
})

user_to_login = json.dumps({
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
})

invalid_login_detail = json.dumps({
    "email": "sompod123@gmail.com",
})

ajan = {
    "city": "kolkata"
}