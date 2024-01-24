# セミナー日程設定
def get_seminar_settings():
    return {
        # 【共通設定】
        'common': {
            'title': 'カレッジセミナー【説明会】', # 予定の名称を設定
            'content': '■スピーカー：', # 予定の内容を設定
            'header': ['開始日', '開始時刻', '終了日', '終了時刻', '場所', '予定', '内容', '名前', 'メールアドレス']
        },

        # 月曜日、水曜日の設定
        'pattern_a': {
            'seminar_start': '19:30', # 開始時間
            'seminar_end': '20:30', # 終了時間
            'speaker': [  # スピーカー（配列）
                {
                    'name': '山口 良',
                    'email': 'r.yamaguchi@internous.co.jp',
                },
                {
                    'name': '金子 聖',
                    'email': 'a.kaneko@internous.co.jp',
                }
            ],
        },

        # 火曜日、木曜日、金曜日の設定
        'pattern_b': {
            'seminar_start': '13:00', # 開始時間
            'seminar_end': '14:00', # 終了時間
            'speaker': [  # スピーカー（配列）
                {
                    'name': '阿部 倫子',
                    'email': 'r.abe@internous.co.jp',
                }
            ],
        },

        # 土曜日の設定（手動で設定しているためコメントアウト）
        # 'pattern_d': {
        #     'seminar_start': '11:00',
        #     'seminar_end': '12:00',
        #     'is_odd_weeks': True, # 奇数週のみの開催かTrueかFalse(金曜日、土曜日のみ)
        #     'is_even_weeks': False, # 偶数週のみの開催かTrueかFalse(金曜日、土曜日のみ)
        #     'speaker': [
        #         {
        #             'name': '阿部倫子',
        #             'email': 'r.abe@internous.co.jp',
        #         }
        #     ],
        # },
    }