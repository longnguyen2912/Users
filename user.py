class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"User's first name: {self.first_name}")
        print(f"User's last name: {self.last_name}")
        print(f"User's email: {self.email}")
        print(f"User's age: {self.age}")
        print(f"User's a reward member: {self.is_rewards_member}")
        print(f"User's gold card points: {self.gold_card_points}")
    
    def enroll(self):
        self.is_rewards_member = True
        if self.is_rewards_member == True:
            self.is_rewards_member = False
            print("User already a member.")
        return self.is_rewards_member   
    def spend_points(self,amount):
        self.gold_card_points = self.gold_card_points + amount
        return self.gold_card_points

user1 = User("John", "Doe", "johndoe@gmail.com", 28)
user1.enroll()
user1.spend_points(2000)
user1.display_info()
user1.enroll(True)
user1.display_info()
user1.enroll()
user1.display_info()