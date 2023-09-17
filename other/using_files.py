my_file = open('xmen.txt', 'w+')
my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n'
    'Nightcrawler\n'
])

my_file.close()


my_file = open('xmen.txt', 'r')
print(my_file.read())
#my_file.seek(0)
my_file.close()

#
with open('xmen.txt', 'w+') as my_file2:
    my_file2 = open('xmen.txt', 'w+')
    my_file2.write('Beast\n')
    my_file2.write('Phoenix\n')
    my_file2.writelines([
        'Cyclops\n',
        'Bishop\n'
        'Nightcrawler\n'
    ])