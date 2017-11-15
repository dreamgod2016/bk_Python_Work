import svn.common

username = ''
password = ''


if __name__ == '__main__':
    new_svn = svn.common.CommonClient('https://code.bk.tencent.com/apps/campus/song-e-test1', 'url', username, password)
    new_svn.run_command('co', ['--depth=empty', 'https://code.bk.tencent.com/apps/campus/song-e-test1/trunk', '.'])
    new_svn.run_command('up', ['README'])
    f = open('README', 'a')
    f.write('\nhello bk!')
    f.close()
    new_svn.run_command('commit', ['-m', '"use svn by py!"'])    