import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config.settings import DATA_DIRS
import matplotlib.pyplot as plt

# 출력 옵션 변경

pd.set_option('display.max_columns', 70)
pd.set_option('display.max_rows', 100)

#------------------------------------------------------------------------------------
# 2018년 수질 데이터
w_idx = ['수도사업자','시설용량(㎥/일)','경도(기준:300/ 단위:(mg/L))','과망간산칼륨소비량(기준:10/ 단위:(mg/L))','염소이온(기준:250/ 단위:(mg/L))',
         '증발잔류물(기준:500/ 단위:(mg/L))','황산이온(기준:200/ 단위:(mg/L))'];
        # 값이 높은 5개의 물진선정

class Water: # 연도별 w_idx의 전국 평균데이터 뿌리기
    def rew1(self):
        lst = []  # Dataframe 만들기 위해서 준비
        cities = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도',
                  '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']
        for i in range(1,11,1):
            dfw = pd.read_excel(DATA_DIRS[0] + '//water_2008_2018_preprocessed.xlsx', sheet_name=i, usecols=w_idx,
                                engine='openpyxl');
            concs = dfw.columns[2:7]
            for city in cities:
                ct_conc = [city]  # 하나의 도시에 대해, 이름과 모든 물질의 농도를 모은 리스트
                for conc in concs:
                    df = dfw[dfw['수도사업자'].str.contains(city)]
                    ct_water = df.copy()
                    ct_water['월별물질농도(mg/일)'] = ct_water['시설용량(㎥/일)'] * ct_water[conc] * 1000
                    if ct_water['시설용량(㎥/일)'].sum() == 0:
                        t_conc = 0
                    else:
                        t_conc = (ct_water['월별물질농도(mg/일)'].sum() / ct_water['시설용량(㎥/일)'].sum()) * 0.001
                        # 2018년, xx지역, xx 물질 평균 농도(mg/L)
                    ct_conc.append(t_conc);
                lst.append(ct_conc)
            result = pd.DataFrame(lst,columns=['수도사업자'] + list(concs));
            result2 = result.mean();
            print(result2)
            #result2.to_excel(water_year_avg.xlsx)


    def rew2(self,year): # 연도를 입력받는 함수
        dfw2 = pd.read_excel(DATA_DIRS[0] + '//water_year_avg.xlsx',engine='openpyxl');
        std = [300,10,250,500,200]
        if year == 2009:
            data = [
            {'name': year,
             'data': np.array(dfw2.iloc[:,1]).tolist()
            },
            {'name': year,
             'data': std
             }];
            print(data);
            return(data);
        elif year == 2010:
            data = [
                {'name': year,
                 'data': np.array(dfw2.iloc[:, 2]).tolist()
                 },
                {'name': year,
                 'data': std
                 }];
            print(data);
            return(data);
        elif year == 2011:
            data = [
                {'name': year,
                 'data': np.array(dfw2.iloc[:, 3]).tolist()
                 },
                {'name': year,
                 'data': std
                 }];
            print(data);
            return(data);
        elif year == 2012:
            data = [
                {'name': year,
                 'data': np.array(dfw2.iloc[:, 4]).tolist()
                 },
                {'name': year,
                 'data': std
                 }];
            print(data);
            return(data);
        elif year == 2013:
            data = [
                {'name': year,
                 'data': np.array(dfw2.iloc[:, 5]).tolist()
                 },
                {'name': year,
                 'data': std
                 }];
            print(data);
            return(data);
        elif year == 2014:
            data = [
                {'name': year,
                 'data': np.array(dfw2.iloc[:, 6]).tolist()
                 },
                {'name': year,
                 'data': std
                 }];
            print(data);
            return(data);
        elif year == 2015:
            data = [
                {'name': year,
                 'data': np.array(dfw2.iloc[:, 7]).tolist()
                 },
                {'name': year,
                 'data': std
                 }];
            print(data);
            return(data);
        elif year == 2016:
            data = [
                {'name': year,
                 'data': np.array(dfw2.iloc[:, 8]).tolist()
                 },
                {'name': year,
                 'data': std
                 }];
            print(data);
            return(data);
        elif year == 2017:
            data = [
                {'name': year,
                 'data': np.array(dfw2.iloc[:, 9]).tolist()
                 },
                {'name': year,
                 'data': std
                 }];
            print(data);
            return(data);
        elif year == 2018:
            data = [
                {'name': year,
                 'data': np.array(dfw2.iloc[:, 10]).tolist()
                 },
                {'name': year,
                 'data': std
                 }];
            print(data);
            return(data);

    def rew3(self):  # 각 지역별, 연도별 1년 평균 물질 농도를 계산하여 dataframe을 반환하는 함수
                     # LJW.py waterQualMean
        lst = []  # Dataframe 만들기 위해서 준비
        years = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
        cities = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시',
                  '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']
        concs = water.columns[3:]

        for y in years:
            year = water['year'] == y
            water_y = water[year]
            for city in cities:
                ct_conc = [city + y]  # 하나의 도시에 대해, 이름과 모든 물질의 농도를 모은 리스트
                for conc in concs:
                    ct_water = water_y[water_y['지역'].str.contains(city)]
                    if conc == '일반세균(기준:100/ 단위:(CFU/mL))':
                        ct_water['월별물질농도(CFU/일)'] = ct_water['시설용량(㎥/일)'] * ct_water[conc] * (10 ** 6)
                        t_conc = ct_water['월별물질농도(CFU/일)'].sum() / ct_water['시설용량(㎥/일)'].sum() * (
                                    10 ** -6)  # 2018년, xx지역, 일반세균 평균 농도(CFU/mL)

                    elif conc == '수소이온농도(기준:5.8 ~ 8.5/ 단위:-)':
                        ct_water[conc] = ct_water[conc].apply(lambda x: 1 / 10 ** x)  # pH를 [H+](단위:mol/L)로 바꾸는 과정

                        ct_water['월별물질농도(mol/일)'] = ct_water['시설용량(㎥/일)'] * ct_water[conc] * 1000
                        t_conc = ct_water['월별물질농도(mol/일)'].sum() / ct_water[
                            '시설용량(㎥/일)'].sum() * 0.001  # 2018년, xx지역, 수소이온 평균 농도(mol/L)
                        t_conc = -np.log10(t_conc)  # 원래대로 pH로 변환

                    else:  # '색도'포함
                        ct_water['월별물질농도(mg/일)'] = ct_water['시설용량(㎥/일)'] * ct_water[conc] * 1000
                        t_conc = ct_water['월별물질농도(mg/일)'].sum() / ct_water[
                            '시설용량(㎥/일)'].sum() * 0.001  # 2018년, xx지역, xx 물질 평균 농도(mg/L)
                    ct_conc.append(t_conc)
                lst.append(ct_conc)

        result = pd.DataFrame(lst, columns=['지역'] + list(concs))
        result = result.set_index('지역').drop(['세종특별자치시2009', '세종특별자치시2010', '세종특별자치시2011', '세종특별자치시2012', '세종특별자치시2013',
                                              '세종특별자치시2014', '세종특별자치시2015', '세종특별자치시2016', '세종특별자치시2017',
                                              '세종특별자치시2018'], axis=0)
        return result
        # result.to_excel(year_region.xlsx)


if __name__ == '__main__':
    Water().rew2(2012)