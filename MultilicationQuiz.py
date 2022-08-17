import pyinputplus as pyip
import random, time

Numberofquestion=10
Correctanswer=0
for question in range(Numberofquestion+1):
    num1= int(random.randint(1,9))
    num2= int(random.randint(1,9))
    ques= num1 * num2
    prompt = " Câu hỏi số %d: %d x %d" %(question, num1, num2)
    print(prompt)
    answer =pyip.inputInt(timeout=5)
    if answer == ques:
        Correctanswer += 1
        print("Corect!")
        time.sleep(1.0)
        continue
    if answer != ques:
        print("Wrong!")
        time.sleep(1.0)
        print("Kết quả đúng là: ",ques)
        continue
print("Số câu trả lời đúng là:", Correctanswer)

"""
 except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
"""
