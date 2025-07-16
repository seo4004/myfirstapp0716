import streamlit as st
import time # 풍선 효과를 위한 time 모듈 추가

# MBTI 유형별 포켓몬 추천 데이터 (이미지 URL과 이름, 그리고 진로 연계 키워드)
pokemon_recommendations = {
    "ISTJ": [
        {"name": "거북왕 (Blastoise)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png", "keywords": "규칙 준수, 책임감, 체계적인 업무"},
        {"name": "이상해꽃 (Venusaur)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png", "keywords": "안정성, 꼼꼼함, 계획적인 실행"},
        {"name": "잠만보 (Snorlax)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png", "keywords": "끈기, 인내심, 신뢰성"}
    ],
    "ISFJ": [
        {"name": "블래키 (Umbreon)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/197.png", "keywords": "조화, 협력, 타인 배려"},
        {"name": "럭키 (Chansey)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png", "keywords": "헌신, 봉사, 따뜻한 마음"},
        {"name": "푸린 (Jigglypuff)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png", "keywords": "관계 중심, 안정적인 지원"}
    ],
    "INFJ": [
        {"name": "뮤츠 (Mewtwo)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png", "keywords": "통찰력, 이상 추구, 깊은 이해"},
        {"name": "루기아 (Lugia)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png", "keywords": "영감, 비전 제시, 평화 지향"},
        {"name": "세레비 (Celebi)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/251.png", "keywords": "성장 촉진, 미래 지향, 의미 부여"}
    ],
    "INTJ": [
        {"name": "뮤츠 (Mewtwo)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png", "keywords": "전략적 사고, 독립성, 문제 해결"},
        {"name": "후딘 (Alakazam)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png", "keywords": "논리적 분석, 복잡한 시스템 이해"},
        {"name": "팬텀 (Gengar)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png", "keywords": "독창성, 비판적 사고, 심오한 탐구"}
    ],
    "ISTP": [
        {"name": "메타몽 (Ditto)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png", "keywords": "적응력, 문제 해결, 실용성"},
        {"name": "파비코리 (Altaria)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/334.png", "keywords": "유연성, 즉흥성, 현실적 대처"},
        {"name": "라이츄 (Raichu)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png", "keywords": "행동 지향, 즉각적인 반응, 기술 활용"}
    ],
    "ISFP": [
        {"name": "이상해씨 (Bulbasaur)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png", "keywords": "예술적 감각, 개성 표현, 유연한 사고"},
        {"name": "피카츄 (Pikachu)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png", "keywords": "자유로움, 친근함, 현재 즐김"},
        {"name": "이브이 (Eevee)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png", "keywords": "탐색, 변화 수용, 감성적 접근"}
    ],
    "INFP": [
        {"name": "뮤 (Mew)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png", "keywords": "창의성, 이상주의, 진정성"},
        {"name": "이상해꽃 (Venusaur)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png", "keywords": "성장, 자기 탐색, 심오한 의미 추구"},
        {"name": "리피아 (Leafeon)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/470.png", "keywords": "독특한 관점, 조화로운 관계, 영감"}
    ],
    "INTP": [
        {"name": "뮤츠 (Mewtwo)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png", "keywords": "이론적 탐구, 분석적 사고, 문제 해결"},
        {"name": "폴리곤 (Porygon)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/137.png", "keywords": "시스템 이해, 복잡한 개념 분석"},
        {"name": "메타그로스 (Metagross)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/376.png", "keywords": "논리적 구조화, 객관적 판단, 지식 확장"}
    ],
    "ESTP": [
        {"name": "리자몽 (Charizard)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png", "keywords": "도전, 실행력, 위기 대처"},
        {"name": "망나뇽 (Dragonite)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png", "keywords": "활동적, 문제 해결, 현실적 판단"},
        {"name": "꼬부기 (Squirtle)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png", "keywords": "자신감, 즉각적인 행동, 경험 중시"}
    ],
    "ESFP": [
        {"name": "피카츄 (Pikachu)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png", "keywords": "에너지 넘침, 사교성, 재미 추구"},
        {"name": "푸린 (Jigglypuff)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png", "keywords": "즉흥적, 친화력, 낙천적"},
        {"name": "고라파덕 (Psyduck)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/54.png", "keywords": "유머러스, 자유로움, 현재 즐김"}
    ],
    "ENFP": [
        {"name": "피카츄 (Pikachu)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png", "keywords": "열정, 새로운 아이디어, 다양성"},
        {"name": "이브이 (Eevee)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png", "keywords": "호기심, 무한한 가능성, 관계 지향"},
        {"name": "꼬부기 (Squirtle)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png", "keywords": "긍정적 에너지, 탐험가 기질"}
    ],
    "ENTP": [
        {"name": "뮤츠 (Mewtwo)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png", "keywords": "혁신, 비판적 사고, 도전적"},
        {"name": "팬텀 (Gengar)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png", "keywords": "지적 호기심, 다양한 관점, 유머"},
        {"name": "마기라스 (Tyranitar)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/248.png", "keywords": "문제 제기, 논쟁, 창조적 파괴"}
    ],
    "ESTJ": [
        {"name": "거북왕 (Blastoise)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png", "keywords": "실행력, 조직력, 리더십"},
        {"name": "망나뇽 (Dragonite)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png", "keywords": "책임감, 실용적 접근, 목표 달성"},
        {"name": "근육몬 (Machoke)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/67.png", "keywords": "효율성, 구조화, 명확한 지시"}
    ],
    "ESFJ": [
        {"name": "럭키 (Chansey)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png", "keywords": "배려, 공동체 지향, 서비스 정신"},
        {"name": "삐삐 (Clefairy)", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/35.png", "keywords": "사교성, 친화력, 도움 주기"},
        {"name": "잠만보 (Snorlax)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png", "keywords": "안정감, 지지, 따뜻한 분위기 조성"}
    ],
    "ENFJ": [
        {"name": "루기아 (Lugia)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png", "keywords": "영향력, 동기 부여, 리더십"},
        {"name": "이상해꽃 (Venusaur)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png", "keywords": "성장 지원, 공감 능력, 비전 공유"},
        {"name": "피카츄 (Pikachu)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png", "keywords": "긍정적 에너지, 소통 능력, 사람 중심"}
    ],
    "ENTJ": [
        {"name": "리자몽 (Charizard)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png", "keywords": "결단력, 추진력, 전략적 리더십"},
        {"name": "망나뇽 (Dragonite)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png", "keywords": "목표 지향, 효율성, 시스템 구축"},
        {"name": "뮤츠 (Mewtwo)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png", "keywords": "비전 제시, 통솔력, 혁신 주도"}
    ]
}

# MBTI 유형 리스트
mbti_types = list(pokemon_recommendations.keys())
mbti_types.sort() # 순서대로 정렬

# 웹 앱의 제목 설정
st.set_page_config(
    page_title="💖 MBTI x 포켓몬: 진로 짝꿍 찾기 💖",
    page_icon="✨", # 더 센스 있는 아이콘으로 변경
    layout="centered"
)

st.title("💖 MBTI x 포켓몬: 진로 짝꿍 찾기 💖")
st.markdown("""
    환영합니다! 👋 당신의 MBTI는 어떤 포켓몬과 닮았을까요?
    그리고 그 특성들이 당신의 진로 탐색에 어떤 흥미로운 힌트를 줄 수 있을지 함께 알아봐요!
    이 앱은 MBTI 유형별 특징과 포켓몬의 개성을 연결하여 당신의 잠재력을 탐색하고,
    미래의 **직업 선택**이나 **역량 강화**에 대한 영감을 얻을 수 있도록 도와줄 거예요.
    자, 이제 당신의 MBTI를 선택하고 특별한 포켓몬 친구들을 만나러 떠나볼까요? 🚀
    """)
st.write("---")

# MBTI 선택 드롭다운
selected_mbti = st.selectbox(
    "✨ 당신의 MBTI 유형은 무엇인가요?",
    mbti_types,
    index=mbti_types.index("INFP") # 초기 선택값 설정
)

# 풍선 효과 추가: MBTI 선택 시 나타남
if selected_mbti:
    st.balloons() # 풍선 효과!

st.write(f"### 🎉 당신의 MBTI는 **{selected_mbti}** 이군요!")
st.write(f"**{selected_mbti}** 유형에게 잘 어울릴 것 같은 포켓몬 친구들과 진로 힌트를 소개합니다! 🧐")

# 선택된 MBTI에 따른 포켓몬 추천 및 진로 연계 설명
if selected_mbti:
    recommended_pokemons = pokemon_recommendations.get(selected_mbti, [])

    if recommended_pokemons:
        cols = st.columns(3)
        for i, pokemon in enumerate(recommended_pokemons):
            with cols[i]:
                st.image(pokemon["image_url"], caption=pokemon["name"], use_container_width=True)
                st.markdown(f"<h4 style='text-align: center; color: #5B5B5B;'>{pokemon['name']}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: center; font-size: 0.9em; color: #7F7F7F;'><b>키워드:</b> {pokemon['keywords']}</p>", unsafe_allow_html=True)
        
        # 진로 연계 설명 (최소 300자)
        st.write("---")
        st.subheader(f"💡 {selected_mbti} 유형을 위한 진로 가이드!")
        
        if selected_mbti == "ISTJ":
            st.write("""
                **ISTJ** 유형은 '세상의 소금' 같은 존재로, 책임감이 강하고 현실적인 특성을 지닙니다. 거북왕처럼 묵묵히 제 역할을 수행하고, 이상해꽃처럼 꼼꼼하게 계획을 실행하며, 잠만보처럼 끈기 있게 목표를 달성하죠.
                이러한 특성은 **회계사, 공무원, 경찰, 감사원, 시스템 관리자, 데이터 분석가**와 같이 정확성과 신뢰성이 중요한 직업에 매우 잘 어울립니다. 체계적인 절차를 따르고 세부 사항을 놓치지 않는 당신의 강점은 조직의 안정성과 효율성을 높이는 데 크게 기여할 것입니다. 꼼꼼한 기록과 분석을 통해 문제점을 발견하고 해결하는 능력은 어떤 분야에서든 빛을 발할 거예요.
                """)
        elif selected_mbti == "ISFJ":
            st.write("""
                **ISFJ** 유형은 '수호자'로 불리며, 따뜻하고 헌신적인 마음으로 타인을 배려하는 데 능숙합니다. 블래키처럼 온화하면서도 든든한 존재가 되어주고, 럭키처럼 타인의 건강과 행복을 돌보며, 푸린처럼 사람들과 안정적인 관계를 형성하는 데 탁월하죠.
                이러한 당신의 강점은 **간호사, 사회복지사, 교사, 상담사, 인사 담당자, 고객 서비스 전문가**와 같이 사람을 직접 돕고 지원하는 직업에서 빛을 발합니다. 공감 능력과 세심함으로 주변 사람들에게 편안함과 안정감을 제공하며, 조화로운 환경을 조성하는 데 기여할 수 있습니다. 따뜻한 마음과 실질적인 도움을 통해 사회에 긍정적인 영향을 미칠 수 있을 거예요.
                """)
        elif selected_mbti == "INFJ":
            st.write("""
                **INFJ** 유형은 '예언자' 또는 '옹호자'로, 깊은 통찰력과 이상을 추구하는 특성을 지닙니다. 뮤츠처럼 심오한 생각과 비전을 가지고, 루기아처럼 영감을 주며 평화를 지향하고, 세레비처럼 성장과 의미를 찾아 나섭니다.
                이러한 당신의 강점은 **심리학자, 상담사, 작가, 예술가, 사회 운동가, HR 전문가, 교육자**와 같이 사람들의 내면을 이해하고 변화를 이끌어내는 직업에 잘 맞습니다. 복잡한 문제를 깊이 탐구하고, 이상을 현실로 만들기 위한 전략을 세우는 데 뛰어난 능력을 발휘할 수 있습니다. 타인의 잠재력을 보고 성장하도록 돕는 당신의 역할은 사회에 큰 울림을 줄 것입니다.
                """)
        elif selected_mbti == "INTJ":
            st.write("""
                **INTJ** 유형은 '전략가' 또는 '설계자'로, 독립적이고 논리적인 사고를 바탕으로 혁신적인 아이디어를 추구합니다. 뮤츠처럼 뛰어난 지능으로 복잡한 문제를 해결하고, 후딘처럼 논리적으로 분석하며, 팬텀처럼 독창적인 방식으로 세상을 탐구하죠.
                이러한 당신의 강점은 **과학자, 연구원, IT 개발자, 전략 컨설턴트, 건축가, 시스템 설계자, 교수**와 같이 복잡한 시스템을 분석하고 새로운 해결책을 제시하는 직업에 적합합니다. 비판적 사고와 장기적인 안목으로 큰 그림을 그리며, 효율적인 계획을 통해 목표를 달성하는 데 능숙합니다. 당신의 지적인 호기심과 분석력은 미지의 영역을 개척하는 데 기여할 것입니다.
                """)
        elif selected_mbti == "ISTP":
            st.write("""
                **ISTP** 유형은 '장인'으로, 호기심이 많고 실용적인 문제 해결에 능숙합니다. 메타몽처럼 어떤 상황에도 적응하며, 파비코리처럼 유연하게 대처하고, 라이츄처럼 즉각적으로 행동하여 문제를 해결합니다.
                이러한 특성은 **엔지니어, 기술자, 파일럿, 스포츠 선수, 외과의사, 요리사, 그래픽 디자이너**와 같이 직접 손으로 만들고 문제를 해결하는 직업에 이상적입니다. 실제적인 경험을 통해 배우고, 도구를 다루는 데 뛰어난 당신의 능력은 복잡한 기계를 수리하거나, 정교한 작업을 수행하는 데 큰 강점이 됩니다. 예측 불가능한 상황에서도 침착하게 대응하여 효율적인 결과를 만들어낼 수 있을 거예요.
                """)
        elif selected_mbti == "ISFP":
            st.write("""
                **ISFP** 유형은 '모험가' 또는 '예술가'로, 아름다움을 추구하고 감각적인 경험을 중요시합니다. 이상해씨처럼 자연을 사랑하고, 피카츄처럼 자유롭게 자신을 표현하며, 이브이처럼 다양한 가능성을 탐색합니다.
                이러한 당신의 강점은 **미술가, 음악가, 디자이너, 사진작가, 패션 관련 직업, 여행 가이드, 조경사**와 같이 창의성과 감성을 발휘할 수 있는 직업에 잘 어울립니다. 현재를 즐기고 순간의 아름다움을 포착하는 당신의 능력은 사람들에게 새로운 영감과 즐거움을 줄 수 있습니다. 개성적인 표현과 유연한 사고로 자신만의 길을 개척하는 데 뛰어날 거예요.
                """)
        elif selected_mbti == "INFP":
            st.write("""
                **INFP** 유형은 '중재자' 또는 '치유자'로, 깊은 공감 능력과 이상을 추구하는 따뜻한 마음을 지닙니다. 뮤처럼 순수하고 창의적인 에너지를 가지고, 이상해꽃처럼 성장과 진정한 의미를 찾아 나서는 당신은 마치 리피아처럼 조화롭고 독특한 관점을 가집니다.
                이러한 특성은 **작가, 상담사, 예술가, 사회복지사, 심리학자, 교육자, 연구원** 등 자신의 가치를 표현하고 타인의 성장을 돕는 직업에 잘 맞습니다. 당신의 풍부한 상상력과 타인의 감정을 이해하는 능력은 사람들에게 영감을 주고, 더 나은 세상을 만드는 데 기여할 수 있습니다. 진정성과 깊이를 추구하는 당신은 어떤 분야에서든 긍정적인 변화를 가져올 수 있을 거예요.
                """)
        elif selected_mbti == "INTP":
            st.write("""
                **INTP** 유형은 '논리적인 사색가'로, 지적 호기심이 강하고 복잡한 이론을 탐구하는 데 뛰어납니다. 뮤츠처럼 심오한 지식을 추구하고, 폴리곤처럼 시스템을 분석하며, 메타그로스처럼 논리적으로 구조화하는 능력을 지닙니다.
                이러한 당신의 강점은 **과학자, 연구원, IT 개발자, 프로그래머, 철학자, 대학 교수, 분석가**와 같이 지적인 도전과 문제 해결을 요하는 직업에 매우 적합합니다. 새로운 아이디어를 탐색하고 복잡한 문제를 해결하는 데 탁월하며, 끊임없이 배우고 성장하려는 욕구가 강합니다. 당신의 객관적이고 비판적인 사고는 혁신적인 발견과 발전에 기여할 것입니다.
                """)
        elif selected_mbti == "ESTP":
            st.write("""
                **ESTP** 유형은 '사업가' 또는 '활동가'로, 에너지가 넘치고 현실적인 문제 해결에 능합니다. 리자몽처럼 도전을 즐기고, 망나뇽처럼 활발하게 활동하며, 꼬부기처럼 자신감 있게 상황에 대처합니다.
                이러한 특성은 **영업 관리자, 기업가, 스포츠 선수, 응급 구조원, 마케터, 배우, 투자자**와 같이 빠르고 즉각적인 판단과 행동이 필요한 직업에 잘 어울립니다. 당신의 순발력과 뛰어난 현실감각은 위기 상황에서 빛을 발하며, 사람들과의 상호작용을 통해 기회를 포착하는 데 능숙합니다. 생동감 넘치는 에너지는 어떤 환경에서든 긍정적인 영향을 미칠 것입니다.
                """)
        elif selected_mbti == "ESFP":
            st.write("""
                **ESFP** 유형은 '연예인' 또는 '사교형'으로, 활발하고 낙천적인 성격으로 주변 사람들에게 즐거움을 줍니다. 피카츄처럼 밝은 에너지를 발산하고, 푸린처럼 사람들과 쉽게 어울리며, 고라파덕처럼 유머러스하게 분위기를 만듭니다.
                이러한 당신의 강점은 **공연 예술가, 이벤트 기획자, 유튜버, 강사, 여행 가이드, 파티 플래너, 판매원**과 같이 사람들과 소통하고 즐거움을 주는 직업에 잘 맞습니다. 즉흥적이고 유연한 사고로 다양한 상황에 빠르게 적응하며, 사람들을 편안하게 해주는 당신의 매력은 어떤 모임에서든 주목받을 것입니다. 당신의 긍정적인 에너지는 주변을 활기차게 만들 거예요.
                """)
        elif selected_mbti == "ENFP":
            st.write("""
                **ENFP** 유형은 '활동가' 또는 '스파크'로, 넘치는 열정과 새로운 아이디어를 통해 사람들에게 영감을 줍니다. 피카츄처럼 긍정적인 에너지를 뿜어내고, 이브이처럼 무한한 가능성을 탐색하며, 꼬부기처럼 호기심 가득한 눈으로 세상을 바라봅니다.
                이러한 당신의 강점은 **마케터, 광고 기획자, 컨설턴트, 교육자, 유튜버, 스타트업 창업가, 심리 상담사**와 같이 창의성과 대인 관계 능력이 중요한 직업에 잘 어울립니다. 새로운 아이디어를 제안하고 사람들에게 동기를 부여하는 데 탁월하며, 다양한 사람들과 교류하며 시너지를 창출합니다. 당신의 긍정적인 에너지와 개방적인 태도는 어떤 분야에서든 혁신을 이끌어낼 것입니다.
                """)
        elif selected_mbti == "ENTP":
            st.write("""
                **ENTP** 유형은 '변론가' 또는 '발명가'로, 지적인 호기심이 강하고 기존의 틀을 깨는 혁신적인 사고를 지닙니다. 뮤츠처럼 날카로운 분석력으로 본질을 꿰뚫고, 팬텀처럼 독창적인 관점으로 문제를 바라보며, 마기라스처럼 창조적인 도전을 두려워하지 않습니다.
                이러한 당신의 강점은 **기업가, 컨설턴트, 변호사, 연구원, 소프트웨어 개발자, 과학자, 발명가**와 같이 복잡한 문제를 해결하고 새로운 시스템을 구축하는 직업에 적합합니다. 논쟁을 통해 아이디어를 발전시키고, 다양한 가능성을 탐색하며, 혁신적인 해결책을 제시하는 데 능숙합니다. 당신의 지적인 재치와 도전 정신은 어떤 분야에서든 새로운 가치를 창출할 것입니다.
                """)
        elif selected_mbti == "ESTJ":
            st.write("""
                **ESTJ** 유형은 '경영자' 또는 '리더'로, 뛰어난 실행력과 조직력을 바탕으로 목표를 효율적으로 달성합니다. 거북왕처럼 든든하게 팀을 이끌고, 망나뇽처럼 책임감 있게 임무를 완수하며, 근육몬처럼 효율적으로 일을 처리합니다.
                이러한 당신의 강점은 **기업 관리자, 프로젝트 매니저, 경찰관, 군인, 회계사, 공무원, 행정 관리자**와 같이 명확한 목표 설정과 체계적인 실행이 필요한 직업에 매우 잘 어울립니다. 질서와 효율성을 중시하며, 계획을 세우고 이를 추진하는 데 탁월한 능력을 발휘합니다. 당신의 리더십과 실용적인 접근 방식은 어떤 조직에서든 안정적인 성과를 만들어낼 것입니다.
                """)
        elif selected_mbti == "ESFJ":
            st.write("""
                **ESFJ** 유형은 '사회운동가' 또는 '친선 도모자'로, 따뜻한 마음으로 사람들을 연결하고 공동체의 조화를 중요시합니다. 럭키처럼 타인을 배려하고, 삐삐처럼 사교성이 뛰어나며, 잠만보처럼 주변에 안정감과 편안함을 제공합니다.
                이러한 당신의 강점은 **교사, 간호사, 사회복지사, 상담사, 인사 담당자, 고객 서비스 관리자, 이벤트 플래너**와 같이 사람들과 직접 소통하고 지원하는 직업에 잘 맞습니다. 뛰어난 공감 능력과 친화력으로 사람들을 편안하게 해주고, 공동체의 화합을 이끌어내는 데 기여합니다. 당신의 따뜻한 배려심과 책임감은 주변 사람들에게 큰 힘이 될 것입니다.
                """)
        elif selected_mbti == "ENFJ":
            st.write("""
                **ENFJ** 유형은 '선도자' 또는 '정의로운 지도자'로, 타인에게 영감을 주고 긍정적인 변화를 이끌어내는 데 능숙합니다. 루기아처럼 강력한 영향력으로 사람들을 이끌고, 이상해꽃처럼 성장을 돕고, 피카츄처럼 긍정적인 에너지로 주변을 밝힙니다.
                이러한 당신의 강점은 **교사, 강사, 리더십 코치, 컨설턴트, 심리 상담사, 사회 운동가, HR 매니저**와 같이 사람들에게 동기를 부여하고 잠재력을 이끌어내는 직업에 매우 적합합니다. 뛰어난 소통 능력과 공감력으로 사람들의 마음을 움직이고, 공동의 목표를 향해 나아가도록 이끄는 데 탁월합니다. 당신의 비전과 리더십은 어떤 분야에서든 긍정적인 변화를 가져올 것입니다.
                """)
        elif selected_mbti == "ENTJ":
            st.write("""
                **ENTJ** 유형은 '통솔자' 또는 '지도자'로, 강한 결단력과 추진력으로 목표를 향해 나아갑니다. 리자몽처럼 강력한 리더십으로 상황을 주도하고, 망나뇽처럼 효율적으로 목표를 달성하며, 뮤츠처럼 비전을 제시하고 혁신을 이끌어냅니다.
                이러한 당신의 강점은 **최고 경영자(CEO), 사업가, 프로젝트 매니저, 전략 컨설턴트, 변호사, 정치인, 군 지휘관**과 같이 리더십과 전략적 사고가 중요한 직업에 잘 어울립니다. 복잡한 문제를 분석하고, 명확한 목표를 설정하며, 사람들을 효율적으로 조직하여 원하는 결과를 만들어내는 데 능숙합니다. 당신의 뛰어난 통솔력과 비전은 어떤 조직에서든 성공적인 미래를 만들어갈 것입니다.
                """)
        else:
            st.write("해당 MBTI에 대한 자세한 진로 가이드는 준비 중입니다! 😅")

else:
    st.info("⬆️ 위에서 당신의 MBTI를 선택해주세요! ⬆️")


st.write("---") # 푸터 구분선
st.markdown("Made with ❤️ by AI for your bright future! ✨") # 푸터
