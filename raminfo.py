import psutil

def get_size(bytes, suffix="B"):
	factor = 1024
	for unit in ["", "K" , "M" , "G" , "I" ,"P"]:
		if bytes < factor:
			return f"{bytes:.2f}{unit}{suffix}"
		bytes /= factor
"Abhishek Patel @imdarkcoder"
#get the memory details
svmen = psutil.virtual_memory()
print(f"Total: {get_size(svmen.total)}")
print(f"Available : {get_size(svmen.available)}")
print(f"Used : {get_size(svmen.used)}")
print(f"Percentage : {svmen.percent}%")
#get swap memory details if exists
swap =psutil.swap_memory()
print("\nSwap Partition:")
print(f"Total :{get_size(swap.total)}")
print(f"Free : {get_size(swap.free)}")
print(f"Used : {get_size(swap.used)}")
print(f"Percentage : {swap.percent}%")

#end code
