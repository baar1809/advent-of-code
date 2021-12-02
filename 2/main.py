class Submarine:
    position = 0
    deep = 0

    def forward(self, x):
        self.position += x

    def down(self, x):
        self.deep += x

    def up(self, x):
        self.deep -= x


file1 = open('./2/input.txt', 'r')
lines = file1.readlines()
submarine = Submarine()

for line in lines:
    temp = line.replace('\n', '').split(' ')
    getattr(submarine, temp[0])(int(temp[1]))

print(submarine.position * submarine.deep)