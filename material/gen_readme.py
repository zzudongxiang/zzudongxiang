import os

dir_name = 'images'
for item in ['1. 比赛获奖', '2. 专利软著', '3. 经历证明', '4. 其他']:
    filelist = os.listdir('%s/%s' % (item, dir_name))
    with open('%s/README.md' % item, 'w+') as file:
        file.writelines('# %s\n\n' % item)
        for i in range(len(filelist) - 1, -1, -1):
            item = filelist[i]
            file.writelines('![%s](%s/%s)\n\n' % (item, dir_name, item))
