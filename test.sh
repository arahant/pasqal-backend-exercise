DEVICE_TYPE1=typ1
DEVICE_TYPE2=typ2
PORT=5000

# Adding devices
curl localhost:${PORT}/devices -d "{\"id\": \"dev-42\", \"address\": \"addr1\", \"type\": \"${DEVICE_TYPE1}\", \"size\": 1000}"
curl localhost:${PORT}/devices -d "{\"id\": \"dev-43\", \"address\": \"addr2\", \"type\": \"${DEVICE_TYPE2}\", \"size\": 500}"

# Pushing jobs
curl localhost:${PORT}/jobs -d "{\"id\": \"job-3301\", \"priority\": 31, \"user_id\": \"uid1\", \"program_id\": \"prog11\",  \"device_type\": \"${DEVICE_TYPE2}\"}"
curl localhost:${PORT}/jobs -d "{\"id\": \"job-9973\", \"priority\": 31, \"user_id\": \"uid2\", \"program_id\": \"prog22\",  \"device_type\": \"${DEVICE_TYPE1}\"}"
curl localhost:${PORT}/jobs -d "{\"id\": \"job-9974\", \"priority\": 31, \"user_id\": \"uid2\", \"program_id\": \"prog22\",  \"device_type\": \"${DEVICE_TYPE1}\"}"
curl localhost:${PORT}/jobs -d "{\"id\": \"job-3302\", \"priority\": 31, \"user_id\": \"uid3\", \"program_id\": \"prog33\",  \"device_type\": \"${DEVICE_TYPE2}\"}"
