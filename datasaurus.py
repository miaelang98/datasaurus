import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 온라인 원본 데이터 로드
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-10-13/datasaurus.csv"
df = pd.read_csv(url)

# 2. 각 데이터 세트별 통계치 계산 및 출력
print(f"{'Dataset':<12} | {'X Mean':<8} | {'Y Mean':<8} | {'X SD':<8} | {'Y SD':<8} | {'Corr':<8}")
print("-" * 70)

stats_list = []
for name in df['dataset'].unique():
    subset = df[df['dataset'] == name]
    x_mean = subset['x'].mean() #데이터 중심 위치 찾기
    y_mean = subset['y'].mean()
    x_std = subset['x'].std() #데이터가 중심에서 얼마나 퍼져 있는지 측정 (표준편차)
    y_std = subset['y'].std() #x가 커질 때 y도 같이 커지는지 확인 / 두 변수의 선형적 관계를 -1~1사이 숫자로 나타내기
    corr = subset['x'].corr(subset['y'])
    
    print(f"{name:<12} | {x_mean:<8.2f} | {y_mean:<8.2f} | {x_std:<8.2f} | {y_std:<8.2f} | {corr:<8.2f}")

# 3. 시각화 (FacetGrid 활용)
sns.set_theme(style="whitegrid")
g = sns.FacetGrid(df, col="dataset", col_wrap=4, height=3)
g.map(sns.scatterplot, "x", "y", s=15, alpha=0.8, color="#2c3e50")

# 디자인 정돈
g.set_titles("{col_name}")
plt.subplots_adjust(top=0.92)
g.fig.suptitle("The Datasaurus Dozen: Same Statistics, Different Visuals", fontsize=18)

plt.show()

plt.savefig("datasaurus_result.png", dpi=300)
print("그래프가 'datasaurus_result.png' 파일로 저장되었습니다!")