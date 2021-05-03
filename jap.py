import os
import codecs
from datetime import datetime as dt

puncList = ['！', '？', '。', '、', '『', '』']
# print(chr(12353)) ~ print(chr(12543))

retType = 0
while retType<1 or retType>3:
    retType = input('1. 日本語(にほんご)➔\t日本語\n\n' + 
                    '2. 日本語(にほんご)➔\tにほんご\n\n' + 
                    '                    \tに ほん ご\n' +
                    '3. 日本語(にほんご)➔\t日  本  語 (as html)\n>> ')
    try:
        retType = int(retType.split('.')[0])
    except ValueError:
        retType = 0

text = input('Text：\n')

if retType==1:
    ans = ''
    status = True
    for i in text:
        if status:
            if i=='(':
                status = False
            else:
                ans+=str(i)
        else:
            if i==')':
                status = True

    print(ans)

    name = '[{}]JapanTranslateor.txt'.format(dt.now().strftime('%Y-%m-%d'))
    file = codecs.open(name, 'w', encoding='utf-8')
    file.write(ans)
    file.close()

    os.system('start {}'.format(name))

elif retType==2:
    # puncList = ['！', '？', '。', '、', '『', '』']
    # print(chr(12353)) ~ print(chr(12543))

    ans = ''
    for i in text:
        if ord(i) >= 12353 and ord(i)<=12543 or i in puncList:
            ans+=i

    print(ans)

    name = '[{}]JapanTranslateor.txt'.format(dt.now().strftime('%Y-%m-%d'))
    file = codecs.open(name, 'w', encoding='utf-8')
    file.write(ans)
    file.close()

    os.system('start {}'.format(name))

elif retType==3:
    # puncList = ['！', '？', '。', '、', '『', '』']
    # print(chr(12353)) ~ print(chr(12543))

    ans = '<div>\n\t'
    kannji = ''
    hiragana = ''
    status = True

    for i in text:
        if status:
            if (ord(i) >= 12353 and ord(i)<=12543) or i in puncList:
                ans+=i
            elif i=='(':
                status = False
            else:
                kannji+=i
            if i=='。':
                ans+='\n\t<br>\n\t<br>\n\t'
        else:
            if i==')':
                status = True
                ans+= ( '\n' + 
                        '\t<ruby>\n' + 
                        '\t\t<rb>{}</rb>\n'.format(kannji) + 
                        '\t\t<rt>{}</rt>\n'.format(hiragana) + 
                        '\t</ruby>\n\t' )
                kannji = ''
                hiragana = ''
            else:
                hiragana += i

    ans += '\n</div>'

    ans = '<div lang="ja" id="divResult" style="font-size:28px;">\n' + ans + '\n</div>'
    print(ans)
    name = '[{}]JapanTranslateor.html'.format(dt.now().strftime('%Y-%m-%d'))
    file = codecs.open(name, 'w', encoding='utf-8')
    file.write(ans)
    file.close()

    os.system('start {}'.format(name))


