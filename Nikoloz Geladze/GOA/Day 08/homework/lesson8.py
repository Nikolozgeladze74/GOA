squats_target = 150
pushups_target = 100

completed_squat = int(input("how many squat did you made?: "))
completed_pushups = int(input("how many pushups did you made?: "))

print(squats_target <= completed_squat and pushups_target <= completed_pushups)
print(squats_target == completed_squat and pushups_target == completed_pushups)

i = completed_pushups
if i >= 100:
    print("you won!")
else:
    print("you failed!")

i = completed_squat
if i >=150:
    print("you won!")
else:
    print("you failed!")