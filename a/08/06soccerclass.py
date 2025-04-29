# 06/29 파이썬 수업
# 객체지향 프로그래밍 실습


class SoccerPlayer(object):
    # 생성자 constructor
    # 객체 object가 자동 생성
    def __init__(self,name,position,back_number):
        self.name=name
        self.position=position
        self.back_number=back_number
        print("init 함수 실행")

    def change_back_number(self,new_number):
        print(f'선수 번호 교체 : {self.back_number} => {new_number}')
        self.back_number=new_number

    def __str__(self):
        return f"저의 이름은 {self.name}, 위치는 {self.position}, 번호는 {self.back_number} 입니다"

# SoccerPlayer 클래스가 jh 오브젝트를 생성함
# 클래스의 생성함수 constructor가 실행됨
jh = SoccerPlayer(name="A", position="MF", back_number=10)

# jh 객체를 출력
print(jh)

# jh 객체의 name을 출력
print(jh.name)

# 백넘버 교체
jh.change_back_number(5)

# 교체된 백넘버 확인
print(f'{jh.change_back_number=}')

names=["Q","W","E","R","T"]
positions=["MF","DF","CF","WF","GK"]
numbers=[10,9,8,7,1]

players=[[name,position,number] for name,position,number in zip(names,positions,numbers)]
print(players)
print(players[0])

# 첫번째 선수로 Q 생성
Q=SoccerPlayer(players[0][0],players[0][1],players[0][2])
print(Q.name)

# 선수들의 리스트 생성
player_objects=[SoccerPlayer(name,position,number) for name,position,number in zip(names,positions,numbers)]
print(player_objects[0])

# 첫번째 선수의 이름
print(player_objects[0].name)

# 모든 선수의 이름, 포지션, 번호 출력
for player in player_objects:
    print(player)

# print(player_objects[0])
# print(player_objects[1])
# print(player_objects[2])
# print(player_objects[3])
# print(player_objects[4])






