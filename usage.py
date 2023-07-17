import re

fp = open("usage.txt", "r")
text = fp.read()
fp.close()

pattern = r'carts-5bb979cb6d-gfhk5\s+(\d+m)\s+[0-9]*Mi'
matchs = re.findall(pattern, text)
cart_cpu_value = [int(match[:-1]) for match in matchs]

pattern = r'carts-5bb979cb6d-gfhk5\s+[0-9]*m\s+(\d+Mi)'
matchs = re.findall(pattern, text)
cart_memory_value = [int(match[:-2]) for match in matchs]

pattern = r'carts-db-98ff4cbc7-6p7gl\s+(\d+m)\s+[0-9]*Mi'
matchs = re.findall(pattern, text)
cart_db_cpu_value = [int(match[:-1]) for match in matchs]

pattern = r'carts-db-98ff4cbc7-6p7gl\s+[0-9]*m\s+(\d+Mi)'
matchs = re.findall(pattern, text)
cart_db_memory_value = [int(match[:-2]) for match in matchs]

pattern = r'orders-d5f745cc6-shf4d\s+(\d+m)\s+[0-9]*Mi'
matchs = re.findall(pattern, text)
order_cpu_value = [int(match[:-1]) for match in matchs]

pattern = r'orders-d5f745cc6-shf4d\s+[0-9]*m\s+(\d+Mi)'
matchs = re.findall(pattern, text)
order_memory_value = [int(match[:-2]) for match in matchs]

pattern = r'orders-db-c6897fc87-t44jc\s+(\d+m)\s+[0-9]*Mi'
matchs = re.findall(pattern, text)
order_db_cpu_value = [int(match[:-1]) for match in matchs]

pattern = r'orders-db-c6897fc87-t44jc\s+[0-9]*m\s+(\d+Mi)'
matchs = re.findall(pattern, text)
order_db_memory_value = [int(match[:-2]) for match in matchs]

pattern2 = r'[0-9]*:[0-9]*:[0-9]*'
timestamp = re.findall(pattern2, text)

length = len(timestamp)

fp = open("unchi.csv", "w")
fp.write("timestamp,cart_CPU,cart_db_CPU,order_CPU,order_db_CPU,cart_memory,cart_db_memory,order_memory,order_db_memory\n")
for i in range(length):
    fp.write(timestamp[i] + ',')
    fp.write(str(cart_cpu_value[i]) + ',')
    fp.write(str(cart_db_cpu_value[i]) + ',')
    fp.write(str(order_cpu_value[i]) + ',')
    fp.write(str(order_db_cpu_value[i]) + ',')
    fp.write(str(cart_memory_value[i]) + ',')
    fp.write(str(cart_db_memory_value[i]) + ',')
    fp.write(str(order_memory_value[i]) + ',')
    fp.write(str(order_db_memory_value[i]) + '\n')
fp.close()