class Athlete:
    def __init__(self,name,event,record):
        
        self.name = name
        self.event = event
        self.record = record
    
    def update_record(self, new_record):
        if new_record < self.record:
            print(f"{self.name}님의 새로운 기록:{new_record}(기존기록 : {self.record})")
            self.record = new_record
        else:
            print(f"{self.name}님의 기록은 업데이트 되지 않았습니다.(현재 기록 : {self.record})")
    
    def display_info(self):
        print(f"{self.name}")
        print(f"{self.event}")
        print(f"{self.record}")