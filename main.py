import sys
sys.dont_write_bytecode = True
import unicodedata
import datetime
import re
from create_information_session_date import create

def questions():
    try:
        # 説明会を開催しない日の設定を確認
        answer1 = input('【除外日程のファイルを修正しましたか？】（yes / no）：　')
        if answer1 == 'no' or not answer1 == 'yes':
            return print('\n【終了します】')

        # 説明会を開催する日の設定を確認
        answer2 = input('【特殊日程のファイルを修正しましたか？】（yes / no）：　')
        if answer2 == 'no' or not answer2 == 'yes':
            return print('\n【終了します】')

        # 作成対象年
        year = input('【何年の説明会日程を作成しますか？】：　')
        year = unicodedata.normalize('NFKC', year)
        if (
            not str(datetime.datetime.now().year) == str(year) and
            not str(datetime.datetime.now().year + 1) == str(year)
        ):
            return print('\n【正しい年を入力してください】')

        # 作成対象月
        month = input('【何月の説明会日程を作成しますか？】：　')
        month = unicodedata.normalize('NFKC', re.sub(r'^0+', '', month))
        if (
            not re.match(r'^(1[0-2]|[1-9])$', month) and
            not 1 <= int(month) <= 12
        ):
            return print('\n【正しい月を入力してください】')

        # 作成対象の確認
        input(f'【{year}年{month}月の説明会日程を作成します】：　【Enter】')

        # 説明会の自動生成処理実行
        create(int(year), int(month))
        print('\n【[./csv]ディレクトリのcsvをaipoにインポートしてください】')
    except KeyboardInterrupt:
        # 入力キャンセル時
        return print('\n\n【入力がキャンセルされました】')

# 対話式プロンプト開始
questions()