# セミナー前昼食日程設定
def get_lunch_settings():
    return {
        # 【共通設定】
        'common': {
            'title': '【カレッジセミナー】スピーカー準備/昼食', # 予定の名称を設定
            'content': '■スピーカー：', # 予定の内容を設定
            'header': ['開始日', '開始時刻', '終了日', '終了時刻', '場所', '予定', '内容', '名前', 'メールアドレス']
        },

        # 火曜日、木曜日、(金曜日)の設定
        'pattern_a': {
            'seminar_start': '12:00', # 開始時間
            'seminar_end': '12:30', # 終了時間
            'speaker': [  # スピーカー（配列）
                {
                    'name': '阿部 倫子',
                    'email': 'r.abe@internous.co.jp',
                },
            ],
        },
    }