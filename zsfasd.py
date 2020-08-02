import random
dig = random.randint(1, 100)
print("Шалом, тут угадывают числа, хочешь попробовать? От 1 до 100")

def valid_ok(num):
    num = int(num)
    if 0 < num < 101:
        return True
    else:
        return False

def main():
    count = 0
    while True:
        count += 1
        b = input("Какое число я загадал?")
        if valid_ok(int(b)) == True:
            if int(b) > dig:
                print('Слишком много хочешь')
            elif int(b) < dig:
                print('Слабо берешь, мысли шире')
            if int(b) == dig:
                print("Думаешь угадал? Получается, что так.")
                print("Количество попыток :", count)
                break
        else:
            print("Ты шо, самый умный?")


ok = input("да или нет?").lower()
if ok == "да" or ok == "yes" or ok == "da":
    main()

elif ok == "нет" or ok == "no" or ok == "net":
    print("Тогда arividrochi, бродяга.")

else:
    print("Внимание, вы не прошли тест на натурала, прощайте.")

while True:
    print("Хочешь еще разок затраить?")
    answer = input("да или нет?").lower()
    if answer == "да" or answer == "yes" or answer == "da":
        dig = random.randint(1, 100)
        main()
        continue
    else:
        print("ЧАО КАКАО!")
        break