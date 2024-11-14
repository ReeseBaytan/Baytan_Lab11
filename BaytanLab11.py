Salita = []
for user in range(10):
    pogi_ako = input(f"Mag lagay ng salita {user + 1}: ")
    Salita.append(pogi_ako)
 
while True:   
    length = input("Lagay mo kung ilan letter gusto mo: ")
    if length.isdigit():
        length = int(length)
        break
    else:
        print("Bawal tong nilagay mo lods.")
        
combine = [pogi_ko for pogi_ko in Salita if len(pogi_ko) == length]

if combine: 
    print("Mga salitang may haba ng kung anong number ang ilagay mo:", ', '.join(combine))
else:
    print("Walang salitang nakuha.")
        
        