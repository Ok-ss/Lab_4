from random import randint

class State:
    SLEEP = 0
    EAT = 1
    STUDY = 14
    WORK_OUT = 2
    LISTEN_TO_MUSIC = 3
    RELAX_ALONE = 5
    TALK_TO_FRIENDS = 6
    RECOVERY = 12

class LabRat:
    days = []

    def __init__(self, ) -> None:
        self.hunger = 0
        self.energy = 0 
        self.resource = 100
        self.social_battery = 100
        self.state = State.SLEEP


    @classmethod
    def day_counter(cls):
        if len(cls.days) > 6:
            while cls.days:
                cls.days.remove(1)
        cls.days.append(1)
        return len(cls.days)
    
    @staticmethod
    def figure_out_a_day(num):
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', \
                'Friday', 'Saturday', 'Sunday']
        return week[num-1]

    def live_a_day(self):
        week_day = self.day_counter()
        print(f'It`s {self.figure_out_a_day(week_day)}!')

        for hour in range(48):
            if self.hunger >= 6:
                self.social_battery -= 10 

            hour = hour/2
            print(f' {int(hour)}:{30 if hour != int(hour) else "00"}:')

            if self.state == State.SLEEP:
                #Put sth for sunday & tuesday here
                if self.energy < 12:
                    self.energy += 1
                    self.social_battery += 5
                self.hunger += 0.25

                if hour == 6 and week_day < 6:
                    print('  *6am alarm ringing*')
                    if self.energy in [9, 12, 15]:
                        print('  Goodbye drem world, hello reality')
                        self.state = State.WORK_OUT
                    else:
                        print('  Too bad, I missed that')

                elif hour == 7 and week_day < 6:
                    print('  *7am alarm ringing*')
                    print('  Now, I have to wake up')
                    self.state = State.EAT
                
                elif week_day > 5 and hour == 9:
                    print('  Time to wake up')
                    if week_day == 6:
                        self.state = State.WORK_OUT
                    else:
                        self.state = State.EAT
                
                else:
                    print('  zzzz....')
                continue
            if self.state == State.WORK_OUT:
                sudden_injury = not randint(0, 200)
                if sudden_injury:
                    print('  Looks like I have to rest')
                    self.state = State.RELAX_ALONE


                if hour == 7 or hour == 10:
                    print('  Great morning warmup. It`s going to give me energy for the day')
                    self.energy += 3
                    self.state = State.EAT
                elif hour == 15 or hour == 17:
                    print('  Time to refresh my mind with some exercises')
                else:
                    print('  Working out')
                
                self.hunger += 1.5
                if hour == 16.5:
                    print('  That`s enough for now')
                    self.state = State.STUDY
                if hour == 18.5:
                    print('  That`s enough for now')
                    self.state = State.LISTEN_TO_MUSIC
                
                self.social_battery += 5
                self.hunger += 0.5
                continue

            if self.state == State.EAT:
                if hour < 11:
                    self.hunger -= 5
                    print('  Let`s have some breakfast')
                    print('  *Eats breakfast*')
                    print('  Breakfast was nice.', end = ' ')
                    if week_day < 6 and week_day != 2:
                        print('Time to go to univercity')
                        self.state = State.LISTEN_TO_MUSIC
                    elif week_day == 2:
                        print('I still have some time before I have to go')
                        self.state = State.RELAX_ALONE
                    elif week_day == 6:
                        print('It`s time to organize my conspects')
                        self.state = State.STUDY
                    else:
                        print('The whole day in front of me')
                        if self.social_battery >= 50:
                            self.state = State.TALK_TO_FRIENDS
                        else:
                            self.state = State.RELAX_ALONE

                elif 11 < hour < 18:
                    self.hunger -= 7
                    print('  Let`s have some dinner')
                    print('  *Eats dinner*')
                    print('  Dinner was tasty. Gotta carry on')
                    if week_day < 6 and week_day != 3:
                        self.state = State.STUDY
                    elif week_day == 3:
                        self.state = State.RELAX_ALONE
                    elif week_day == 6:
                        self.state = State.RELAX_ALONE
                    else:
                        print('The whole day in front of me')
                        if self.social_battery >= 50:
                            self.state = State.TALK_TO_FRIENDS
                        else:
                            self.state = State.RELAX_ALONE
                else:
                    self.hunger -= 7
                    print('  Let`s have some supper')
                    print('  *Eats supper*')
                    print('  Supper was delicious it`s time to relax now')
                    if week_day == 6:
                        self.state = State.LISTEN_TO_MUSIC
                    elif self.social_battery < 50 or week_day == 3:
                        self.state = State.RELAX_ALONE
                    else:
                        self.state = State.TALK_TO_FRIENDS

                self.hunger += 0.5
                continue

            if self.state == State.STUDY:
                if (week_day in [1, 3, 4, 5] and hour == 8.5) or (week_day == 2 and hour == 10):
                    print('  Great. I`m at uni.')
                burning_out = not randint(0, 150)
                if burning_out:
                    print('Now I`m burnt out. I need to go to the park')
                    self.resource = 0
                    self.state = State.RECOVERY
                    continue

                match week_day:
                    case 1:
                        if 8 < hour < 15 or hour > 16:
                            print('  *Studies Basics of programming*')
                        else:
                            print(f'  *Studies English*')
                        if hour == 19:
                            self.state = State.LISTEN_TO_MUSIC
                    case 2:
                        if hour in [10, 10.5, 11, 18.5, 19, 19.5]:
                            print('  *at a СЯ-шка lecture*')
                        else:
                            print(f'  *prepares for some upcomming tests*')
                        if hour == 14.5:
                            self.state = State.WORK_OUT
                        if hour == 19.5:
                            self.state = State.LISTEN_TO_MUSIC

                    case 3:
                        if hour == 8.5:
                            print(f'  Just some lectures today')
                        if 8 < hour < 10:
                            print('  *Listening to Пані Юля*')
                        if 9.5 < hour < 11.5:
                            print('  *On an Economical analysys lecture*')
                        if 11 < hour:
                            print('  *Solving economical problems*') 
                        if hour == 13:
                            self.state = State.LISTEN_TO_MUSIC
                    case 4:
                        if hour == 8.5:
                            print('  It`s Calculus day')
                        if hour < 14 or hour > 19:
                            print('  *Studies calculus*')
                        elif hour < 16.5:
                            print('  *Studies English*')
                        if hour == 16.5:
                            print('  I`ll have a small break')
                            self.state = State.WORK_OUT
                    case 5:
                        if hour == 8.5:
                            print('   Let me enjoy some logic from descrete maths \
                              and utter chaos from economical analysys')
                        if 9.5 < hour < 12:
                            print('  *Studying economical analysys*')
                        elif 8 < hour < 15 or hour > 19:
                            print('  *Studyng descrete maths*')
                        elif 14.5 < hour < 16.5:
                            print('  *Studying english*')
                        if hour == 16:
                            self.state = State.LISTEN_TO_MUSIC
                    case 6:
                        print('  *Looks through conspects*')
                    
                    case 7:
                        print('  *works while panicking*')

                if hour == 13.5:
                    self.state = State.EAT
                
                if hour == 23.5:
                    self.state = State.SLEEP
                self.hunger += 0.5
                continue
                
            if self.state == State.LISTEN_TO_MUSIC:
                if 0 < week_day < 6:
                    print('  Let`s listen to some music', end = ' ')
                    if 0 < hour < 12:
                        print('on my way to UCU')
                        self.state = State.STUDY
                    else:
                        print('on my way from UCU')
                        if week_day != 5:
                            self.state = State.EAT
                        else:
                            self.state = State.RELAX_ALONE
                else:
                    if hour == 20.5:
                        print('  Let`s listen to some music \
                              just for the fun of it')
                    print('  *listens to music*')
                    if hour == 23.5:
                        self.state = State.SLEEP
                
                self.hunger += 0.5
                continue
                

            if self.state == State.RELAX_ALONE:
                forgotten_deadline = not randint(0, 60)
                if forgotten_deadline and hour != 23.5:
                    print('  I forgot a deadline!!')
                    self.state = State.STUDY
                    continue

                match week_day:
                    case 1 | 4:
                        if hour == 20.5:
                            print('  Let me have some alone time.')
                        print('  *Plays the guitar*')
                    case 2:
                        if hour == 8 or hour == 21:
                            print('  Let me have some alone time.')
                        print('  *Reads*')
                        if hour == 9:
                            print('  Time to go to uni')
                            self.state = State.LISTEN_TO_MUSIC
                    case 3:
                        if hour == 14:
                            print('  Let me have some alone time.')
                        elif hour == 19.5:
                            self.state = State.EAT
                        elif hour == 16 and self.social_battery >= 50:
                            self.state = State.TALK_TO_FRIENDS
                        
                        if 14 <= hour <= 16:
                            print('  *reads*')
                        elif hour > 19:
                            print('  *Watches YouTube*')
                        else:
                            print('  *plays the guitar*')
                    case 5:
                        if hour == 17:
                            print('  Finally some time for computer games')
                        print('  *plays computer games*')
                    case 6:
                        print('  *Does whatever comes to mind*')
                        if hour == 19.5:
                            self.state = State.EAT
                    case 7:
                        if hour == 13.5 or hour == 19.5:
                            self.state = State.EAT
                        elif hour < 20:
                            print('  *Out on an event*')
                        else:
                            print('  *Watches a film*')
                        

                                                
                if hour == 23.5:
                    self.state = State.SLEEP
                
                self.hunger += 0.5
                continue
    

            if self.state == State.TALK_TO_FRIENDS:
                
                forgotten_deadline = not randint(0, 60)
                if forgotten_deadline and hour != 23.5:
                    print('  I forgot a deadline!!')
                    self.state = State.STUDY
                    continue

                match week_day:
                    case 1 | 2 | 4:
                        print('  *Chats with friends*')
                    case 3:
                        print('  *Goes out with friends*')
                        if hour == 19:
                            print('Time to go home')
                            self.state = State.EAT
                    case 5:
                        print('  *plays computer games*')

                    case 7:
                        if hour == 13.5 or hour == 19.5:
                            self.state = State.EAT
                        elif hour < 20:
                            print('  *Goes out to an event*')
                        else:
                            print('  *Watches a film*')

                if hour == 23.5:
                    self.state = State.SLEEP
                
                self.hunger += 0.5
                continue

            if self.state == State.RECOVERY:
                print('  *Walks through the park*')
                self.resource += 20
                if self.resource > 50:
                    if hour == 13.5:
                        self.state = State.EAT
                    if hour > 19:
                        self.state = State.LISTEN_TO_MUSIC
                    else:
                        self.state = State.STUDY
                continue

def live_a_week():
    me = LabRat()
    n = 1
    while n != 8:
        me.live_a_day()
        n+=1

live_a_week() #JUST RUN THIS