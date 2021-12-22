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


def calc_total(lists_x, month_x):
    lists_x.append(month_x)
    total_x = 0
    for x in lists_x:
        total_x += x
        total_x = round(total_x, 2)
    return total_x


def calc_income(base_income, base_pay, month):
    # 住房公积金
    accumulation_fund_pv = round(base_pay * accumulation_fund_p, 2)
    accumulation_fund_ev = round(base_pay * accumulation_fund_e, 2)
    # 养老保险
    old_age_insurance_pv = round(base_pay * old_age_insurance_p, 2)
    old_age_insurance_ev = round(base_pay * old_age_insurance_e, 2)
    # 医疗保险
    media_insurance_pv = round(base_pay * media_insurance_p, 2)
    media_insurance_ev = round(base_pay * media_insurance_e, 2)
    # 失业保险
    unemployment_insurance_pv = round(base_pay * unemployment_insurance_p, 2)
    unemployment_insurance_ev = round(base_pay * unemployment_insurance_e, 2)
    # 工伤保险
    injury_insurance_pv = round(base_pay * injury_insurance_p, 2)
    injury_insurance_ev = round(base_pay * injury_insurance_e, 2)

    # 当月专项扣除五险一金剩余
    month_special_deduction_income = base_income - accumulation_fund_pv - old_age_insurance_pv - media_insurance_pv - unemployment_insurance_pv - injury_insurance_pv
    # 累计专项扣除五险一金剩余
    total_special_deduction_income = calc_total(lists_special_deduction_income, month_special_deduction_income)

    # 当月应交所得税额
    month_income_tax_payable = month_special_deduction_income - 5000
    # 累计应交所得税额
    total_income_tax_payable = calc_total(lists_income_tax_payable, month_income_tax_payable)

    # 当月申报税额
    # percent = 0.1
    percent = get_percent(total_income_tax_payable)
    month_tax = round(month_income_tax_payable * percent, 2)
    # 累计申报税额
    total_tax = calc_total(lists_tax, month_tax)

    # 当月实际收入
    month_real_income = round(month_special_deduction_income - month_tax, 2)
    # 累计实际收入
    total_real_income = calc_total(lists_real_income, month_real_income)

    # 当月公积金收入
    month_real_accumulation_fund = accumulation_fund_pv + accumulation_fund_ev
    # 累计公积金收入
    total_real_accumulation_fund = calc_total(lists_real_accumulation_fund, month_real_accumulation_fund)

    # 当月实际+公积金收入
    month_real_income_accumulation_fund = month_real_income + month_real_accumulation_fund
    # 累计实际+公积金收入
    total_real_income_accumulation_fund = calc_total(lists_real_income_accumulation_fund, month_real_income_accumulation_fund)

    print('')
    print('month=', month, '---------------------------')
    print('当月专项扣除五险一金剩余=', month_special_deduction_income, '当月应交所得税额=', month_income_tax_payable, '当月申报税额=', month_tax)
    print('累计专项扣除五险一金剩余=', total_special_deduction_income, '累计应交所得税额=', total_income_tax_payable, '累计申报税额=', total_tax)

    print('当月实际收入=', month_real_income, '当月公积金收入=', month_real_accumulation_fund, '当月实际+公积金收入=', month_real_income_accumulation_fund)
    print('累计实际收入=', total_real_income, '累计公积金收入=', total_real_accumulation_fund, '累计实际+公积金收入=', total_real_income_accumulation_fund)


# 基本薪资 缴纳基数
# 01-12 薪资发放时间 02-01 次年
def calc(base_income, total_pay, base_pay_pref, mon, base_pay_post):
    print()
    print("#########################################################################################")
    print('####', '税前月收入=', base_income, '已累计税额=', total_pay, '存缴比例1=', base_pay_pref, '存缴比例月份=', mon, '存缴比例2', base_pay_post, '####')
    print("#########################################################################################")
    print()

    clearList()
    lists_income_tax_payable.append(total_pay)

    if mon == 0:
        print('存缴比例没有变化')
        for i in range(2, 12 + 2):
            calc_income(base_income, base_pay_pref, i)
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


calc(29000, 12806.37, 18625, 7, 21250)

calc(29000, 12806.37, 18625, 7, 28221)

calc(28000, 0, 28000, 0, 28000)
