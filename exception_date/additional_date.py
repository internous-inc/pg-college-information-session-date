# 急遽開催する日程、時間を変更したい日程を返却
def get_additional_date():
    return {
        # 以下のdictionaryの形式で開催する日程を追加する
        # 日程をYYYYMMDD
        # seminar_startにセミナーの開始時間を追加（その他の時間は自動算出）
        # 1100 or 1300 or 1930
        # 昼食の時間が必要ならlunchをTrue、不要ならFalse

        # '20240101': {
        #     'seminar_start': '1100'
        #     'lunch': False
        # },

        # =======================================================

        '20240223': {
            'seminar_start': '1100', # セミナー日程の開始時間を設定
            'lunch': False,
        }
    }


# 急遽開催する日程、時間を変更したい日程を返却
def get_additional_time():
    return {
        '1100': {
            'preparation_seminar_start': '10:30',
            'preparation_seminar_end': '11:00',
            'seminar_start': '11:00',
            'seminar_end': '12:00',
            'interview_start': '12:00',
            'interview_end': '13:00',
            'users': [
                '山口 良',
                '金子 聖',
                '阿部 倫子',
                '加藤 憲康',
                '大井雄介',
                '富永達彦',
                '松山 光',
                '井上 彩楓',
                '山口 直也',
                '兵藤 慶征',
            ],
            'email': [
                'r.yamaguchi@internous.co.jp',
                'a.kaneko@internous.co.jp',
                'r.abe@internous.co.jp',
                'katoh@internous.co.jp',
                'y.ooi@internous.co.jp',
                't.tominaga@internous.co.jp',
                'h.matsuyama@internous.co.jp',
                's.inoue@internous.co.jp',
                'n.yamaguchi@internous.co.jp',
                'hyodo@internous.co.jp',
            ],
        },
    }