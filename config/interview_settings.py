# 個別面談日程設定
def get_interview_settings():
    return {
        # 【共通設定】
        'common': {
            'title': 'カレッジ個別面談【説明会】', # 予定の名称を設定
            'header': ['開始日', '開始時刻', '終了日', '終了時刻', '場所', '予定', '内容', '名前', 'メールアドレス']
        },

        # 月曜日、水曜日の設定
        'pattern_a': {
            'seminar_start': '20:30', # 開始時間
            'seminar_end': '21:30', # 終了時間
            'users': [
                '山口 良',
                '金子 聖',
                '阿部 倫子',
                '加藤 憲康',
                '大井 雄介',
                '富永 達彦',
            ],
            'email': [
                'r.yamaguchi@internous.co.jp',
                'a.kaneko@internous.co.jp',
                'r.abe@internous.co.jp',
                'katoh@internous.co.jp',
                'y.ooi@internous.co.jp',
                't.tominaga@internous.co.jp',
            ],
        },

        # 火曜日、木曜日、金曜日の設定
        'pattern_b': {
            'seminar_start': '14:00', # 開始時間
            'seminar_end': '15:00', # 終了時間
            'users': [
                '山口 良',
                '金子 聖',
                '阿部 倫子',
                '加藤 憲康',
                '大井 雄介',
                '富永 達彦',
                '松山 光', #　昼のみ
                '井上 彩楓', #　昼のみ
            ],
            'email': [
                'r.yamaguchi@internous.co.jp',
                'a.kaneko@internous.co.jp',
                'r.abe@internous.co.jp',
                'katoh@internous.co.jp',
                'y.ooi@internous.co.jp',
                't.tominaga@internous.co.jp',
                'h.matsuyama@internous.co.jp', #　昼のみ
                's.inoue@internous.co.jp', #　昼のみ
            ],
        },

        # 土曜日の設定（手動で設定しているためコメントアウト）
        # 'pattern_c': {
        #     'seminar_start': '12:00',
        #     'seminar_end': '13:00',
        #     'is_odd_weeks': True, # 奇数週のみの開催かTrueかFalse(金曜日、土曜日のみ)
        #     'users': [
        #             '山口 良',
        #             '金子 聖',
        #             '阿部倫子',
        #             '加藤 憲康',
        #             '大井雄介',
        #             '富永達彦',
        #             '松山 光', #　昼のみ
        #             '井上彩楓', #　昼のみ
        #         ],
        #         'email': [
        #             'r.yamaguchi@internous.co.jp',
        #             'a.kaneko@internous.co.jp',
        #             'r.abe@internous.co.jp',
        #             'katoh@internous.co.jp',
        #             'y.ooi@internous.co.jp',
        #             't.tominaga@internous.co.jp',
        #             'h.matsuyama@internous.co.jp', #　昼のみ
        #             's.inoue@internous.co.jp', #　昼のみ
        #         ],
        #     },
    }