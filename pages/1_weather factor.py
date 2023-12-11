import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import koreanize_matplotlib

def main():
    st.title("강수량에 영향을 주는 요소는 무엇일까❓🤔🌧️")  # 웹 페이지 제목

    # 사용자로부터 파일 업로드 받기
    uploaded_file = st.file_uploader("기상청 데이터를 업로드 해주세요", type=['csv'])

    if uploaded_file is not None:
        try:
            # pandas를 이용하여 데이터를 읽기
            if uploaded_file.type == 'application/vnd.ms-excel':
                data = pd.read_excel(uploaded_file)
            else:
                data = pd.read_csv(uploaded_file,encoding='cp949')

            # 사용자로부터 x축과 y축 데이터 선택 받기
            x_axis = st.radio('x축에 들어갈 데이터를 선택하세요:', data.columns)
            y_axis = st.radio('y축에 들어갈 데이터를 선택하세요:', [col for col in data.columns if col != x_axis])

            if st.button("산점도"):  # 버튼이 눌리면
                fig, ax = plt.subplots()
                ax.scatter(data[x_axis], data[y_axis])
                ax.set_xlabel(x_axis)
                ax.set_ylabel(y_axis)
                st.pyplot(fig)  # 산점도 출력
                correlation = data[[x_axis, y_axis]].corr().iloc[0, 1]
                st.write(f" {x_axis} 와 {y_axis} 의 상관계수는 {correlation:.2f} 입니다.")
                st.image('images/cor.png')

        except Exception as e:
            st.write("There was an error in loading the file.")
            st.write(e)

if __name__ == "__main__":
    main()