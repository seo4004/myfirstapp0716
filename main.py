import streamlit as st

# MBTI 유형별 포켓몬 추천 데이터 (기본 라이브러리만 사용하므로 딕셔너리로 직접 관리)
# 각 MBTI에 어울리는 포켓몬 이미지 URL과 이름 3개를 매핑합니다.
# 이미지 URL은 포켓몬 공식 사이트나 신뢰할 수 있는 CDN에서 가져오는 것이 좋습니다.
# 여기서는 예시로 'https://example.com/pokemon_image_url' 형태를 사용합니다.
# 실제 배포 시에는 유효한 이미지 URL로 교체해야 합니다.

pokemon_recommendations = {
    "ISTJ": [
        {"name": "거북왕 (Blastoise)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png"},
        {"name": "이상해꽃 (Venusaur)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png"},
        {"name": "잠만보 (Snorlax)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png"}
    ],
    "ISFJ": [
        {"name": "블래키 (Umbreon)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/197.png"},
        {"name": "럭키 (Chansey)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png"},
        {"name": "푸린 (Jigglypuff)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png"}
    ],
    "INFJ": [
        {"name": "뮤츠 (Mewtwo)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"},
        {"name": "루기아 (Lugia)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png"},
        {"name": "세레비 (Celebi)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/251.png"}
    ],
    "INTJ": [
        {"name": "뮤츠 (Mewtwo)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"},
        {"name": "후딘 (Alakazam)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png"},
        {"name": "팬텀 (Gengar)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png"}
    ],
    "ISTP": [
        {"name": "메타몽 (Ditto)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png"},
        {"name": "파비코리 (Altaria)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/334.png"},
        {"name": "라이츄 (Raichu)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png"}
    ],
    "ISFP": [
        {"name": "이상해씨 (Bulbasaur)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"},
        {"name": "피카츄 (Pikachu)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"},
        {"name": "이브이 (Eevee)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png"}
    ],
    "INFP": [
        {"name": "뮤 (Mew)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png"},
        {"name": "이상해꽃 (Venusaur)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png"},
        {"name": "리피아 (Leafeon)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/470.png"}
    ],
    "INTP": [
        {"name": "뮤츠 (Mewtwo)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"},
        {"name": "폴리곤 (Porygon)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/137.png"},
        {"name": "메타그로스 (Metagross)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/376.png"}
    ],
    "ESTP": [
        {"name": "리자몽 (Charizard)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png"},
        {"name": "망나뇽 (Dragonite)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png"},
        {"name": "꼬부기 (Squirtle)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"}
    ],
    "ESFP": [
        {"name": "피카츄 (Pikachu)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"},
        {"name": "푸린 (Jigglypuff)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png"},
        {"name": "고라파덕 (Psyduck)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/54.png"}
    ],
    "ENFP": [
        {"name": "피카츄 (Pikachu)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"},
        {"name": "이브이 (Eevee)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png"},
        {"name": "꼬부기 (Squirtle)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"}
    ],
    "ENTP": [
        {"name": "뮤츠 (Mewtwo)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"},
        {"name": "팬텀 (Gengar)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png"},
        {"name": "마기라스 (Tyranitar)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/248.png"}
    ],
    "ESTJ": [
        {"name": "거북왕 (Blastoise)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png"},
        {"name": "망나뇽 (Dragonite)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png"},
        {"name": "근육몬 (Machoke)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/67.png"}
    ],
    "ESFJ": [
        {"name": "럭키 (Chansey)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png"},
        {"name": "삐삐 (Clefairy)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/35.png"},
        {"name": "잠만보 (Snorlax)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png"}
    ],
    "ENFJ": [
        {"name": "루기아 (Lugia)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png"},
        {"name": "이상해꽃 (Venusaur)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png"},
        {"name": "피카츄 (Pikachu)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"}
    ],
    "ENTJ": [
        {"name": "리자몽 (Charizard)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png"},
        {"name": "망나뇽 (Dragonite)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png"},
        {"name": "뮤츠 (Mewtwo)", "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"}
    ]
}

# MBTI 유형 리스트
mbti_types = list(pokemon_recommendations.keys())
mbti_types.sort() # 순서대로 정렬

# 웹 앱의 제목 설정
st.set_page_config(
    page_title="💖 MBTI x 포켓몬 짝꿍 찾기 💖",
    page_icon="⚡️",
    layout="centered"
)

st.title("💖 MBTI x 포켓몬 짝꿍 찾기 💖")
st.markdown("당신의 MBTI에 딱 맞는 포켓몬 친구들을 찾아보세요!")
st.write("---")

# MBTI 선택 드롭다운
selected_mbti = st.selectbox(
    "당신의 MBTI 유형은 무엇인가요?",
    mbti_types,
    index=mbti_types.index("INFP") # 초기 선택값 설정 (예시)
)

st.write(f"### ✨ 당신의 MBTI는 **{selected_mbti}** 이군요!")
st.write(f"**{selected_mbti}** 유형에게 잘 어울릴 것 같은 포켓몬 친구들을 소개합니다!")

# 선택된 MBTI에 따른 포켓몬 추천
if selected_mbti:
    recommended_pokemons = pokemon_recommendations.get(selected_mbti, [])

    if recommended_pokemons:
        # 3단 컬럼으로 포켓몬 이미지와 이름을 나열
        cols = st.columns(3)
        for i, pokemon in enumerate(recommended_pokemons):
            with cols[i]:
                st.image(pokemon["image_url"], caption=pokemon["name"], use_column_width=True)
                st.markdown(f"<h4 style='text-align: center; color: #5B5B5B;'>{pokemon['name']}</h4>", unsafe_allow_html=True)
    else:
        st.warning("아직 해당 MBTI에 대한 포켓몬 추천 데이터가 없습니다. 곧 업데이트될 예정입니다!")

st.write("---")
st.markdown("Made with ❤️ by Your Name (or AI)") # footer
