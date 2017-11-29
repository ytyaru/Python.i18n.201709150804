#!python3.6
import gettext
import os
gettext.install('hello', os.path.join(os.path.dirname(__file__)))
print(_('Hello World !!'))

langs = ['ja', 'en', 'de']
lang = 'ja'
while lang:
    print(f'言語コードを入力してください(未入力+Enterで終了) {langs}: ', end='')
    lang = input()
    if lang not in langs: continue
    l = gettext.translation('hello', os.path.join(os.path.dirname(__file__)), languages=[lang])
    l.install()
    print(_('Welcome i18n !!'))
