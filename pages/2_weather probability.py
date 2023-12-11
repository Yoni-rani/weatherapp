import streamlit as st
import pandas as pd

st.title("통계적 확률을 이용하여 강수확률을 계산해보자‼️✏️🌧️")  # 웹 페이지 제목

# 사용자로부터 의견 입력 받기
opinions = []
@st.cache(allow_output_mutation=True)  # 캐싱 데코레이터 추가
def get_opinions():
    # 빈 리스트 반환
    return []

opinion = st.text_input('강수확률이 60%라면 아침에 우산을 들고 나갈지 얘기해봅시다. 내가 생각하는 강수 확률의 60%의 의미를 적어볼까요?')
    
    # 제출 버튼이 클릭되면, 의견을 리스트에 추가
if st.button('제출'):
    if opinion:  # 입력이 비어있지 않은 경우
        opinions.append(opinion)
        st.success('의견이 제출되었습니다.')
    else:  # 입력이 비어있는 경우
        st.error('의견을 입력해주세요.')
    
    # 제출된 의견 출력
    st.subheader('제출된 의견:')
    for opinion in opinions:
        st.write(opinion)

# CSV 파일 로드
file_path = r'C:\Users\yeonhee\project2\weather_.csv'
data = pd.read_csv(file_path,encoding='cp949')

# NA 값을 0으로 대체
data_filled = data.fillna(0)

# 사용자로부터 입력 값을 받습니다.
st.text("기상 조건을 입력하여 조건이 비슷한 날들의 강수량 데이터를 통해 확률을 계산합니다.")
input_avg_temp = st.number_input('평균기온를 입력하세요:', value=0.0)
input_avg_temperature = st.number_input('평균습도를 입력하세요:', value=0.0)
input_error_range = st.number_input('오차 범위를 입력하세요:', value=0.0)

if st.button('확인'):
    # 입력한 오차 범위에 있는 데이터를 필터링합니다.
    within_range = data_filled[
        (data_filled['평균기온'] >= input_avg_temp - input_error_range) & (data_filled['평균기온'] <= input_avg_temp + input_error_range) &
        (data_filled['평균습도'] >= input_avg_temperature - input_error_range) & (data_filled['평균습도'] <= input_avg_temperature + input_error_range)
    ]

    # 강수량이 0인 데이터의 개수를 세어줍니다.
    zero_precipitation_count = within_range[within_range['강수량'] == 0].shape[0]

    # 강수량이 0이 아닌 데이터의 개수를 세어줍니다.
    non_zero_precipitation_count = within_range[within_range['강수량'] != 0].shape[0]

    # 결과 출력
    st.write(f"강수량이 0인 데이터의 개수 (모든 조건이 ±{input_error_range} 범위 내일 때): {zero_precipitation_count}")
    st.write(f"강수량이 0이 아닌 데이터의 개수 (모든 조건이 ±{input_error_range} 범위 내일 때): {non_zero_precipitation_count}")


    # 분모가 0인 경우 예외 처리
    if zero_precipitation_count + non_zero_precipitation_count == 0:
        st.write("주어진 상황에 맞는 데이터가 없습니다.😢")
    else:
        st.write(f"확률 : {non_zero_precipitation_count/(zero_precipitation_count+non_zero_precipitation_count)*100}" )
        if input_avg_temp < 0:
            st.write("눈이 옵니다.❄️☃️")
            st.image('images/snow.gif')
        elif input_avg_temp >= 0:
            st.write("비가 옵니다.🌧️☔")
            st.image('images/rain.gif')
    # 평균 기온에 따른 메시지 출력
    