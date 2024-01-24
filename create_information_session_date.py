from config.seminar_settings import get_seminar_settings
from config.interview_settings import get_interview_settings
from config.preparation_seminar_settings import get_preparation_seminar_settings
from config.lunch_settings import get_lunch_settings
from exception_date.additional_date import get_additional_date, get_additional_time
from exception_date.exclusion_date import get_exclusion_date
import calendar
import traceback
import csv

cal = calendar.Calendar()
exclusion_date = get_exclusion_date()
additional_date = get_additional_date()
additional_time = get_additional_time()

# CSVの作成
def create_csv(file_name, header, body):
    with open(f'./csv/{file_name}', 'w', encoding='shift-jis') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(body)
        print(f'【{file_name}の書き出しに成功しました】')
    return

# セミナー日程作成
def create_seminar_date(date_arr, month):
    file_name = 'seminar_date.csv'
    setting = get_seminar_settings() # 設定ファイルの読み込み
    csv_header = setting['common']['header']
    csv_body = [] # 格納する日程を入れるCSV
    user_count_a = 0
    user_arr_a = setting['pattern_a']['speaker']
    user_count_b = 0
    user_arr_b = setting['pattern_b']['speaker']
    speaker = {}

    for index, week_arr in enumerate(date_arr):
        week_number = index + 1
        for date in week_arr:
            comparison_date = date.strftime('%Y%m%d') # 除外日程をチェックするためにフォーマット
            input_date = date.strftime('%Y/%m/%d') # csvに格納するためにフォーマット
            weekday = date.weekday() # 曜日（月:0, 火:1, 水:2, 木:3, 金:4, 土:5, 日:6）
            if (
                comparison_date in additional_date or # 急遽開催する日程、時間を変更したい日程に設定されている
                (
                    (
                        date.month == month and
                        not comparison_date in exclusion_date # 祝日、除外日程ではない
                    ) and
                    (
                        weekday == 0 or # 月曜日
                        weekday == 1 or # 火曜日
                        weekday == 2 or # 水曜日ではない
                        weekday == 3 or # 木曜日ではない
                        (weekday == 4 and week_number % 2 == 0) # 金曜日の偶数数週
                    )
                )
            ):
                start_time = ''
                end_time = ''
                name = ''
                email = ''
                content = ''
                if (
                    comparison_date in additional_date and
                    additional_date[comparison_date]['seminar_start'] == '1100' # 特殊日程のセミナー11時開始の場合
                ):
                    additional_key = additional_date[comparison_date]['seminar_start']
                    start_time = additional_time[additional_key]['seminar_start']
                    end_time = additional_time[additional_key]['seminar_end']
                    name = ','.join(additional_time[additional_key]['users'])
                    email = ','.join(additional_time[additional_key]['email'])
                    content = content = setting['common']['content'] + '未設定'
                elif (
                    weekday == 0 or weekday == 2 or  # 月曜日、水曜日
                    (
                        comparison_date in additional_date and
                        additional_date[comparison_date]['seminar_start'] == '1930' # 特殊日程のセミナー19時半開始の場合
                    )
                ):
                    start_time = setting['pattern_a']['seminar_start']
                    end_time = setting['pattern_a']['seminar_end']
                    name = user_arr_a[user_count_a]['name']
                    email = user_arr_a[user_count_a]['email']
                    content = setting['common']['content'] + name
                    # カウントチェックとスピーカーリセット
                    if user_count_a + 1 == len(user_arr_a):
                        user_count_a = 0
                    else:
                        user_count_a = user_count_a + 1
                elif (
                    weekday == 1 or weekday == 3 or weekday == 4 or # 火曜日、木曜日、金曜日
                    (
                        comparison_date in additional_date and
                        additional_date[comparison_date]['seminar_start'] == '1300' # 特殊日程のセミナー13時開始の場合
                    )
                ):
                    start_time = setting['pattern_b']['seminar_start']
                    end_time = setting['pattern_b']['seminar_end']
                    name = user_arr_b[user_count_b]['name']
                    email = user_arr_b[user_count_b]['email']
                    content = setting['common']['content'] + name
                    # カウントチェックとスピーカーリセット
                    if user_count_b + 1 == len(user_arr_b):
                        user_count_b = 0
                    else:
                        user_count_b = user_count_b + 1
                csv_body.append([
                    input_date, # 開始日
                    start_time, # 開始時刻
                    input_date, # 終了日
                    end_time, # 終了時刻
                    '', # 場所
                    setting['common']['title'], # 予定
                    content, # 内容
                    name, # 名前
                    email, # メールアドレス
                ])
                speaker[comparison_date] = {'name': name, 'email': email} # スピーカーを保存

    create_csv(file_name, csv_header, csv_body) # ファイル書き込み処理
    return speaker

