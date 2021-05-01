import pandas as pd

# 데이터 프레임 만들기
# 1)
df1 = pd.DataFrame({
    'title': ['batman begins', 'about time', 'matrix'],
    'genres': ['action', 'drama', 'science fiction'],
    'released': [2005, 2013, 1999]},
    index=[1, 2, 3]
)

print(df1)

# 2)
movie_list = [
    ['batman begins', 'action', 2005],
    ['about time', 'drama', 2013],
    ['matrix', 'science fiction', 1999]
]
df2 = pd.DataFrame(movie_list, columns=['제목', '장르', '출시'])
print(df2)

# csv파일 불러오기
player_df = pd.read_csv('data/transfermarket100.csv')
print(player_df)

# 웹에 있는 파일 불러오기
# -> pd.read_csv('파일 주소')

# 데이터 뜯어보기
print(player_df.shape)  # (행(rows), 열(columns))

# (rows, columns) = player_df

print(player_df.info())  # 데이터에 대한 정보를 보여줌

player_df.head()  # default 5
player_df.tail()  # default 5

# 인자로 원하는 숫자를 넣으면 head는 처음부터 인자수만큼, tail은 마지막에서 인자수만큼의 데이터를 가져온다

# 여러 개 컬럼 이름 선택하기 - df[]안에 리스트로 삽입
print(player_df[['name', 'age']][:10])
print(player_df[['ranking', 'name', 'club']].head(10))

# iloc & local
print(player_df[:5])
print(player_df.iloc[: 5])  # 마지막(5)가 안들어간다
print(player_df.loc[: 5])  # 마지막(5)가 들어간다

print(player_df.loc[15, 'name'])  # Heung-min Son

print(player_df.loc[10:20, ['name', 'position', 'club', 'market_value']])

# 조건 인덱싱
print(player_df['age'] >= 25)

print(player_df[player_df['age'] >= 25])

# 소속팀이 토트넘인 선수
print(player_df[player_df['club'] == 'Tottenham Hotspur'])

# loc 조건으로 나이가 30이상인 선수의 'name'과 'value'를 가져오세요.¶
print(player_df.loc[player_df['age'] >= 30, ['name', 'age', 'market_value']])

# 데이터 프레임 정렬하기와 컬럼 바꾸기


# 데이터 프레임 통계와 groupby()
