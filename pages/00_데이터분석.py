import pandas as pd
import altair as alt
import streamlit as st

# CSV 파일명 정의
FILE_NAME = 'countriesMBTI_16types.csv'

# Streamlit 애플리케이션 시작
st.set_page_config(layout="centered")
st.title('🌍 국가별 MBTI Top 3 유형 시각화')
st.write('선택하신 국가에서 가장 높은 비율을 차지하는 MBTI 유형 Top 3를 시각화합니다.')

# 파일에서 데이터 로드
# 데이터가 없을 경우를 대비하여 예외 처리 추가
try:
    df = pd.read_csv(FILE_NAME)
except FileNotFoundError:
    st.error(f"오류: '{FILE_NAME}' 파일을 찾을 수 없습니다. 파일이 실행 파일과 같은 폴더에 있는지 확인해주세요.")
    st.stop() # 파일이 없으면 앱 실행을 중단합니다.
except Exception as e:
    st.error(f"오류: 데이터를 읽어오는 중 문제가 발생했습니다. {e}")
    st.stop()

# MBTI 유형 컬럼 목록 (첫 번째 'Country' 컬럼을 제외한 나머지)
mbti_types = df.columns.tolist()[1:]

# 국가 선택 드롭다운 메뉴
countries = df['Country'].unique().tolist()
selected_country = st.selectbox('나라를 선택해 주세요:', countries)

if selected_country:
    st.header(f'📍 {selected_country}의 MBTI Top 3 유형')

    # 선택된 국가의 데이터 필터링
    country_data = df[df['Country'] == selected_country].copy() # SettingWithCopyWarning 방지 위해 .copy() 사용

    # 데이터를 long format으로 변환 (Altair 시각화를 위해 필요)
    # 선택된 국가의 데이터에서 Country 컬럼을 제외한 MBTI 유형 컬럼들을 선택
    mbti_values = country_data[mbti_types].iloc[0] # 첫 번째 (유일한) 행의 값들을 가져옴
    mbti_melted = pd.DataFrame({
        'MBTI 유형': mbti_values.index,
        '비율': mbti_values.values.astype(float) # float 타입으로 명시적 변환
    })

    # 비율 기준으로 내림차순 정렬하고 Top 3 선택
    top_3_mbti = mbti_melted.sort_values(by='비율', ascending=False).head(3)

    # Altair를 이용한 막대 그래프 시각화
    chart = alt.Chart(top_3_mbti).mark_bar().encode(
        # y축: MBTI 유형 (비율에 따라 정렬)
        y=alt.Y('MBTI 유형', sort='-x', title='MBTI 유형'),
        # x축: 비율 (소수점 첫째 자리까지 백분율로 표시)
        x=alt.X('비율', title='비율 (%)', axis=alt.Axis(format='.1%')),
        # 막대 색상: MBTI 유형별로 다르게 표시
        color=alt.Color('MBTI 유형', title='MBTI 유형'),
        # 마우스 오버 시 MBTI 유형과 비율을 툴팁으로 표시
        tooltip=['MBTI 유형', alt.Tooltip('비율', format='.3f', title='비율')]
    ).properties(
        # 그래프 제목 설정
        title=f'{selected_country}에서 가장 높은 MBTI 유형 TOP 3'
    ).interactive() # 상호작용 기능 활성화 (줌, 팬 등)

    # Streamlit에 차트 표시
    st.altair_chart(chart, use_container_width=True)

    st.write("---")
    st.subheader("데이터 상세 정보")
    st.dataframe(top_3_mbti.reset_index(drop=True)) # 인덱스 리셋하여 깔끔하게 표시
else:
    st.info("시각화를 위해 나라를 선택해주세요.")
