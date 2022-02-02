# -*- coding: utf-8 -*-

# 住房公积金比例
accumulation_fund_e = 0.12
accumulation_fund_p = 0.12

# 养老保险比例
old_age_insurance_e = 0.16
old_age_insurance_p = 0.08

# 医疗保险比例
media_insurance_e = 0.098
media_insurance_p = 0.02

# 失业保险比例
unemployment_insurance_e = 0.005
unemployment_insurance_p = 0.005

# 工伤保险比例
injury_insurance_e = 0.002
injury_insurance_p = 0

lists_special_deduction_income = []
lists_income_tax_payable = []
lists_tax = []

lists_real_income = []
lists_real_accumulation_fund = []
lists_real_income_accumulation_fund = []


def clearList():
    lists_special_deduction_income.clear()
    lists_income_tax_payable.clear()
    lists_tax.clear()
    lists_real_income.clear()
    lists_real_accumulation_fund.clear()
    lists_real_income_accumulation_fund.clear()


def plus(a, b):
    return round(a + b, 2)


def subtract(a, b):
    return round(a - b, 2)


def multiply(a, b):
    return round(a * b, 2)


def get_percent(total):
    if total <= 36000:
        return 0.03
    elif total <= 144000:
        return 0.1
    elif total <= 300000:
        return 0.2
    elif total <= 420000:
        return 0.25
    elif total <= 660000:
        return 0.3
    elif total <= 960000:
        return 0.35
    else:
        return 0.45


def get_year_percent(total):
    month = round(total / 12, 2)
    if month <= 3000:
        return 0.03, 0
    elif month <= 12000:
        return 0.1, 210
    elif month <= 25000:
        return 0.2, 1410
    elif month <= 35000:
        return 0.25, 2660
    elif month <= 55000:
        return 0.3, 4410
    elif month <= 80000:
        return 0.35, 7160
    else:
        return 0.45, 15160


def calc_total(lists_x, month_x):
    lists_x.append(month_x)
    total_x = 0
    for x in lists_x:
        total_x += x
        total_x = round(total_x, 2)
    return total_x


