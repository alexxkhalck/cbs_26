
if True:
    print("aaaa")

if False:
    print("aaaa")

class Emp():
    pass

employee = Emp()
employee.gender = "male"

print(employee.gender == "male")
print(employee.gender == "female")

years = 64
count = 0 
MAN_RETIMENT_AGE = 65
WOMAN_RETIMENT_AGE = 60

# if employee.gender == "male" and years >= MAN_RETIMENT_AGE:
#     count += 1
# elif employee.gender == "female" and years >= WOMAN_RETIMENT_AGE:
#     count += 1

if years >= MAN_RETIMENT_AGE:
    count += 1
elif years >= WOMAN_RETIMENT_AGE:
    count += 1

print(count)

employee.name = "Ivan"
employee.fam_name = "Obivan"

if employee.name == "Ivan" and employee.fam_name == "Obivan":
    count += 1
print(count)

if employee.name == "Ivan" and employee.fam_name == "Ivan":
    count += 1
print(count)

if employee.name == "Ivan" or employee.fam_name == "PobIvan":
    count += 1
print(count)

if all([employee.name == "Ivan",
        employee.fam_name == "Obivan"
    ]):
        count += 1
print(count)

if any([employee.name == "Ivan",
        employee.fam_name == "PobIvan"
    ]):
        count += 1
print(count)