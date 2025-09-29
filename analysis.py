import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv("data/gdp_data.csv")
    print("数据预览：")
    print(data.head())
    print("\n描述统计：")
    print(data.describe())

    # GDP 趋势图
    plt.figure(figsize=(8,5))
    plt.plot(data['Year'], data['GDP'], marker='o', linestyle='-')
    plt.title('GDP Trend')
    plt.xlabel('Year')
    plt.ylabel('GDP (Million RMB)')
    plt.grid(True)
    plt.savefig('gdp_trend.png', bbox_inches='tight')
    plt.close()

    # 计算增长率
    data['GrowthRate'] = data['GDP'].pct_change() * 100

    # 增长率柱状图
    plt.figure(figsize=(8,5))
    plt.bar(data['Year'].astype(str), data['GrowthRate'])
    plt.title('GDP Growth Rate (%)')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate (%)')
    plt.savefig('gdp_growth_rate.png', bbox_inches='tight')
    plt.close()

    print("\n已生成图片：gdp_trend.png, gdp_growth_rate.png")

if __name__ == '__main__':
    main()
