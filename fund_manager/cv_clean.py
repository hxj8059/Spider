import pandas as pd


with open('manager_info.csv', encoding='utf-8') as mi:
    data = pd.read_csv(mi)
    cnt_phd = 0
    cnt_master = 0
    cnt_bachelor = 0
    cnt_other = 0
    cnt_cfa = 0
    cnt_cpa = 0
    cnt_acca = 0
    cnt_frm = 0
    degree_list = []
    cfa_list = []
    frm_list = []
    cpa_list = []
    acca_list = []

    for intro in data['intro']:
        intro = str(intro)
        if '博士' in intro:
            cnt_phd += 1
            print('phd')
            degree_list.append(3)
        elif '硕士' in intro or '研究生' in intro or 'MBA' in intro:
            print('master')
            cnt_master += 1
            degree_list.append(2)
        elif '本科' in intro or '学士' in intro:
            print('bachelor')
            cnt_bachelor += 1
            degree_list.append(1)
        else:
            print(intro)
            cnt_other += 1
            print('unknown')
            degree_list.append(0)


        if 'CFA' in intro:
            cfa_list.append(1)
            cnt_cfa += 1
        else:
            cfa_list.append(0)
        if 'FRM' in intro:
            frm_list.append(1)
            cnt_frm += 1
        else:
            frm_list.append(0)
        if 'CPA' in intro or '注册会计师' in intro:
            cpa_list.append(1)
            cnt_cpa += 1
        else:
            cpa_list.append(0)
        if 'ACCA' in intro or 'acca' in intro:
            acca_list.append(1)
            cnt_acca += 1
        else:
            acca_list.append(0)
    data['degree'] = degree_list
    data['cfa'] = cfa_list
    data['frm'] = frm_list
    data['cpa'] = cpa_list
    data['acca'] = acca_list
    data.to_csv('degree.csv', index=False, sep=',')


    print(cnt_phd)
    print(cnt_master)
    print(cnt_bachelor)
    print(cnt_other)
    print(cnt_cfa)
    print(cnt_frm)
    print(cnt_cpa)
    print(cnt_acca)
