def dfs(city, dic, route, total):
    if len(route) == total + 1:
        return route
    if len(dic[city]) == 0:
        return route
    cities = dic[city]
    cities.sort()
    for c in cities:
        dic[city].remove(c)
        route.append(c)
        print(c, dic, route, total)
        return dfs(c, dic, route, total)
        if len(result) == total + 1:
            return result
        dic[city].append(c)
        route.pop(-1)
    return route
def solution(tickets):
    dic = dict()
    total = len(tickets)
    for ticket in tickets:
        if ticket[0] not in dic:
            dic[ticket[0]] = [ticket[1]]
        else:
            dic[ticket[0]].append(ticket[1])

    return dfs("ICN", dic, ["ICN"], total)

print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))