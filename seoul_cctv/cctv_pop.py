"""
# # 서울시 구별 CCTV 현황 분석하기
#
#
# 1장 서울시 구별 CCTV 현황 분석
# 1-1. CCTV 현황과 인구 현황 데이터 구하기
# 1-2. 파이썬에서 텍스트 파일과 엑셀 파일을 읽기 - pandas
# 1-3. pandas 기초 익히기
# 1-4. pandas를 이용해서 CCTV와 인구 현황 데이터 파악하기
# 1-5. pandas 고급 기능 - 두 DataFrame 병합하기
# 1-6. CCTV 데이터와 인구 현황 데이터를 합치고 분석하기
# 1-7. 파이썬의 대표 시각화 도구 Matplotlib
# 1-8. CCTV 현황 그래프로 분석하기
# * 서울시 각 구별 CCTV수를 파악하고, 인구대비 CCTV 비율을 파악해서 순위 비교
# * 인구대비 CCTV의 평균치를 확인하고 그로부터 CCTV가 과하게 부족한 구를 확인
# * Pandas와 Matplotlib의 기본적 사용법을 확인
# * 단순한 그래프 표현에서 한 단계 더 나아가 경향을 확인하고 시각화하는 기초 확인
# * 서울 열린데이터 광장 사이트 https://data.seoul.go.kr/
# * 서울시 자치구 년도별 CCTV 설치 현황
# * https://data.seoul.go.kr/dataList/datasetView.do?infId=OA-2734&srvType=S&serviceKind=1&currentPageNo=1
# * CSV 파일 다운로드

"""

import pandas as pd
import numpy as np

ctx = '../data/'
df_pop = pd.read_excel(ctx+'population_in_Seoul.xls'
                    ,encoding='UTF-8'
                    ,header=2
                    ,usecols='B,D,G,J,N')
df_cctv = pd.read_csv(ctx+'CCTV_in_Seoul.csv')



df_cctv_col = df_cctv.columns
df_pop_col = df_pop.columns

"""
df_cctv_col
['구별', '소계', '2013년도 이전', '2014년', '2015년', '2016년']

df_pop_col
['구별', '인구수', '한국인', '외국인', '고령자']
"""
df_cctv.rename(columns={df_cctv.columns[0]:'구별'}
                 ,inplace=True)
# inplace=True 실제 변수의내용을 바꿔라


df_pop.rename(columns={df_pop.columns[0]:'구별'
                         ,df_pop.columns[1]:'인구수'
                         ,df_pop.columns[2]:'한국인'
                         ,df_pop.columns[3]:'외국인'
                         ,df_pop.columns[4]:'고령자'}
                ,inplace=True)
# print(df_cctv.sort_values(by='소계', ascending=True))

"""
문제 1: df_cctv 를 소계 기준 오름차순 정렬
문제 2: df_pop 에서 0 번행 삭제
문제 3: df_pop 에서 구별 기준 중복제거
문제 4: df_pop 에서 null 체크 (null 있는지 여부)
문제 5: df_pop 에서 인구수 기준 오름차순 정렬
문제 6: df_cctv 에서  
   '2013년도 이전', 
   '2014년', 
   '2015년', 
   '2016년' 열 삭제. 
	결국 df_cctv 는 '구별', '소계' 만 남김
"""

df_pop.drop([0],inplace=True) #합계 삭제

df_pop['구별'].unique()
df_pop[df_pop['구별'].isnull()]
df_pop.drop([26],inplace=True)
df_pop['외국인비율'] = (df_pop['외국인'] / df_pop['인구수']) * 100
df_pop['고령자비율'] = (df_pop['고령자'] / df_pop['인구수']) * 100
df_cctv.drop(['2013년도 이전','2014년','2015년','2016년'],1,inplace=True)

df_cctv_pop = pd.merge(df_cctv, df_pop, on='구별')


"""
r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
"""
# np.corrcoef()

df_cctv_pop.set_index('구별',inplace=True)

cor1 = np.corrcoef(df_cctv_pop['고령자비율'],df_cctv_pop['소계'])
cor2 = np.corrcoef(df_cctv_pop['외국인비율'],df_cctv_pop['소계'])

#print("고령자비율 상관계수 {} \n 외국인비율 상관계수 {}".format(cor1, cor2))

df_cctv_pop.to_csv(ctx+'cctv_pop.csv')










