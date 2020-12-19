from json.decoder import JSONDecodeError

from locust import HttpUser, task, between
import json
import redis
import random
import time

r = redis.StrictRedis(host="39.107.248.13", port=17396, db=0, password="Game$AaA@56912348")

# 是否睡眠
isSleep = False


class UserBehavior(HttpUser):
    def __init__(self, *args, **kwargs):
        print(now(),  " ", "__init__ start")
        super().__init__(*args, **kwargs)
        self.thirdId = None
        self.userId = None
        self.headers = None
        self.isCaptain = False
        self.conditionId = None
        self.roomId = None
        self.matching = False
        self.matchCount = 0
        print(now(),  " ", "__init__ end")

    def on_start(self):
        print(now(),  " ", "on_start start")
        self.enterLoad()
        # self.homeLoad()
        sleep(10)
        print(now(),  " ", "on_start end")

    @task
    def nullTask(self):
        sleep(1)
        pass

    # enter
    # @task(1)
    def enterLoad(self):
        thirdId = str(r.incr("locust-load-thirdId", amount=1))
        self.thirdId = thirdId

        data = self.enter(thirdId)
        userId = data['userId']
        headers = {"token": data['token'], "x-tag": "locust"}
        self.userId = userId
        self.headers = headers
        r.set(getTokenKey(userId), data['token'])


        # conditionId = self.updateTeamCondition()
        # self.conditionId = conditionId
        # self.turnCaptain()

        self.homeLoad()
        # sleep(20)

    # @task(2)
    def userHoemPage(self):
        self.getUserBase()
        self.getUserGameHistory()
        self.getUserGameTime()
        self.getUserOftenWay()
        self.getUserTeamCondition()
        self.getTeamLabel()
        # sleep(10)

    wait_time = between(30, 60)

    # @task(7)
    def homeLoad(self):
        self.getLevelUpgrade()
        self.getUserTeamInfo()
        self.teamHomePage()
        self.getTeamUnRecomment()
        self.updateTeamConditionSort()
        # sleep(10)

    # @task(2)
    # def matchRoomLoad(self):
    #     self.matchRoom(self.userId, self.conditionId, self.headers)
    #     sleep(getRandom(10, 20))
    #     self.matchRoomCancel(self.headers)
    #     sleep(10)

    # @task(1)
    def roomLoad(self):
        self.createRoom()
        sleep(1, 5)
        self.prepare(self.userId, self.roomId, self.headers)
        sleep(1, 5)
        self.getRoomInfo()
        sleep(1, 5)
        self.getRoomInfo()
        self.getRoomInfo()
        sleep(1, 5)
        self.unPrepare()
        sleep(1, 5)
        self.prepare(self.userId, self.roomId, self.headers)
        sleep(1, 5)
        self.teamHallUser()
        sleep(1, 5)
        self.teamHallUser()
        sleep(1, 5)
        self.teamHallUser()
        sleep(1, 5)
        for member in range(1, 5):
            pass
        sleep(1, 5)
        self.startGame()
        sleep(1,5)
        self.joinGame()
        sleep(1,5)
        self.prepare(self.userId, self.roomId, self.headers)
        sleep(1,5)
        self.teamHallRoom()
        sleep(1,5)
        self.teamHallRoom()
        sleep(1,5)
        self.teamHallRoom()
        self.startGame()
        sleep(1,5)
        self.joinGame()
        sleep(60)
        self.endGame()
        sleep(1,5)
        self.dissolveRoom()
        sleep(1,5)

    def redisLoad(self):
        self.client.get("/test/redisGet")
        self.client.get("/test/redisSet")

    # @task
    # def hall_load(self):
    #     self.createRoom()
    #     self.teamHallRoom()
    #     self.teamHallUser()
    #     self.dissolveRoom()


    # 模拟组队流程
    def patch(self):
        if self.isCaptain:
            self.captain()
        else:
            self.member()

    # 模拟队长流程
    def captain(self):
        self.getUserTeamInfo()
        if self.roomId is None:
            # 创建房间
            self.createRoom()
            sleep(3)
            self.prepare(self.userId, self.roomId, self.headers)
        sleep(2)
        self.getRoomInfo()
        roomInfo = self.getRoomInfo()
        members = roomInfo['members']
        # 三人发车
        if len(members) > 2:
            # 每个人都准备
            for member in members:
                memberUserId = member['userId']
                token = r.get(getTokenKey(memberUserId))
                memberHeaders = {"token": token, "x-tag": "locust"}
                self.prepare(memberUserId, self.roomId, memberHeaders)
            roomInfo = self.getRoomInfo()
            roomInfo = self.getRoomInfo()
            roomInfo = self.getRoomInfo()
            sleep(3)
            self.startGame()
            sleep(3)
            self.joinGame()
            sleep(3)
            self.endGame()
            sleep(3)
            self.dissolveRoom()
        elif  self.matchCount < 5:
            self.matchCount += 1
            sleep(2)
        else:
            # 每个人都准备
            for member in members:
                memberUserId = member['userId']
                token = r.get(getTokenKey(memberUserId))
                memberHeaders = {"token": token, "x-tag": "locust"}
                self.prepare(memberUserId, self.roomId, memberHeaders)
            roomInfo = self.getRoomInfo()
            roomInfo = self.getRoomInfo()
            roomInfo = self.getRoomInfo()
            sleep(3)
            self.startGame()
            sleep(3)
            self.joinGame()
            sleep(3)
            self.endGame()
            sleep(3)
            self.dissolveRoom()

    # 模拟队员流程
    def member(self):
        # 没进房间且没有匹配
        if self.roomId is None and self.matching is False:
            self.matchRoom()
            self.matching = True

    def test(self):
        thirdId = str(r.incr("locust-load-thirdId", amount=1))
        self.enter(thirdId)

    # 获取用户token和userId
    def enter(self, thirdId):
        nickname = "locust_" + thirdId
        avatar = "https://www.app10.com/upload/img/2020/04/02/5e859d7f20c6a.png"
        param = {"appId": 999, "thirdUserId": thirdId, "nickname": nickname, "avatar": avatar, "sex": 1,
                 "phone": "18500001234", "location": "趣星球", "device": None}
        resp = self.client.post("/api/team/third/enter", json=param)
        return getResData(resp)

    # 获取用户组队信息
    def getUserTeamInfo(self):
        print(now(),  " ", "getUserTeamInfo, userId:", self.userId)
        resp = self.client.get("/api/team/getUserTeamInfo", headers=self.headers, verify=False)
        data = getResData(resp)
        if data:
            self.roomId = data['roomId']

    # 成为队长
    def turnCaptain(self):
        print(now(), " turnCaptain, userId:", self.userId)
        resp = self.client.post("/api/team/third/turnCaptain", headers=self.headers, verify=False)
        data = getResData(resp)
        if data:
            self.isCaptain = True

    # 获取房间快捷语句
    def getRoomQuickTalk(self):
        print(now(),  " ", "getRoomQuickTalk, userId:", self.userId)
        resp = self.client.get("/api/team/getRoomQuickTalk")

    # 新增入队条件卡,修改时需要传conditionId、currentIndex、sort
    def updateTeamCondition(self):
        print(now(),  " ", "updateTeamCondition, userId:", self.userId)
        param = {"nickName": "", "serverType": getRandom(1, 3), "voiceType": getRandom(0, 3), "lines": [],
                 "jobLevel": 13, "captainJobLevels": [13]}
        resp = self.client.post("/api/team/updateTeamCondition", headers=self.headers, json=param)
        data = getResData(resp)
        if data:
            for d in data:
                if d['currentIndex'] == 0:
                    return d['conditionId']
        return None

    # 更新入队条件卡
    def updateTeamConditionSort(self):
        print(now(),  " ", "updateTeamConditionSort, userId:", self.userId)
        param = self.conditionId
        if param:
            resp = self.client.get("/api/team/updateTeamConditionSort", json=param, headers=self.headers)

    # 创建房间
    def createRoom(self):
        print(now(),  " ", "createRoom, userId:", self.userId)
        voiceType = getRandom(1, 3)
        #url = f"/api/team/createRoom?conditionId={self.conditionId}&roomType=1&voiceType={voiceType}"
        #resp_create = self.client.post(url, headers=self.headers)
        url = "/api/team/createRoom"
        params = {"voiceType": voiceType, "conditionId": self.conditionId, "roomType": 1}
        resp_create = self.client.post(url, data=params, headers=self.headers)
        data = getResData(resp_create)
        self.roomId = data

    # 准备
    def prepare(self, userId, roomId, headers):
        print(now(),  " ", "prepare, userId:", userId)
        params={"roomId": roomId}
        resp_prepare = self.client.post("/api/team/prepare", data=params, headers=headers)

    def unPrepare(self):
        print(now(),  " ", "unPrepare, userId:", self.userId)
        params = {"roomId": self.roomId}
        # 取消准备 unPrepare
        resp_cancel = self.client.post("/api/team/unPrepare", data=params, headers=self.headers)

    def getRoomInfo(self):
        params = {"roomId": self.roomId}
        res = self.client.get("/api/team/getRoomInfo", params=params, headers=self.headers)
        return getResData(res)

    def startGame(self):
        print(now(),  " ", "startGame, userId:", self.userId)
        params = {"roomId": self.roomId}
        resp_start_game = self.client.post("/api/team/startGame", data=params, headers=self.headers)

    def joinGame(self):
        print(now(),  " ", "joinGame, userId:", self.userId)
        params = {"roomId": self.roomId}
        resp_join_game = self.client.post("/test/joinGame", data=params, headers=self.headers)

    def endGame(self):
        print(now(),  " ", "endGame, userId:", self.userId)
        resp_end_game = self.client.post("/api/team/endGame", headers=self.headers)

    def dissolveRoom(self):
        print(now(),  " ", "dissolveRoom, userId:", self.userId)
        #  关闭房间 dissolveRoom
        params = {"roomId": self.roomId}
        resp_dissolve = self.client.post("/api/team/dissolveRoom", data=params, headers=self.headers)
        self.roomId = None

    def matchRoom(self, userId, conditionId, headers):
        print(now(),  " ", "matchRoom, userId:", userId)
        params = {"conditionId": conditionId, "matchType": 1}
        self.client.get("/api/team/matchRoom", params=params, headers=headers)

    def getGamingRoomInfo(self):
        print(now(),  " ", "matchRoom, userId:", self.userId)
        res = self.client.get("/api/team/getGamingRoomInfo", header=self.headers)

    # 邀请大厅-用户列表
    def teamHallUser(self):
        print(now(), " ", "teamHallUser, userId:", self.userId)
        param = {"pageNum": getRandom(0, 5), "pageSize": 25, "roomId": self.roomId, "inviteType": 0}
        roomId = self.roomId
        if roomId:
            res = self.client.get("/api/team/v1/teamHallUser", params=param, headers=self.headers)

    # 队伍大厅
    def teamHallRoom(self):
        print(now(), "  ", "teamHallRoom, userId:", self.userId)
        # captainJobLevels、captainLevels、voiceType 非必填
        query = {"pageNum": getRandom(0, 5), "pageSize": 20}
        res = self.client.post("/api/team/v1/teamHallRoom", json=query, headers=self.headers)

    # 获取当前用户还没有评论的组队id
    def getTeamUnRecomment(self):
        print(now(), " ", "getTeamUnRecomment, userID: ", self.userId)
        res = self.client.get("/api/team/getTeamUnRecomment", headers=self.headers)

    # 组队首页信息
    def teamHomePage(self):
        print(now(), "  ", "teamHomePage, userId:", self.userId)
        res = self.client.get("/api/team/teamHomePage", headers=self.headers)

    # 获取用户组队信息 uid\in\tm\deviceId
    def getUserTeamInfo(self):
        print(now(), "  ", "getUserTeamInfo, userId:", self.userId)
        res = self.client.get("/api/team/getUserTeamInfo", headers=self.headers)

    # 用户等级升级
    def getLevelUpgrade(self):
        print(now(), "  ", "getLevelUpgrade, userId:", self.userId)
        res = self.client.get("/api/team/user/getLevelUpgrade", headers=self.headers)

    # 用户主页-用户基本信息
    def getUserBase(self):
        print(now(), "  ", "getUserBase, userId:", self.userId)
        params = {"userId": self.userId}
        res = self.client.get("/api/team/user/getUserBase", params=params, headers=self.headers)

    # 用户主页-历史组队
    def getUserGameHistory(self):
        print(now(), "  ", "getUserGameHistory, userId:", self.userId)
        params = {"pageNum": 0, "pageSize": 30, "userId": self.userId}
        res = self.client.get("/api/team/user/getUserGameHistory", params=params, headers=self.headers)

    # 用户主页-组队时光
    def getUserGameTime(self):
        print(now(), "  ", "getUserGameTime, userId:", self.userId)
        params = {"userId": self.userId}
        res = self.client.get("/api/team/user/getUserGameTime", params=params, headers=self.headers)

    # 用户主页-常玩路线
    def getUserOftenWay(self):
        print(now(), "  ", "getUserOftenWay, userId:", self.userId)
        params = {"userId": self.userId}
        res = self.client.get("/api/team/user/getUserOftenWay", params=params, headers=self.headers)

    # 用户主页-在玩账号
    def getUserTeamCondition(self):
        print(now(), "  ", "getUserTeamCondition, userId:", self.userId)
        params = {"userId": self.userId}
        res = self.client.get("/api/team/user/getUserTeamCondition", params=params, headers=self.headers)

    # 用户主页-获取用户标签
    def getTeamLabel(self):
        print(now(), "  ", "getTeamLabel, userId:", self.userId)
        params = {"userId": self.userId}
        res = self.client.get("/api/team/getTeamLabel", params=params, headers=self.headers)

    def matchRoomCancel(self, headers):
        res = self.client.get("/api/team/matchRoomCancel", headers=headers)

# 获取响应实体
def getRes(resp):
    if resp.status_code == 200:
        try:
            return json.loads(resp.text)
        except JSONDecodeError:
            raise ValueError("请求反序列化异常 text:", resp.text)
    else:
        raise ValueError("http请求异常, resp.status_code", resp.status_code, "resp.text:", resp.text)


# 直接获取响应实体的data部分
def getResData(resp):
    res = getRes(resp)
    if res['code'] == '0':
        return res['data']
    else:
        raise ValueError("业务异常", res)


def sleep(first, *last):
    if isSleep:
        if last:
            time.sleep(getRandom(first, last))
        else:
            time.sleep(first)


def getRandom(first, last):
    return int(random.random() * (last - first) + first)


if __name__ == "__main__":
    pass


def getTokenKey(userId):
    return "locust-load-userId-" + str(userId)


def now():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
