# create an user
curl -X POST -H "Content-Type: application/json" -d '{"email": "shunakano@test.com", "password": "abc"}' 127.0.0.1:3000/users/