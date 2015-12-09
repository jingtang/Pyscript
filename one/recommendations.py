# -*- coding: utf-8 -*-
from math import sqrt
import sys
critics = {'Lisa Rose': {'lady in the water': 2.5, 'Snake on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You,Me and Dupree': 2.5, 'The Night Listener': 3.0},
		   'Gene Seymour': {'lady in the water': 3.0, 'Snake on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 'You,Me and Dupree': 3.5},
	       'Michael Phillips': {'lady in the water': 2.5, 'Snake on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0},
		   'Claudia Puig': {'Snake on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 4.0, 'You,Me and Dupree': 2.5, 'The Night Listener': 4.5},
		   'Mick LaSalle': {'lady in the water': 3.0, 'Snake on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You,Me and Dupree': 2.0},
	       'Jack Mattews': {'lady in the water': 3.0, 'Snake on a Plane': 4.0, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 'You,Me and Dupree': 3.5},
		   'Toby': {'Snake on a Plane': 4.5, 'You,Me and Dupree': 1.0, 'Superman Returns': 4.0}}

#
#计算两人偏好空间。两人在坐标轴中距离越近，两人的喜好度就越相似
#
#欧几里得距离法
#指在m维空间中两个点之间的真实距离，或者向量的自然长度（即该点到原点的距离）。在二维和三维空间中的欧氏距离就是两点之间的实际距离
#0ρ = sqrt( (x1-x2)^2+(y1-y2)^2 )
#######
def sim_distance(ref, person1, person2):
    sim = {}
    for item in ref[person1]:
        if item in ref[person2]:
            sim[item] = 1

    #两者无共同相似之处返回0
    if len(sim) == 0:
        return 0
    #计算所有差值的平方和
    sum_of_squares = sum([pow(ref[person1][item]-ref[person2][item], 2)
                          for item in ref[person1] if item in ref[person2]])
    return 1/(1+sqrt(sum_of_squares))

#皮尔逊相关度评价
#判断两组数据与某一直线拟合程度的一种度量
#返回两人的皮尔逊相关度
def sim_person(ref, person1, person2):
    si = {}
    #获取双方都评价过的产品
    for item in ref[person1]:
        if item in ref[person2]:
            si[item] = 1
    #相同的数量
    n = len(si)

    #无共同处返回1
    if n == 0:
        return 1

    #有共同处
    #1对所有偏好求和
    sum1 = sum([ref[person1][item] for item in si])
    sum2 = sum([ref[person2][item] for item in si])
    #2对所有偏好求平方和
    sum1sq = sum([pow(ref[person1][item], 2) for item in si])
    sum2sq = sum([pow(ref[person2][item], 2) for item in si])
    #求乘积和
    pSum = sum([ref[person1][item] * ref[person2][item] for item in si])

    #计算皮尔逊评价值
    num = pSum - (sum1 * sum2/n)
    den = sqrt((sum1sq - pow(sum1, 2)/n) * (sum2sq - pow(sum2, 2)/n))
    if den == 0:
        return 0
    r = num/den
    return r

#为评论者打分
def topMatches(ref, person, n):
    scores = [(sim_person(ref, person, other), other) for other in ref if other != person]
    scores.sort()
    scores.reverse()
    #返回前N名评分
    return scores[0:n]

#生成相近物品的集合
def cereteSimilarItems(p, n = 10):
    return 0


#获得推荐
def getRecommendedItem(p, itemMatch, user):
    #某用户评分集合
    userRatings = p[user]
    #
    scores = {}
    #
    totalSim = {}


def loadMovieLens():
  #  path = r"E:\work file\ml-100k"
    movies = {}
    #获取影片标题
    for line in open('E:/work file/ml-100k/u.txt', 'r', encoding = 'utf-8'):
        (id, title) = line.split('|')[0:2]
        movies[id] = title
    #加载数据
    p = {}
    for line in open("E:/work file/ml-100k/u.data", 'r', encoding = 'utf-8'):
        (user, movieid, rating, ts) = line.split("\t")
        p.setdefault(user, {})
        p[user][movies[movieid]] = float(rating)
    return p





if __name__ == "__main__":
    print(sim_distance(critics, "Lisa Rose", "Gene Seymour"))
    print(sim_person(critics, "Lisa Rose", "Gene Seymour"))
    print(topMatches(critics, "Toby", 5))
    # print(sys.getdefaultencoding())
    per = loadMovieLens()
    print(len(per))
    print(per['810'])