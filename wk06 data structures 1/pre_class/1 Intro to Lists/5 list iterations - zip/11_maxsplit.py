# Limiting Splits With Maxsplit
ip_address = '192.168.26.10'
print(ip_address.split(".", maxsplit=1))
print(ip_address.split(".", maxsplit=2))
print(ip_address.split(".", maxsplit=3))