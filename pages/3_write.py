import streamlit as st
import pandas as pd

# 의견을 저장할 빈 리스트 생성
opinions = []

def get_opinions():
    # 빈 리스트 반환
    return []

def main():
    st.title("생각을 적어볼까요❓💭")  # 웹 페이지 제목

    # 캐싱된 리스트 가져오기
    opinions = get_opinions()

    # 여러 개의 텍스트 입력 칸 만들기
    opinion1 = st.text_input('1.강수확률은 통계적 확률로 계산합니다."비올 확률이 60%이다"의 의미를 이와 연결지어 적어주세요.')
    opinion2 = st.text_input('2.오늘의 온도와 습도를 입력해보고 데이터로 구한 강수확률과 실제 예보된 강수확률을 비교해봅시다. 어떤 차이가 있나요? 차이가 있다면 그 이유는 무엇이라고 생각하나요?')
    opinion3 = st.text_input('3.실제 기상청에서는 강수 확률을 어떻게 구할 것같나요?')
    
    # 각각의 의견을 제출하기 위한 버튼 만들기
    if st.button('1번 응답 제출'):
        if opinion1:  # 입력이 비어있지 않은 경우
            opinions.append(opinion1)
            st.success('1번 응답이 제출되었습니다.')
        else:  # 입력이 비어있는 경우
            st.error('1번 응답을 입력해주세요.')
    if st.button('2번 응답 제출'):
        if opinion2:  # 입력이 비어있지 않은 경우
            opinions.append(opinion2)
            st.success('2번 응답이 제출되었습니다.')
        else:  # 입력이 비어있는 경우
            st.error('2번 응답을 입력해주세요.')
    if st.button('3번 응답 제출'):
        if opinion3:  # 입력이 비어있지 않은 경우
            opinions.append(opinion3)
            st.success('3번 응답이 제출되었습니다.')
        else:  # 입력이 비어있는 경우
            st.error('3번 응답을 입력해주세요.')
    
    # 제출된 의견 출력
    st.subheader('제출된 의견:')
    for opinion in opinions:
        st.write(opinion)


    st.text('실제 기상청에서는 강수 확률을 어떻게 계산할까요? 왜 일기예보를 예측하는 것이 어려울까요?')
    st.text('아래 동영상에서 확인해봅시다.')
    st.video('https://www.youtube.com/watch?v=klZNqI93rtc')

if __name__ == "__main__":
    main()