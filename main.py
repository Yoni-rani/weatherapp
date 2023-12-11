import streamlit as st
import pandas as pd
import re

def main():
    st.title("내 생일에는 비가 올까🌂☔🎂?")

    # 사용자로부터 입력 받기
    month_day = st.text_input('생일을 적어주세요 (MM.DD):')

    if st.button("날씨를 알아보자"):
        # 입력 형식 확인
        if not re.match(r"\d{1,2}\.\d{1,2}", month_day):
            st.error("입력 형식이 잘못되었습니다. 'MM.DD' 형식으로 입력해주세요.")
            return

        # 엑셀 파일 경로 지정
        data = pd.read_csv('data/weather_.csv',encoding='cp949')

        # '일시' 열의 데이터를 datetime 타입으로 변환
        data['일시'] = pd.to_datetime(data['일시'], format='%Y-%m-%d')

        # '일시' 열의 데이터를 'YYYY.M.D' 형식의 문자열 변환
        data['일시'] = data['일시'].dt.strftime('%Y.%m.%d')

        # 변환된 월-일을 기반으로 데이터 필터링
        mask = (data['일시'].str.slice(start=5) == month_day)
        filtered_data = data.loc[mask]

        # 결과 출력
        st.write(filtered_data)

if __name__ == "__main__":
    main()
