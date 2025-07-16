import pandas as pd
import altair as alt
import streamlit as st

# CSV 파일명 정의
FILE_NAME = 'countriesMBTI_16types.csv'

# Streamlit 애플리케이션 시작
st.set_page_config(layout="centered")
st.title('🌍 국가별 MBTI 분포 시각화')
st.write('선택하신 국가의 MBTI 유형 분포를 확인하고, 상위 3가지 유형을 시각화합니다.')

# 파일에서 데이터 로드
try:
    df = pd.read_csv(FILE_NAME)
except FileNotFoundError:
    st.error(f"오류: '{FILE_NAME}' 파일을 찾을 수 없습니다. 파일이 실행 파일과 같은 폴더에 있는지 확인해주세요.")
    st.stop()
except Exception as e:
    st.error(f"오류: 데이터를 읽어오는 중 문제가 발생했습니다. {e}")
    st.stop()

# MBTI 유형 컬럼 목록 (첫 번째 'Country' 컬럼을 제외한 나머지)
mbti_types = df.columns.tolist()[1:]

# 국가 선택 드롭다운 메뉴
countries = df['Country'].unique().tolist()
selected_country = st.selectbox('나라를 선택해 주세요:', countries)

if selected_country:
    st.header(f'📍 {selected_country}의 MBTI 유형 분포')

    # 선택된 국가의 데이터 필터링
    country_data = df[df['Country'] == selected_country].copy()

    # 데이터를 long format으로 변환 (Altair 시각화 및 상세 데이터 표시를 위해 필요)
    mbti_values = country_data[mbti_types].iloc[0] # 첫 번째 (유일한) 행의 값들을 가져옴
    mbti_melted = pd.DataFrame({
        'MBTI 유형': mbti_values.index,
        '비율': mbti_values.values.astype(float) # float 타입으로 명시적 변환
    })

    # Top 3 MBTI 유형 추출 (시각화용)
    top_3_mbti = mbti_melted.sort_values(by='비율', ascending=False).head(3)

    st.subheader(f'{selected_country}의 MBTI 상위 3가지 유형')
    # Altair를 이용한 막대 그래프 시각화 (Top 3)
    chart = alt.Chart(top_3_mbti).mark_bar().encode(
        y=alt.Y('MBTI 유형', sort='-x', title='MBTI 유형'),
        x=alt.X('비율', title='비율 (%)', axis=alt.Axis(format='.1%')),
        color=alt.Color('MBTI 유형', title='MBTI 유형'),
        tooltip=['MBTI 유형', alt.Tooltip('비율', format='.3f', title='비율')]
    ).properties(
        title=f'{selected_country}의 MBTI 상위 3가지 유형'
    ).interactive()

    # Streamlit에 Top 3 차트 표시
    st.altair_chart(chart, use_container_width=True)

    st.write("---")
    st.subheader(f"{selected_country}의 전체 MBTI 유형 상세 분포")

    # 전체 16개 MBTI 유형 데이터를 비율 기준으로 정렬하여 표시
    st.dataframe(mbti_melted.sort_values(by='비율', ascending=False).reset_index(drop=True).style.format({'비율': '{:.2%}'}))

else:
    st.info("시각화를 위해 나라를 선택해주세요.")
