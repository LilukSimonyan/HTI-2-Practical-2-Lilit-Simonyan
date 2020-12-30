s = input('Enter the word: ')
# էսքան հատվածն ավելորդ էր
# if len(s) == 1:
#     print('Yes')
# elif len(s) == 2:
#     if s[0] != s[1]:
#         print('No')
#     else:
#         print('Yes')
# else:
first = 0
last = len(s) - 1
while first < last:
    if s[first] == s[last]:
        first = first + 1
        last = last - 1
        print('Yes')
    else:
        print('No')
        break
        # ես գիտեմ, որ սխալ կա մեջը, s[first] == s[last] դեպքում
        # բերում է, բոլոր ելքերը (և yes, և no, օրինակ abccda input-ի դեպքում),
        # իսկ ինձ պետք է, որ եթե թեկուզ մեկ false կա տպի No
        # կուղղեմ, բայց գիտեմ երբ :-)
        # հուշում կանե՞ք