def calc_income(base_income, base_pay, month):
    # 住房公积金
    accumulation_fund_pv = multiply(base_pay, accumulation_fund_p)
    accumulation_fund_ev = multiply(base_pay, accumulation_fund_e)
    # 养老保险
    old_age_insurance_pv = multiply(base_pay, old_age_insurance_p)
    old_age_insurance_ev = multiply(base_pay, old_age_insurance_e)
    # 医疗保险
    media_insurance_pv = multiply(base_pay, media_insurance_p)
    media_insurance_ev = multiply(base_pay, media_insurance_e)
    # 失业保险
    unemployment_insurance_pv = multiply(base_pay, unemployment_insurance_p)
    unemployment_insurance_ev = multiply(base_pay, unemployment_insurance_e)
    # 工伤保险
    injury_insurance_pv = multiply(base_pay, injury_insurance_p)
    injury_insurance_ev = multiply(base_pay, injury_insurance_e)

    # 当月专项扣除五险一金剩余
    month_special_deduction_income = base_income - accumulation_fund_pv - old_age_insurance_pv - media_insurance_pv - unemployment_insurance_pv - injury_insurance_pv
    month_special_deduction_income = round(month_special_deduction_income, 2)
    # 累计专项扣除五险一金剩余
    total_special_deduction_income = calc_total(lists_special_deduction_income, month_special_deduction_income)

    # 当月应交所得税额
    month_income_tax_payable = month_special_deduction_income - 5000
    # 累计应交所得税额
    total_income_tax_payable = calc_total(lists_income_tax_payable, month_income_tax_payable)

    # 当月申报税额
    percent = get_percent(total_income_tax_payable)
    month_tax = multiply(month_income_tax_payable, percent)
    # 累计申报税额
    total_tax = calc_total(lists_tax, month_tax)

    # 当月实际收入
    month_real_income = subtract(month_special_deduction_income, month_tax)
    # 累计实际收入
    total_real_income = calc_total(lists_real_income, month_real_income)

    # 当月公积金收入
    month_real_accumulation_fund = plus(accumulation_fund_pv, accumulation_fund_ev)
    # 累计公积金收入
    total_real_accumulation_fund = calc_total(lists_real_accumulation_fund, month_real_accumulation_fund)

    # 当月实际+公积金收入
    month_real_income_accumulation_fund = plus(month_real_income, month_real_accumulation_fund)
    # 累计实际+公积金收入
    total_real_income_accumulation_fund = calc_total(lists_real_income_accumulation_fund,
                                                     month_real_income_accumulation_fund)

    print('')
    print('month=', month, '---------------------------')
    print('个人', '公积金=', accumulation_fund_pv, '养老=', old_age_insurance_pv, '医疗=', media_insurance_pv, '失业=',
          unemployment_insurance_pv)
    print('公司', '公积金=', accumulation_fund_ev, '养老=', old_age_insurance_ev, '医疗=', media_insurance_ev, '失业=',
          unemployment_insurance_ev, '工伤=', injury_insurance_ev)
    print('当月专项扣除五险一金剩余=', month_special_deduction_income, '当月应交所得税额=', month_income_tax_payable, '当月申报税额=', month_tax)
    print('累计专项扣除五险一金剩余=', total_special_deduction_income, '累计应交所得税额=', total_income_tax_payable, '累计申报税额=', total_tax)

    print('当月实际收入=', month_real_income, '当月公积金收入=', month_real_accumulation_fund, '当月实际+公积金收入=',
          month_real_income_accumulation_fund)
    print('累计实际收入=', total_real_income, '累计公积金收入=', total_real_accumulation_fund, '累计实际+公积金收入=',
          total_real_income_accumulation_fund)


def calc_awards(base_income, ppr):
    total_award = multiply(base_income, ppr)

    total_award_p = get_year_percent(total_award)

    total_award_tax = subtract(multiply(total_award, total_award_p[0]), total_award_p[1])

    total_award_real = subtract(total_award, total_award_tax)

    print(base_income, '*', ppr, '=', total_award, '-', total_award_tax, '=', total_award_real)
    return total_award_real


def print_total_income(base_income, month):
    print('\ncalc_awards')
    total_award_real = calc_awards(base_income, month)

    money = calc_total(lists_real_income, 0)
    come_real = plus(money, total_award_real)
    print('累计实际收入:', money, ' + ', '年终奖:', total_award_real, ' = ', come_real)


# 基本薪资 缴纳基数
# 01-12 薪资发放时间 02-01 次年
def calc(base_income, base_pay_pref, mon, base_pay_post):
    print()
    print("#########################################################################################")
    print('####', '税前月收入=', base_income, '存缴比例1=', base_pay_pref, '存缴比例月份=', mon, '存缴比例2',
          base_pay_post, '####')
    print("#########################################################################################")
    print()

    clearList()

    if mon == 0:
        print('存缴比例没有变化')
        for i in range(2, 12 + 2):
            calc_income(base_income, base_pay_pref, i)

        print_total_income(base_income, 4)
        return

    print('存缴比例变前, 存缴比例=', base_pay_pref)
    for i in range(2, mon):
        calc_income(base_income, base_pay_pref, i)

    print("")
    print("#########################################################################################")
    print("")

    print('存缴比例变后, 存缴比例=', base_pay_post)
    for i in range(mon, 12 + 2):
        calc_income(base_income, base_pay_post, i)

    # 年终奖按照财年平均
    print_total_income(23750, 3.0)
    print_total_income(23750, 3.5)
    print_total_income(23750, 4.0)


calc(29000, 18625, 7, 21250)

# calc(29000, 18625, 7, 28221)

# calc(28000, 28000, 0, 28000)

# calc(34000, 28221, 0, 28221)
