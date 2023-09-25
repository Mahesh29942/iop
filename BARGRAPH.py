import matplotlib.pyplot as plt
plt.bar(df['NAME'], df['SOCIAL'])
plt.xlabel('NAME')
plt.ylabel('Maths Score')
plt.title('Maths Scores')
plt.xticks(rotation=0)
plt.show()