# 個別面談日程作成
def create_interview_date(date_arr, month):
    file_name = 'interview_date.csv'
    setting = get_interview_settings() # 設定ファイルの読み込み
    csv_header = setting['common']['header']
    csv_body = [] # 格納する日程を入れるCSV
    for index, week_arr in enumerate(date_arr):
        week_number = index + 1
        for date in week_arr:
            comparison_date = date.strftime('%Y%m%d') # 除外日程をチェックするためにフォーマット
            input_date = date.strftime('%Y/%m/%d') # csvに格納するためにフォーマット
            weekday = date.weekday() # 曜日（月:0, 火:1, 水:2, 木:3, 金:4, 土:5, 日:6）
            if (
                comparison_date in additional_date or # 急遽開催する日程、時間を変更したい日程に設定されている
                (
                    (
                        date.month == month and
                        not comparison_date in exclusion_date # 祝日、除外日程ではない
                    ) and
                    (
                        weekday == 0 or # 月曜日
                        weekday == 1 or # 火曜日
                        weekday == 2 or # 水曜日ではない
                        weekday == 3 or # 木曜日ではない
                        (weekday == 4 and week_number % 2 == 0) # 金曜日の偶数数週
                    )
                )
            ):
                start_time = ''
                end_time = ''
                users = ''
                email = ''
                if (
                    comparison_date in additional_date and
                    additional_date[comparison_date]['seminar_start'] == '1100' # 特殊日程のセミナー11時開始の場合
                ):
                    additional_key = additional_date[comparison_date]['seminar_start']
                    start_time = additional_time[additional_key]['interview_start']
                    end_time = additional_time[additional_key]['interview_end']
                    users = ','.join(additional_time[additional_key]['users'])
                    email = ','.join(additional_time[additional_key]['email'])
                elif (
                    weekday == 0 or weekday == 2 or  # 月曜日、水曜日
                    (
                        comparison_date in additional_date and
                        additional_date[comparison_date]['seminar_start'] == '1930' # 特殊日程のセミナー19時半開始の場合
                    )
                ):
                    start_time = setting['pattern_a']['seminar_start']
                    end_time = setting['pattern_a']['seminar_end']
                    users = ','.join(setting['pattern_a']['users'])
                    email = ','.join(setting['pattern_a']['email'])
                elif (
                    weekday == 1 or weekday == 3 or weekday == 4 or # 火曜日、木曜日、金曜日
                    (
                        comparison_date in additional_date and
                        additional_date[comparison_date]['seminar_start'] == '1300' # 特殊日程のセミナー13時開始の場合
                    )
                ):
                    start_time = setting['pattern_b']['seminar_start']
                    end_time = setting['pattern_b']['seminar_end']
                    users = ','.join(setting['pattern_b']['users'])
                    email = ','.join(setting['pattern_b']['email'])
                csv_body.append([
                    input_date, # 開始日
                    start_time, # 開始時刻
                    input_date, # 終了日
                    end_time, # 終了時刻
                    '', # 場所
                    setting['common']['title'], # 予定
                    '', # 内容
                    users, # 名前
                    email, # メールアドレス
                ])
    create_csv(file_name, csv_header, csv_body) # ファイル書き込み処理

