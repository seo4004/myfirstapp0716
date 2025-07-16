import streamlit as st
import pandas as pd
import altair as alt

# 엑셀 파일 로드 (스트림릿 클라우드에 배포 시 해당 파일이 리포지토리에 함께 있어야 합니다)
# countriesMBTI_16types.csv 파일을 사용합니다.
try:
    df = pd.read_csv('countriesMBTI_16types.csv')
except FileNotFoundError:
    st.error("🚨 'countriesMBTI_16types.csv' 파일을 찾을 수 없습니다. 파일이 앱과 같은 디렉토리에 있는지 확인해주세요!")
    st.stop() # 파일이 없으면 앱 실행 중단

# --- 스트림릿 앱 UI 시작 ---
st.set_page_config(
    page_title="🌍 국가별 MBTI TOP 3 분석 📊",
    page_icon="🔍",
    layout="wide" # 넓은 레이아웃으로 설정하여 시각화 공간 확보
)

st.title("🌍 국가별 MBTI TOP 3 분석 📊")
st.markdown("""
    이 앱은 'countriesMBTI_16types.csv' 데이터를 기반으로,
    선택한 국가에서 가장 높은 비율을 차지하는 MBTI 유형 Top 3를 시각화하여 보여줍니다.
    """)
st.write("---")

# 고유한 국가 목록 가져오기
countries = df['country'].unique().tolist()
countries.sort() # 국가 이름을 알파벳 순으로 정렬

# 사용자로부터 국가 선택 받기
selected_country = st.selectbox(
    "나라를 선택하세요 👇",
    countries,
    index=countries.index('South Korea') if 'South Korea' in countries else 0 # 기본값 한국으로 설정
)

if selected_country:
    st.header(f"✨ {selected_country}의 MBTI TOP 3 유형 분석")

    # 선택된 국가의 데이터 필터링
    country_data = df[df['country'] == selected_country]

    if not country_data.empty:
        # percentage 열이 숫자로 되어 있는지 확인 (혹시 문자열이면 변환)
        country_data['percentage'] = pd.to_numeric(country_data['percentage'], errors='coerce')
        country_data.dropna(subset=['percentage'], inplace=True) # 변환 실패한 행 제거

        # percentage 기준으로 상위 3개 MBTI 유형 추출
        top3_mbti = country_data.sort_values(by='percentage', ascending=False).head(3)

        if not top3_mbti.empty:
            st.markdown(f"**{selected_country}**에서 가장 높은 비율을 차지하는 MBTI 유형은 다음과 같습니다:")

            # Altair를 사용한 막대 그래프 시각화
            chart = alt.Chart(top3_mbti).mark_bar(color='#4c78a8').encode(
                x=alt.X('mbti_type:N', sort='-y', title='MBTI 유형'), # y축 값에 따라 정렬
                y=alt.Y('percentage:Q', title='비율 (%)'),
                tooltip=['mbti_type', alt.Tooltip('percentage', format='.1f')] # 툴팁에 비율 소수점 한자리까지 표시
            ).properties(
                title=f'{selected_country}의 MBTI TOP 3 분포'
            ).interactive() # 차트 상호작용 가능하게 함 (줌, 팬 등)

            st.altair_chart(chart, use_container_width=True)

            st.write("---")
            st.subheader("📊 상세 데이터:")
            st.dataframe(top3_mbti.reset_index(drop=True), hide_index=True) # 보기 좋게 인덱스 숨김
        else:
            st.warning("선택된 국가에 대한 MBTI 데이터가 충분하지 않습니다. 다른 국가를 선택해주세요.")
    else:
        st.warning("선택된 국가에 대한 MBTI 데이터가 없습니다. 다른 국가를 선택해주세요.")

st.write("---")
st.markdown("데이터 출처: countriesMBTI_16types.csv")
st.markdown("Made with ❤️ by AI for data insights! ✨")
