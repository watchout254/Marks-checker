print("\t\t\t\t\t\t\tWELCOME TO JAWABU SCHOOLS\n")
print("\t\tConfirm your KCPE marks.")

name = input("Your name: ")

print("Kindly enter enter your marks in the following subjects:  ")
maths = int(input("Maths: "))
eng = int(input("Eng: "))
kis = int(input("Kis: "))
sci = int(input("Science: "))
creSs = int(input("S/sCre: "))

total = maths+eng+kis+sci+creSs
mean = int(total/5)

totalMarks = print(f"Your total marks is {total}\n")
totalMean = print(f"Your mean is: {mean}\n")

if total >= 400:
    print("😍😍CONGRATULATIONS 😍😍")
    print("You will go to a national school")
    print(f"1. ALLIANCE HIGH SCHOOL\n"
          f"2. MOI HIGH SCHOOL KABARAK\n"
          f"3. KAPSABET BOYS\n"
          f"4. MASENO SCHOOL\n"
          f"5. CHAVAKALI HIGH SCHOOL\n"
          f"6. MARYHILL GIRLS HIGH SCHOOL\n"
          f"7. THE KENYA HIGH SCHOOL\n"
          f"8. NAIROBI SCHOOL\n"
          f"9. ST.ANTHONY'S BOYS' HIGH SCHOOL - KITALE\n"
          f"10. STAREHE BOYS' CENTRE & SCHOOL\n")
    print("To see more click 👉https://teacher.co.ke/list-of-national-school-in-kenya-according-to-clusters/")
elif total >= 300:
    print("😊😊WELL DONE😊😊")
    print("You will go to a county or an extra county school")
    print("Click here to view 👉https://educationnewshub.co.ke/new-list-of-all-the-extra-county-secondary-schools-in-kenya-school-code-type-cluster-and-category/#:~:text=Extra%20County%20Schools%20in%20Kenya,from%20all%20over%20the%20country.")
else:
    print("🙂🙂GOOD🙂🙂")
    print("You tried, you will go a school of your choice")
    print("Click here to view 👉https://newsblaze.co.ke/full-list-of-all-county-secondary-schools-in-kenya-school-code-name-location-and-other-details/ ")


print("\t\tFeel free to visit our app again\n")






