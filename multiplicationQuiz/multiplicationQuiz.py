import pyinputplus as pyip
import time
import random

NUMBER_OF_QUESTIONS = 10
correct_answers = 0
for questionNumber in range(NUMBER_OF_QUESTIONS):
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)

    prompt = f'#{questionNumber}: {num_1} x {num_2} = '
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num_1 * num_2)],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Ouy of tries!')
    else:
        print('Correct!')
        correct_answers += 1
        time.sleep(1)
print(f'Score: {correct_answers} / {NUMBER_OF_QUESTIONS}')
