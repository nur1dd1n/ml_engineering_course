import matplotlib.pyplot as plt 
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.show()



plt.plot(x, y)
plt.title("Рост значений")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()



y2 = [5, 15, 20, 25]

plt.plot(x, y)
plt.plot(x, y2)
plt.show()




plt.scatter(x, y)
plt.show()


scores = [80, 85, 90, 70, 75, 95, 88]

plt.hist(scores, bins=5)
plt.show()