# セミナー準備日程作成
def create_preparation_seminar_date(date_arr, month, speaker):
    file_name = 'preparation_seminar_date.csv'
    setting = get_preparation_seminar_settings() # 設定ファイルの読み込み
    csv_header = setting['common']['header']
    csv_body = [] # 格納する日程を入れるCSV
    for index, week_arr in enumerate(date_arr):
        week_number = index + 1
        for date in week_arr:
            comparison_date = date.strftime('%Y%m%d') # 除外日程をチェックするためにフォーマット
            input_date = date.strftime('%Y/%m/%d') # csvに格納するためにフォーマット
            weekday = date.weekday() # 曜日（月:0, 火:1, 水:2, 木:3, 金:4, 土:5, 日:6）
            if (
                comparison_date in additional_date or # 急遽開催する日程、時間を変更したい日程に設定されている
                (
                    (
                        date.month == month and
                        not comparison_date in exclusion_date # 祝日、除外日程ではない
                    ) and
                    (
                        weekday == 0 or # 月曜日
                        weekday == 1 or # 火曜日
                        weekday == 2 or # 水曜日ではない
                        weekday == 3 or # 木曜日ではない
                        (weekday == 4 and week_number % 2 == 0) # 金曜日の偶数数週
                    )
                )
            ):
                start_time = ''
                end_time = ''
                content = ''
                if (
                    comparison_date in additional_date and
                    additional_date[comparison_date]['seminar_start'] == '1100' # 特殊日程のセミナー11時開始の場合
                ):
                    additional_key = additional_date[comparison_date]['seminar_start']
                    start_time = additional_time[additional_key]['preparation_seminar_start']
                    end_time = additional_time[additional_key]['preparation_seminar_end']
                    content = setting['common']['content'] + '未設定'
                elif (
                    weekday == 0 or weekday == 2 or  # 月曜日、水曜日
                    (
                        comparison_date in additional_date and
                        additional_date[comparison_date]['seminar_start'] == '1930' # 特殊日程のセミナー19時半開始の場合
                    )
                ):
                    start_time = setting['pattern_a']['seminar_start']
                    end_time = setting['pattern_a']['seminar_end']
                    content = setting['common']['content'] + speaker[comparison_date]['name']
                elif (
                    weekday == 1 or weekday == 3 or weekday == 4 or # 火曜日、木曜日、金曜日
                    (
                        comparison_date in additional_date and
                        additional_date[comparison_date]['seminar_start'] == '1300' # 特殊日程のセミナー13時開始の場合
                    )
                ):
                    start_time = setting['pattern_b']['seminar_start']
                    end_time = setting['pattern_b']['seminar_end']
                    content = setting['common']['content'] + speaker[comparison_date]['name']
                csv_body.append([
                    input_date, # 開始日
                    start_time, # 開始時刻
                    input_date, # 終了日
                    end_time, # 終了時刻
                    '', # 場所
                    setting['common']['title'], # 予定
                    content, # 内容
                    ','.join(setting['common']['users']), # 名前
                    ','.join(setting['common']['email']), # メールアドレス
                ])
    create_csv(file_name, csv_header, csv_body) # ファイル書き込み処理

# 昼食日程作成
def create_lunch_time(date_arr, month, speaker):
    file_name = 'lunch_time.csv'
    setting = get_lunch_settings() # 設定ファイルの読み込み
    csv_header = setting['common']['header']
    csv_body = [] # 格納する日程を入れるCSV
    for index, week_arr in enumerate(date_arr):
        week_number = index + 1
        for date in week_arr:
            comparison_date = date.strftime('%Y%m%d') # 除外日程をチェックするためにフォーマット
            input_date = date.strftime('%Y/%m/%d') # csvに格納するためにフォーマット
            weekday = date.weekday() # 曜日（月:0, 火:1, 水:2, 木:3, 金:4, 土:5, 日:6）
            if (
                (
                    comparison_date in additional_date and
                    additional_date[comparison_date]['seminar_start'] == '1300' # セミナーの開始時間が13時で昼休憩が必要な場合
                ) or
                (
                    (
                        date.month == month and
                        not comparison_date in exclusion_date # 祝日、除外日程ではない
                    ) and
                    (
                        weekday == 1 or # 火曜日
                        weekday == 3 or # 木曜日
                        (weekday == 4 and week_number % 2 == 0) # 金曜日の偶数週
                    )
                )
            ):
                csv_body.append([
                    input_date, # 開始日
                    setting['pattern_a']['seminar_start'], # 開始時刻
                    input_date, # 終了日
                    setting['pattern_a']['seminar_end'], # 終了時刻
                    '', # 場所
                    setting['common']['title'], # 予定
                    setting['common']['content'] + speaker[comparison_date]['name'], # 内容
                    speaker[comparison_date]['name'], # 名前
                    speaker[comparison_date]['email'], # メールアドレス
                ])
    create_csv(file_name, csv_header, csv_body) # ファイル書き込み処理

def create(year, month):
    # 指定された月のカレンダーを取得
    date_arr = cal.monthdatescalendar(int(year), int(month))
    if len(date_arr):
        try:
            print(f'\n【csvファイルの作成を開始します】')
            print('----------------------------------------------------------')
            speaker = create_seminar_date(date_arr, month)
            create_interview_date(date_arr, month)
            create_preparation_seminar_date(date_arr, month, speaker)
            create_lunch_time(date_arr, month, speaker)
            print('----------------------------------------------------------')
            print(f'【csvファイルの作成が終了しました】')
        except:
            print('**********************************************************')
            traceback.print_exc()
            print('**********************************************************')
            print(f'【csvファイルの作成に失敗しました】')
