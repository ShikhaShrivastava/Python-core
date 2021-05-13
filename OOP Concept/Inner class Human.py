class Human:
    def __init__(self, name):
        print('Human object is created')
        self.name = name
        self.my_head = self.Head()

    def display_activities(self):
        print('Human is alive')
        self.my_head.shake()
        self.my_head.my_brain.think()

    class Head:
        def __init__(self):
            print('Head object is created')
            self.my_brain = self.Brain()

        def shake(self):
            print('Head is making some movements')

        class Brain:
            def __init__(self):
                print('Head object got created')

            def think(self):
                print('Thinking process going on')


my_human = Human('shikha')
my_human.display_activities()
